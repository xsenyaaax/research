from fastapi import FastAPI, Request, Response, Header, Query, Depends, Cookie, HTTPException
from fastapi.responses import StreamingResponse
import asyncio
from typing import Optional

app = FastAPI()

FILES = {
    "file1": 4 * 1024 * 1024 * 1024,  # 4 GB
}
chunk_size = 1024 * 1024
client_offsets = {}
file_path = '/home/senyaaa/Work/research/large_file.bin'

@app.get("/simple-response")
async def simple_response():
    """
    Simple response endpoint.
    """
    return {"message": "Hello, world!"}

@app.post("/process-jwe")
async def process_jwe(request: Request):
    """
    Simulate decryption/encryption with a small delay.
    """
    data = await request.json()
    await asyncio.sleep(2)  # Simulate processing delay
    return {"status": "Processed", "data": data}


@app.get("/stream-file")
async def stream_file(chunk_index: int = Query(..., ge=0)):
    try:
        with open(file_path, "rb") as file:
            file.seek(chunk_index * chunk_size)
            chunk = file.read(chunk_size)
            if not chunk:
                raise HTTPException(status_code=416, detail="Requested chunk out of range")
            return StreamingResponse(iter([chunk]), media_type="application/octet-stream")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
