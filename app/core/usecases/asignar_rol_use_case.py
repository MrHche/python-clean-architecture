from app.core.dtos.rol_dto import AsignarRolDTO

class AsignarRolUseCase:
    # Recibe las interfaces (puertos) inyectadas, respetando Clean Architecture
    def __init__(self, usuario_repository, rol_repository):
        self.usuario_repo = usuario_repository
        self.rol_repo = rol_repository

    def ejecutar(self, dto: AsignarRolDTO) -> bool:
        # 1. Valida que el rol exista usando el repositorio
        rol = self.rol_repo.obtener_por_id(dto.rol_id)
        if not rol:
            raise ValueError("El rol especificado no existe.")
        
        # 2. Asigna el rol al usuario
        return self.usuario_repo.agregar_rol(dto.usuario_id, dto.rol_id)