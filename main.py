from fastapi import FastAPI, HTTPException
from modelos.cliente import cliente, ClearCliente, EditarCliente

app = FastAPI()

lista_clientes:list[cliente] = []


@app.get("/clientes", response_model=list[cliente])
def clientes():
    return lista_clientes

@app.get("/clientes/{idClientes}", response_model=(cliente))
async def clientes(cliente_id: int):
    for i, obj_cliente in enumerate (lista_clientes):
        if obj_cliente.id == cliente_id:
             return obj_cliente

@app.post("/clientes", response_model=cliente)
async def crear_cliente(datos_cliente: ClearCliente):
    Validar_cliente = cliente.model_validate(datos_cliente.model_dump())
    id_cliente = len(lista_clientes)+1
    Validar_cliente.id = id_cliente
    lista_clientes.append(Validar_cliente)
    return Validar_cliente

@app.patch("/clientes/{cliente_id}", response_model=cliente)
async def editar_cliente(cliente_id: int, datos_cliente: EditarCliente):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            Validar_cliente = cliente.model_validate(datos_cliente.model_dump())
            Validar_cliente.id = cliente_id
            lista_clientes[i] = Validar_cliente
            return Validar_cliente
    raise HTTPException(status_code=400,detail=f"el cliente con id {cliente_id}, no existe.")