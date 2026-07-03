from fastapi import FastAPI
from modelos.cliente import cliente, ClearCliente

app = FastAPI()

lista_clientes:list[cliente] = []


@app.get("/clientes", response_model=list[cliente])
def clientes():
    return lista_clientes

@app.get("/clientes/{idClientes}", response_model=(cliente))
def clientes(cliente_id: int):
    for i, obj_cliente in enumerate (lista_clientes):
        if obj_cliente.get("id") == cliente_id:
             return obj_cliente

@app.post("/clientes", response_model=(cliente))
def crear_cliente(datos_cliente: ClearCliente):
    Validar_cliente = cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(Validar_cliente)
    return Validar_cliente