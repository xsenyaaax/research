 ## Python servers
 
 
1) [Sanic](https://sanic.dev/en/#-the-lightning-fast-asynchronous-python-web-framework)
* Async
* https://github.com/sanic-org/sanic 18k starts, 308 contributors
* https://sanic.dev/en/guide/advanced/streaming.html

Dependencies:
```
sanic==24.6.0
├── aiofiles [required: >=0.6.0, installed: 24.1.0] = Asynchronous file system utilities.
├── html5tagger [required: >=1.2.1, installed: 1.3.0] 
├── httptools [required: >=0.0.10, installed: 0.6.4] = Parser for HTTP requests and responses.
├── multidict [required: >=5.0,<7.0, installed: 6.1.0]
├── sanic-routing [required: >=23.12.0, installed: 23.12.0] = Routing utilities for Sanic.
├── setuptools [required: >=70.1.0, installed: 75.6.0]
├── tracerite [required: >=1.0.0, installed: 1.1.1]
│   └── html5tagger [required: >=1.2.1, installed: 1.3.0]
├── typing_extensions [required: >=4.4.0, installed: 4.12.2]
├── ujson [required: >=1.35, installed: 5.10.0]
├── uvloop [required: >=0.15.0, installed: 0.21.0] = High-performance asyncio event loop.
└── websockets [required: >=10.0, installed: 14.1] = WebSocket support.

```

2) [Bottle](https://github.com/bottlepy/bottle)
* 8.5k stars, 195 contributors
* no additional dependencies only pure python + gevent server for async I/O
* mostly synchronous but can fake async https://bottlepy.org/docs/dev/async.html
* https://bottle.readthedocs.io/en/latest/plugins/list.html JWT plugins
* 
````
bottle==0.13.2

├── geventhttpclient [required: >=2.3.1, installed: 2.3.3]
│   ├── Brotli [required: Any, installed: 1.1.0]
│   ├── certifi [required: Any, installed: 2024.8.30]
│   ├── gevent [required: Any, installed: 24.11.1]
│   │   ├── greenlet [required: >=3.1.1, installed: 3.1.1]
│   │   ├── zope.event [required: Any, installed: 5.0]
│   │   │   └── setuptools [required: Any, installed: 75.6.0]
│   │   └── zope.interface [required: Any, installed: 7.1.1]
│   │       └── setuptools [required: Any, installed: 75.6.0]
│   └── urllib3 [required: Any, installed: 2.2.3]

````

3) [CherryPy](https://github.com/cherrypy/cherrypy)
* multithreaded
* 1.9k stars, contributors 121
```
CherryPy==18.10.0
├── cheroot [required: >=8.2.1, installed: 10.0.1]
│   ├── jaraco.functools [required: Any, installed: 4.1.0]
│   │   └── more-itertools [required: Any, installed: 10.5.0]
│   └── more-itertools [required: >=2.6, installed: 10.5.0]
├── jaraco.collections [required: Any, installed: 5.1.0]
│   └── jaraco.text [required: Any, installed: 4.0.0]
│       ├── autocommand [required: Any, installed: 2.2.2]
│       ├── jaraco.context [required: >=4.1, installed: 6.0.1]
│       ├── jaraco.functools [required: Any, installed: 4.1.0]
│       │   └── more-itertools [required: Any, installed: 10.5.0]
│       └── more-itertools [required: Any, installed: 10.5.0]
├── more-itertools [required: Any, installed: 10.5.0]
├── portend [required: >=2.1.1, installed: 3.2.0]
│   └── tempora [required: >=1.8, installed: 5.7.0]
│       ├── jaraco.functools [required: >=1.20, installed: 4.1.0]
│       │   └── more-itertools [required: Any, installed: 10.5.0]
│       └── python-dateutil [required: Any, installed: 2.9.0.post0]
│           └── six [required: >=1.5, installed: 1.16.0]
└── zc.lockfile [required: Any, installed: 3.0.post1]
    └── setuptools [required: Any, installed: 75.6.0]


```

4) [FastAPI](https://github.com/fastapi/fastapi)
* Async
* 78k stars, 780 contributors
```
fastapi==0.115.5
├── pydantic [required: >=1.7.4,<3.0.0,!=2.1.0,!=2.0.1,!=2.0.0,!=1.8.1,!=1.8, installed: 2.10.1]
│   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   ├── pydantic_core [required: ==2.27.1, installed: 2.27.1]
│   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
├── starlette [required: >=0.40.0,<0.42.0, installed: 0.41.3] = ASGI framework for routing and middleware.
│   └── anyio [required: >=3.4.0,<5, installed: 4.6.2.post1]
│       ├── idna [required: >=2.8, installed: 3.10]
│       └── sniffio [required: >=1.1, installed: 1.3.1]
└── typing_extensions [required: >=4.8.0, installed: 4.12.2]

```

## Testing results:
### 3 tasks 
1) GET /simple-response to get {'message':'hello world'}
2) POST /process-jwe to simulate JWE computation with no or 2 second delay
3) GET /stream-file to get file chunk 1 MB


#### No sleep delay (NO "JWE" fake processing) 15 users concurrently

Very similar results. Bottle has a bit higher average response time

[FAST API](docs/fastapi_no_sleep.html)

[SANIC NO SLEEP](docs/sanic_no_sleep.html)

[BOTTLE](docs/bottle_no_sleep.html)

[CherryPy](docs/cherrypy_no_sleep.html)


#### With sleep delay as faking "JWE" computation for example (decrypting/encrypting)

Bottle has lower total number of sent requests, but still good results on Average response time

[FAST API](docs/fastapi_with_sleep.html)

[SANIC NO SLEEP](docs/sanic_with_sleep.html)

[BOTTLE](docs/bottle_sleep_gevent.html)

[CherryPy](docs/cherrypy_with_sleep.html)

