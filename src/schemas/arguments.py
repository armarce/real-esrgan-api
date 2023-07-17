from pydantic import BaseModel, Field
from typing import Optional

class Arguments(BaseModel):
    model: str = Field(default='RealESRGAN_x4plus')
    outscale: int = Field(default=2)
    tile: int = Field(default=0)
    face_enhace: bool = Field(default=False)
    ext: str = Field(default="auto")
    dn: float = Field(default=1)