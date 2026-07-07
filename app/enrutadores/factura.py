from fastapi import APIRouter, HTTPException, status
from modelos.factura import factura, CrearFactura, EditarFactura

rutas_factura = APIRouter()

lista_factura:list[factura] = []

@rutas_factura.get("/facturas", response_model=list[factura])
async def listar_facturas():
    return lista_factura

@rutas_factura.get("/facturas/{factura_id}", response_model=factura)
async def listar_factura(factura_id: int):
    for i, obj_factura in enumerate (lista_facturas):
        if obj_factura.id == factura_id:
             return obj_factura
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST ,detail=f"la factura con el id {factura_id}, no existe.")

@rutas_factura.post("/facturas/{cliente_id}", response_model=factura)
async def crear_factura(cliente_id: int, datos_factura: CrearFactura):
    cliente_encontrado = None
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente

    if not cliente_encontrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"el cliente con id {cliente_id} no existe.")

    facturaValidar = factura.model_validate(datos_factura.model_dump())
    facturaValidar.cliente = cliente_encontrado
    facturaValidar.id =  len(lista_factura)+1
    lista_factura.append(facturaValidar)
    return facturaValidar


@rutas_factura.patch("/facturas/{factura_id}", response_model=factura)
async def editar_factura(factura_id: int, datos_factura: EditarFactura):
    for i, obj_factura in enumerate(lista_factura):
        if obj_factura.id == factura_id:
            Validar_factura = factura.model_validate(datos_factura.model_dump())
            Validar_factura.id = factura_id
            lista_facturas[i] = Validar_factura
            return Validar_factura
    raise HTTPException(status_code=400,detail=f"el cliente con id {factura_id}, no existe.")

@rutas_factura.delete("/facturas/{factura_id}", response_model=factura)
async def eliminar_factura(factura_id):
    for i, obj_factura in enumerate(lista_factura):
        if obj_factura.id == factura_id:
            factura_eliminada = lista_factura.pop(i)
            return factura_eliminada
    raise HTTPException(status_code=400, detail=f"La factura con id {factura_id}, no existe.")