from pydantic import BaseModel

class AsignarRolDTO(BaseModel):
    usuario_id: str
    rol_id: str