from pydantic import BaseModel


class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float

class CrearTransaccion(TransaccionBase):
    pass

class EditarTransaccion(TransaccionBase):
    pass

class Transaccion(TransaccionBase):
    id: int | None = None
    factura_id: int | None = None
    #aqui va la relación con el modelo Factura(solo un campo = id)