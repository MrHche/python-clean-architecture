from fastapi import APIRouter, HTTPException, Depends
from app.core.dtos.rol_dto import AsignarRolDTO
from app.core.usecases.asignar_rol_use_case import AsignarRolUseCase

router = APIRouter(prefix="/roles", tags=["Roles"])

# Nota: Deberás importar o definir tu función de inyección de dependencias (Dependency Injection)
# Por ejemplo: from app.infra.api.dependencies import get_asignar_rol_use_case

@router.post("/asignar")
def asignar_rol(
    payload: AsignarRolDTO,
    # use_case: AsignarRolUseCase = Depends(get_asignar_rol_use_case) 
):
    """
    Endpoint para asignar un rol a un usuario.
    Descomenta la inyección de dependencias cuando configures el contenedor de FastAPI.
    """
    try:
        # exito = use_case.ejecutar(payload)
        # if not exito:
        #     raise HTTPException(status_code=400, detail="No se pudo asignar el rol")
        return {"mensaje": "Endpoint configurado correctamente en capa infra"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))