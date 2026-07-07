from fastapi import FastAPI, HTTPException, status
from .modelos.cliente import cliente, ClearCliente, EditarCliente
from .modelos.factura import factura, CrearFactura, EditarFactura
from .modelos.transaccion import Transaccion, CrearTransaccion, EditarTransaccion
from .enrutadores import clientes,transaccion,factura

app = FastAPI()

# lista_clientes:list[cliente] = []
# lista_factura:list[factura] = []
# lista_transaccion:list[Transaccion] = []


app.include_router(clientes.rutas_clientes, tags=["Clientes"])
app.include_router(factura.rutas_factura, tags=["Factura"])
app.include_router(transaccion.rutas_Transaccion, tags=["Transacción"])