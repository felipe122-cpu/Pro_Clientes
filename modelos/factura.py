from pydantic import BaseModel
from cliente import cliente

class FacturarBase(BaseModel):
    fecha: str
    vr_total: float  #calcular(cantidad * vr_unitario)
    cliente: cliente  #esta es la relación con el cliente(objeto)


class CrearFactura(FacturarBase):
    pass

class EditarFactura(FacturarBase):
    pass

class factura(FacturarBase):
    id: int | None = None