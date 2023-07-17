from pydantic import BaseModel
from typing import Optional

class Arguments(BaseModel):
    model: Optional[str]
    outscale: Optional[int]
    tile: Optional[str]
    face_enhance: Optional[bool]
    ext: Optional[str]
    dn: Optional[float]