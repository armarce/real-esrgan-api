from fastapi import FastAPI
from routes.real_esrgan_route import real_esrgan
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#app.mount("/results", StaticFiles(directory="/home/real-esrgan-api/results"), name="results")

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(real_esrgan)