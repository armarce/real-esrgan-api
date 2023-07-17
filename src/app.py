from fastapi import FastAPI
from routes.real_esrgan_route import real_esrgan
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Real ESRGAN API",
    version="0.1",  
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    }
)

#app.mount("/results", StaticFiles(directory="/home/real-esrgan-api/results"), name="results")

app.include_router(real_esrgan)