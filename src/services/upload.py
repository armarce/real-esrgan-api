import os
import shutil
from fastapi import HTTPException

async def save_image(uuid, input):

    content_type = input.content_type

    if content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    file_extension = os.path.splitext(input.filename)[1]
    file_path = "../uploads/" + uuid + file_extension.lower()

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(input.file, buffer)
    return file_path