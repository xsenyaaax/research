from gevent import monkey; monkey.patch_all()

import time

from bottle import Bottle, request, response, run, HTTPResponse
import uuid

app = Bottle()

FILES = {
    "file1": 4 * 1024 * 1024 * 1024,  # 4 GB
}
CHUNK_SIZE = 1024 * 1024
chunk_size = 1024 * 1024
client_offsets = {}
file_path = '/home/senyaaa/Work/research/large_file.bin'

@app.get("/simple-response")
def simple_response():
    """
    Simple response endpoint.
    """
    return {"message": "Hello, world!"}

@app.post("/process-jwe")
def process_jwe():
    """
    Simulate decryption/encryption with a small delay.
    """
    data = request.json
    time.sleep(2)
    return {"status": "Processed", "data": data}

@app.get("/stream-file")
def stream_large_file():
    try:
        chunk_index = int(request.query.get("chunk_index", 0))
        with open(file_path, "rb") as file:
            file.seek(chunk_index * chunk_size)
            chunk = file.read(chunk_size)
            if not chunk:
                response.status = 416
                return "Requested chunk out of range"
            response.content_type = "application/octet-stream"
            return HTTPResponse(chunk)
    except FileNotFoundError:
        response.status = 404
        return "File not found"


@app.route('/data')
def stream_data():
    response.content_type = 'application/octet-stream'

    def generate_data():
        for _ in range(4 * 1024):  # 4 GB
            yield b"x" * (1024 * 1024)  # 1 MB chunks
    return generate_data()


if __name__ == "__main__":
    run(app, host='0.0.0.0', port=8080, server='gevent')
