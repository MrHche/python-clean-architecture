from dataclasses import dataclass
from typing import Optional

@dataclass
class Rol:
    id: str
    nombre: str
    descripcion: Optional[str] = None