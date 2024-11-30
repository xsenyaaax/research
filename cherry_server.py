import time

import cherrypy
import uuid
import asyncio
import os
from typing import Optional

FILES = {
    "file1": 4 * 1024 * 1024 * 1024,  # 4 GB
}
CHUNK_SIZE = 1024 * 1024
chunk_size = 1024 * 1024
client_offsets = {}
file_path = '/home/senyaaa/Work/research/large_file.bin'

class FileServer:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def simple_response(self):
        """
        Simple response endpoint.
        """
        return {"message": "Hello, world!"}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def process_jwe(self):
        """
        Simulate decryption/encryption with a small delay.
        """
        data = cherrypy.request.json
        time.sleep(2)
        return {"status": "Processed", "data": data}


    @cherrypy.expose
    def stream_file(self, chunk_index=0):
        try:
            chunk_index = int(chunk_index)
            with open(file_path, "rb") as file:
                file.seek(chunk_index * chunk_size)
                chunk = file.read(chunk_size)
                if not chunk:
                    cherrypy.response.status = 416
                    return "Requested chunk out of range"
                cherrypy.response.headers['Content-Type'] = 'application/octet-stream'
                return chunk
        except FileNotFoundError:
            cherrypy.response.status = 404
            return "File not found"

if __name__ == "__main__":

    num_threads = os.cpu_count()
    print(num_threads)
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
        'engine.autoreload.on': False,
        'thread_pool': num_threads,
    })


    cherrypy.tree.mount(FileServer(), '/')

    cherrypy.engine.start()
    cherrypy.engine.block()
