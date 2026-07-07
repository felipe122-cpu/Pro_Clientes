from fastapi import FastAPI, HTTPException, status
from .enrutadores.clientes import rutas_clientes
from .enrutadores.factura import rutas_factura
from .enrutadores.transaccion import rutas_Transaccion
from .conexion_bs import crear_tablas

app = FastAPI(lifespan=crear_tablas)


app.include_router(rutas_clientes, tags=["Clientes"])
app.include_router(rutas_factura, tags=["Factura"])
app.include_router(rutas_Transaccion, tags=["Transacción"])