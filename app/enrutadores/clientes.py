from fastapi import APIRouter, HTTPException, status
from modelos.cliente import cliente, ClearCliente, EditarCliente

rutas_clientes = APIRouter()

lista_clientes:list[cliente] = []

@rutas_clientes.get("/clientes", response_model=list[cliente])
def Listar_clientes():
    return lista_clientes

@rutas_clientes.get("/clientes/{clientes_id}", response_model=(cliente))
async def Listar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate (lista_clientes):
        if obj_cliente.id == cliente_id:
             return obj_cliente
    raise HTTPException(status_code=400,detail=f"el cliente con el id {cliente_id}, no existe.")

@rutas_clientes.post("/clientes", response_model=cliente)
async def crear_cliente(datos_cliente: ClearCliente):
    Validar_cliente = cliente.model_validate(datos_cliente.model_dump())
    id_cliente = len(lista_clientes)+1
    Validar_cliente.id = id_cliente
    lista_clientes.append(Validar_cliente)
    return Validar_cliente

@rutas_clientes.patch("/clientes/{cliente_id}", response_model=cliente)
async def editar_cliente(cliente_id: int, datos_cliente: EditarCliente):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            Validar_cliente = cliente.model_validate(datos_cliente.model_dump())
            Validar_cliente.id = cliente_id
            lista_clientes[i] = Validar_cliente
            return Validar_cliente
    raise HTTPException(status_code=400,detail=f"el cliente con id {cliente_id}, no existe.")

@rutas_clientes.delete("/clientes/{cliente_id}", response_model=cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(status_code=400, detail=f"El cliente con id {cliente_id}, no existe.")
