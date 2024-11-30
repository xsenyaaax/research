import os

from sanic import Sanic, response
from sanic.request import Request
from sanic.response import ResponseStream, file_stream
from typing import Optional
import asyncio
import uuid


app = Sanic("SanicApp")

FILES = {
    "file1": "/home/senyaaa/Work/research/large_file.bin",
}
CHUNK_SIZE = 1024 * 1024
client_offsets = {}
chunk_size = 1024 * 1024
file_path = '/home/senyaaa/Work/research/large_file.bin'


@app.get("/simple-response")
async def simple_response(request: Request):
    """
    Simple response endpoint.
    """
    return response.json({"message": "Hello, world!"})


@app.post("/process-jwe")
async def process_jwe(request: Request):
    """
    Simulate decryption/encryption with a small delay.
    """
    data = request.json
    await asyncio.sleep(2)
    return response.json({"status": "Processed", "data": data})


@app.get("/stream-file")
async def stream_file(request):
    try:
        chunk_index = int(request.args.get("chunk_index", 0))
        with open(file_path, "rb") as file:
            file.seek(chunk_index * chunk_size)
            chunk = file.read(chunk_size)
            if not chunk:
                return response.text("Requested chunk out of range", status=416)
            return response.raw(chunk, content_type="application/octet-stream")
    except FileNotFoundError:
        return response.text("File not found", status=404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)