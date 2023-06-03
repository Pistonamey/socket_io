from fastapi import FastAPI
from .sockets import sio_app
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*', 'https://647bbad6a098e0451fbfcab7--stellar-sunshine-202c40.netlify.app/',
                   'https://647bbad6a098e0451fbfcab7--stellar-sunshine-202c40.netlify.app'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/home')
async def home():
    return {'message': 'Hello👋 Developers💻'}


@app.get('/tyy')
async def yum():
    return {'message': 'Hello👋 Developers💻'}

app.mount('/', app=sio_app)
