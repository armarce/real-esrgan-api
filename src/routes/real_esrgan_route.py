from fastapi import APIRouter, File, UploadFile, Depends
from fastapi.responses import HTMLResponse
from schemas.arguments import Arguments
from controllers.RealEsrganController import RealEsrganController

real_esrgan = APIRouter()

@real_esrgan.post('/')
async def main(arguments: Arguments = Depends(), input: UploadFile = File(...)):

    return await RealEsrganController(arguments, input).restoration()
    """
    return {
        "JSON Payload ": arguments.dict(),
        "Input": input.filename
    }
    """