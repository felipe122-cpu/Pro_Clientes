from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista_clientes:list[cliente] = []

class cliente(BaseModel):
    id: int
    nombre: str
    apellido:str
    email: str
    telefono: int
    contraseña: str

@app.get("/")
def mensaje():
    return {"mensaje": "Este es el proyecto de clientes a desarrollar"}


@app.get("/clientes")
def clientes():
    return lista_clientes

@app.get("/clientes/{idClientes}")
def clientes(cliente_id: int):
    for i, obj_cliente in enumerate (lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente

@app.post("/clientes")
def crear_cliente(datos_cliente: cliente):
    lista_clientes.append(datos_cliente)
    return datos_cliente