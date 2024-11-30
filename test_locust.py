from locust import HttpUser, TaskSet, task, between, constant


class UserBehavior(TaskSet):
    completed_downloads = set()
    file_chunk_size = 1024 * 1024  # 1 MB
    total_chunks = 4000  # 4 GB
    current_chunk = 0  # Track the current chunk being downloaded by this user


    @task(1)
    def test_simple_response(self):
        """
        Test fetching a simple response from the server.
        """
        with self.client.get("/simple-response", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status code {response.status_code}")

    @task(1)
    def test_process_jwe(self):
        """
        Test the JWE processing endpoint.
        """
        payload = {"key": "value"}
        with self.client.post("/process-jwe", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status code {response.status_code}")

    @task(4)
    def test_stream_large_file(self):
        chunk_index = self.current_chunk
        self.current_chunk = (self.current_chunk + 1) % self.total_chunks

        # Request a single chunk
        with self.client.get(
                f"/stream-file?chunk_index={chunk_index}",
                stream=True,
                name="/stream-large-file",
                catch_response=True
        ) as response:
            if response.status_code == 200:
                # Simulate processing the received chunk
                for _ in response.iter_content(chunk_size=self.file_chunk_size):
                    pass
                response.success()
            elif response.status_code == 416:  # Requested chunk out of range
                print(f"Chunk {chunk_index} out of range.")
                response.success()
            else:
                response.failure(f"Failed with status code {response.status_code}")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(0, 1)
    #wait_time = constant(0)
