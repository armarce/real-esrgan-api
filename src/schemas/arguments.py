from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class Arguments(BaseModel):
    model_name: str = Field(default='RealESRGAN_x4plus')
    outscale: int = Field(default=2)
    tile: int = Field(default=0)
    face_enhance: bool = Field(default=False)
    ext: str = Field(default="auto")
    model_config = ConfigDict(
        protected_namespaces=()
    )