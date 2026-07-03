from fastapi import FastAPI, HTTPException, status
from modelos.cliente import cliente, ClearCliente, EditarCliente
from modelos.factura import factura, CrearFactura, EditarFactura
from modelos.transaccion import Transaccion, CrearTransaccion, EditarTransaccion

app = FastAPI()

lista_clientes:list[cliente] = []
lista_factura:list[factura] = []
lista_transaccion:list[Transaccion] = []


@app.get("/clientes", response_model=list[cliente])
def clientes():
    return lista_clientes

@app.get("/clientes/{clientes_id}", response_model=(cliente))
async def clientes(cliente_id: int):
    for i, obj_cliente in enumerate (lista_clientes):
        if obj_cliente.id == cliente_id:
             return obj_cliente
    raise HTTPException(status_code=400,detail=f"el cliente con el id {cliente_id}, no existe.")

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

@app.delete("/clientes/{cliente_id}", response_model=cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )

#endpoint Factura

@app.get("/facturas", response_model=list[factura])
async def listar_facturas():
    return lista_factura


@app.get("/facturas/{factura_id}", response_model=factura)
async def listar_factura(factura_id: int):
    for i, obj_factura in enumerate (lista_facturas):
        if obj_factura.id == factura_id:
             return obj_factura
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST ,detail=f"la factura con el id {factura_id}, no existe.")

@app.post("/facturas/{cliente_id}", response_model=factura)
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


@app.patch("/facturas/{factura_id}", response_model=factura)
async def editar_factura(factura_id: int, datos_factura: factura):
    for i, obj_factura in enumerate(lista_factura):
        if obj_factura.id == factura_id:
            Validar_factura = factura.model_validate(datos_factura.model_dump())
            Validar_factura.id = factura_id
            lista_facturas[i] = Validar_factura
            return Validar_factura
    raise HTTPException(status_code=400,detail=f"el cliente con id {factura_id}, no existe.")

@app.delete("/facturas/{factura_id}", response_model=factura)
async def eliminar_factura(factura_id):
    for i, obj_factura in enumerate(lista_factura):
        if obj_factura.id == factura_id:
            factura_eliminada = lista_factura.pop(i)
            return factura_eliminada
    raise HTTPException(status_code=400, detail=f"La factura con id {factura_id}, no existe.")

#endpoint Transacción
@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transaccion


@app.get("/transacciones/{transaccion_id}", response_model=Transaccion)
async def listar_transaccion(transaccion_id: int):
    for i, obj_transaccion in enumerate (lista_transaccion):
        if obj_transaccion.id == transaccion_id:
             return obj_transaccion
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST ,detail=f"la transaccion con el id {transaccion_id}, no existe.")


@app.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: transaccionCrear):
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


@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    for i, obj_transaccion in enumerate(lista_transaccion):
        if obj_transaccion.id == transaccion_id:
            Validar_transaccion = transaccion.model_validate(datos_transaccion.model_dump())
            Validar_transaccion.id = transaccion_id
            lista_transacciones[i] = Validar_transaccion
            return Validar_transaccion
    raise HTTPException(status_code=400,detail=f"La transaccion con id {transaccion_id}, no existe.")


@app.delete("/transacciones/{transaccion_id}", response_model=Transaccion)
async def eliminar_transaccion(transaccion_id: int):
    for i, obj_transaccion in enumerate(lista_transaccion):
        if obj_transaccion.id == transaccion_id:
            transaccion_eliminada = lista_transaccion.pop(i)
            return transaccion_eliminada
    raise HTTPException(status_code=400, detail=f"La transaccion con id {transaccion_id}, no existe.")