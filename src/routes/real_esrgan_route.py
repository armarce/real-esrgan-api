from fastapi import APIRouter, File, UploadFile, Depends
from fastapi.responses import HTMLResponse
from schemas.arguments import Arguments
from controllers.RealEsrganController import RealEsrganController

real_esrgan = APIRouter()

@real_esrgan.get('/models')
async def get_models():
    return {
        "models": ['RealESRGAN_x4plus', 'RealESRGAN_x4plus_anime_6B', 'realesr-general-x4v3']
    }

@real_esrgan.post('/')
async def main(arguments: Arguments = Depends(), input: UploadFile = File(...)):

    return await RealEsrganController(arguments, input).restoration()