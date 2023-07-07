from fastapi import HTTPException
from services.upload import save_image
import mimetypes
import base64
import os
import subprocess
from pathlib import Path
import uuid

random_uuid = str(uuid.uuid4())

class RealEsrganController:

    def __init__(self, arguments, input):
        self.arguments = arguments
        self.input = input

        if not bool(input):
            raise HTTPException(status_code=422, detail="Input file is required")

    async def restoration(self):
        
        arguments = dict(self.arguments)

        #python ../Real-ESRGAN/inference_realesrgan.py  -n RealESRGAN_x4plus -i ../results/jime1.jpg --face_enhance --fp32 --out ../results
        file_path_upload_image = await save_image(random_uuid, self.input)

        input = "--input " + file_path_upload_image
        output = "--output /home/real-esrgan-api/results"

        list_arguments = [input, output]

        for argument_key in arguments:

            if arguments[argument_key] != None:
                
                if argument_key == "face_enhance":
                    list_arguments.append(" --face_enhance")
                else:
                    list_arguments.append(" --{argument} {argument_value}".format(argument = argument_key, argument_value = str(arguments[argument_key])))
            
            else:

                list_arguments.append("")
        
        cmd = "python /home/real-esrgan-api/Real-ESRGAN/inference_realesrgan.py {} {}{}{}{}{}{}"
        print(cmd)
        cmd = cmd.format(*list_arguments)
        cmd_output = subprocess.check_output(cmd.split(" "), stderr=subprocess.STDOUT).decode("utf-8")

        file_extension = os.path.splitext(file_path_upload_image)[1]

        match arguments['ext']:
            
            case "jpg":

                file_extension = ".jpg"

            case "png":    

                file_extension = ".png"
        

        file_path_output_image = "/home/real-esrgan-api/results/{}_out{}".format(Path(file_path_upload_image).stem, file_extension) 

        with open(file_path_output_image, "rb") as image_file:
            encoded_image_string = base64.b64encode(image_file.read())

        mime_type = mimetypes.guess_type(file_path_output_image)[0]    
        
        return {
            #B"cmd_output": cmd_output, 
	    "image_url": "http://75.191.38.75:42271/results/{}_out{}".format(Path(file_path_upload_image).stem, file_extension),
            #"ext": file_extension, 
            #"image": "data:"+mime_type+";base64,"+encoded_image_string.decode("utf-8")
        }