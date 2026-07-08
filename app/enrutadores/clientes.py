from fastapi import APIRouter, HTTPException, status
from ..modelos.cliente import cliente, ClearCliente, EditarCliente
from ..listas import lista_cliente
from ..conexion_bs import Sesion_dependecia
from sqlmodel import select

rutas_clientes = APIRouter()

# lista_clientes:list[cliente] = []

@rutas_clientes.get("/clientes", response_model=list[cliente])
def Listar_clientes(sesion: Sesion_dependecia):
    lista_clis =sesion.exec(select(cliente)).all()
    return lista_clis

@rutas_clientes.get("/clientes/{clientes_id}", response_model=cliente)
async def Listar_cliente(cliente_id: int , mi_sesion: Sesion_dependecia):
    clientebd =mi_sesion.get(cliente, cliente_id)
    if not clientebd:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"el cliente con el id {cliente_id}, no existe.")
    return clientebd

@rutas_clientes.post("/clientes", response_model=cliente)
async def crear_cliente(datos_cliente: ClearCliente , mi_sesion: Sesion_dependecia):
    Validar_cliente = cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(Validar_cliente)
    mi_sesion.commit()
    mi_sesion.refresh(Validar_cliente)
    return Validar_cliente

@rutas_clientes.patch("/clientes/{cliente_id}", response_model=cliente)
async def editar_cliente(cliente_id: int, datos_cliente: EditarCliente, mi_sesion:Sesion_dependecia):
    clientebd =mi_sesion.get(cliente, cliente_id)
    if not clientebd:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"el cliente con id {cliente_id}, no existe.")
    clienteDic = datos_cliente.model_dump(exclude_unset=True)
    clientebd.sqlmodel_update(clienteDic)
    mi_sesion.add(clientebd)
    mi_sesion.commit()
    mi_sesion.refresh(clientebd)
    return clientebd

@rutas_clientes.delete("/clientes/{cliente_id}", response_model=cliente)
async def eliminar_cliente(cliente_id: int, mi_sesion: Sesion_dependecia):
    clientebd =mi_sesion.get(cliente, cliente_id)
    if not clientebd:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El cliente con id {cliente_id}, no existe.")
    mi_sesion.delete(clientebd)
    mi_sesion.commit()
    return clientebd    