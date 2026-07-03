from pydantic import BaseModel

class clienteBase(BaseModel):
    nombre: str
    apellido:str
    email: str
    telefono: int
    contraseña: str

class ClearCliente(clienteBase):
    pass

class cliente(clienteBase):
    id: int | None = None