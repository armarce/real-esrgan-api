from fastapi import HTTPException
from services.upload import save_image
import mimetypes
import base64
import os
import subprocess
from pathlib import Path
import uuid
import glob

random_uuid = str(uuid.uuid4())

class RealEsrganController:

    def __init__(self, arguments, input):
        self.arguments = arguments
        self.input = input

        if not bool(input):
            raise HTTPException(status_code=422, detail="Input file is required")

    async def restoration(self):
        
        arguments = dict(self.arguments)
        
        file_path_upload_image = await save_image(random_uuid, self.input)

        input = "--input " + file_path_upload_image
        output = "--output ../results"

        list_arguments = [input, output]

        for argument_key in arguments:

            if arguments[argument_key] != None:

                if(argument_key == 'face_enhance'): 

                    list_arguments.append("--{argument}".format(argument = argument_key))

                else:

                    list_arguments.append("--{argument} {argument_value}".format(argument = argument_key, argument_value = str(arguments[argument_key])))

            else:

                list_arguments.append("")
        
        cmd = "python ../Real-ESRGAN/inference_realesrgan.py {} {} {} {} {} {} {}"
        cmd = cmd.format(*list_arguments)
        cmd_output = subprocess.check_output(cmd.split(" "), stderr=subprocess.STDOUT).decode("utf-8")

        file_path_output_image = glob.glob("../results/{}_out".format(Path(file_path_upload_image).stem))[0]

        with open(file_path_output_image, "rb") as image_file:
            encoded_image_string = base64.b64encode(image_file.read())

        os.remove(file_path_output_image)    

        mime_type = mimetypes.guess_type(file_path_output_image)[0]    
        
        return {
            "cmd_output": cmd_output, 
            "image": "data:"+mime_type+";base64,"+encoded_image_string.decode("utf-8")
        }