from fastapi import APIRouter, HTTPException, status
from modelos.transaccion import Transaccion, CrearTransaccion, EditarTransaccion
from enrutadores.factura import lista_factura

rutas_Transaccion = APIRouter()

lista_transaccion:list[Transaccion] = []

@rutas_Transaccion.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transaccion


@rutas_Transaccion.get("/transacciones/{transaccion_id}", response_model=Transaccion)
async def listar_transaccion(transaccion_id: int):
    for i, obj_transaccion in enumerate (lista_transaccion):
        if obj_transaccion.id == transaccion_id:
             return obj_transaccion
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST ,detail=f"la transaccion con el id {transaccion_id}, no existe.")


@rutas_Transaccion.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(transaccion_id: int, datos_transaccion: CrearTransaccion):
#Buscar factura
    factura_encontrada = None
    for factura in lista_factura:
        if factura.id == factura_id:
            factura_encontrada = factura

    if not factura_encontrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"la factura con id {factura_id} no existe.")

    TransaccionValidar = Transaccion.model_validate(datos_transaccion.model_dump())
    TransaccionValidar.factura_id = factura_id
    factura_encontrada.transacciones.append(TransaccionValidar)
    TransaccionValidar.id =  len(lista_transaccion)+1
    lista_transaccion.append(TransaccionValidar)
    return TransaccionValidar


@rutas_Transaccion.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: EditarTransaccion):
    for i, obj_transaccion in enumerate(lista_transaccion):
        if obj_transaccion.id == transaccion_id:
            TransaccionValidar = transaccion.model_validate(datos_transaccion.model_dump())
            TransaccionValidar.id = transaccion_id
            lista_transacciones[i] = TransaccionValidar
            return TransaccionValidar
    raise HTTPException(status_code=400,detail=f"La transaccion con id {transaccion_id}, no existe.")


@rutas_Transaccion.delete("/transacciones/{transaccion_id}", response_model=Transaccion)
async def eliminar_transaccion(transaccion_id: int):
    for i, obj_transaccion in enumerate(lista_transaccion):
        if obj_transaccion.id == transaccion_id:
            return lista_transaccion.pop(i)
    raise HTTPException(status_code=400, detail=f"La transaccion con id {transaccion_id}, no existe.")