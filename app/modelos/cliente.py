from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class clienteBase(SQLModel):
    nombre: str = Field(default=None)
    apellido: str = Field(default=None)
    email: str = Field(default=None)
    telefono: int = Field(default=None)
    contraseña: str = Field(default=None)

class ClearCliente(clienteBase):
    pass

class cliente(clienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class EditarCliente(clienteBase):
    pass