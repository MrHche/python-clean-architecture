from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

# 1. Tabla Puente (Link Model)
class UserRoleLink(SQLModel, table=True):
    __tablename__ = "user_role"
    
    # Apuntamos exactamente a "users.id" y "roles.id" usando UUID
    user_id: UUID = Field(foreign_key="users.id", primary_key=True)
    role_id: UUID = Field(foreign_key="roles.id", primary_key=True)

# 2. Modelo Principal de Rol
class RolModel(SQLModel, table=True):
    __tablename__ = "roles"

    # Usamos UUID por defecto para mantener consistencia con User
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str = Field(unique=True, index=True)
    descripcion: Optional[str] = None

    # Relación bidireccional hacia User
    users: List["User"] = Relationship(
        back_populates="roles",
        link_model=UserRoleLink
    )