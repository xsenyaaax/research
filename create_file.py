import os


def create_large_file(file_path: str, size_in_gb: int):
    """
    Create a large file of the specified size with dummy data.
    """
    size_in_bytes = size_in_gb * 1024 * 1024 * 1024

    with open(file_path, "wb") as f:
        f.write(b"0" * size_in_bytes)

    print(f"Created file at {file_path} with size {size_in_gb} GB.")


large_file_path = "/home/senyaaa/Work/research/large_file.bin"
create_large_file(large_file_path, 4)
