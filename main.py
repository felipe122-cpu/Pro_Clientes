from fastapi import FastAPI, HTTPException
from modelos.cliente import cliente, ClearCliente, EditarCliente
from modelos.factura import factura, CrearFactura, EditarFactura
from modelos.transaccion import transaccion, CrearTransaccion, EditarTransaccion

app = FastAPI()

lista_clientes:list[cliente] = []
lista_factura:list[factura] = []
Lista_transaccion:list[transaccion] = []


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

@app.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )

#endpoint Factura

@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_factura


@app.get("/facturas/{id_factura}", response_model=Factura)
async def listar_factura(id_factura: int):
    pass


@app.post("/facturas/{id_cliente}", response_model=Factura)
async def crear_factura(id_cliente: int, datos_factura: Factura):
    pass


@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass

@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura):
    pass

#endpoint Transacción
@app.get("/transacciones", response_model=list[Transaccion])
async def listar_ftransacciones():
    pass


@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass


@app.post("/transacciones/{id_factura}", response_model=Transaccion)
async def crear_transaccion(id_factura: int, datos_transaccion: Transaccion):
    pass


@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass