from uuid import UUID
from sqlmodel import Field, SQLModel, Relationship
from typing import List

# Importamos la tabla puente que conectará User con RolModel
from app.infra.db.models.rol_model import UserRoleLink

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(primary_key=True)
    name: str
    email: str = Field(unique=True)
    password_hash: str

    # Agregamos la relación N:M
    roles: List["RolModel"] = Relationship(
        back_populates="users",
        link_model=UserRoleLink
    )