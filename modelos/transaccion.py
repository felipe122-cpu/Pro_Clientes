from pydantic import BaseModel


class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    factura_id: int

class CrearTransaccion(TransaccionBase):
    pass

class EditarTransaccion(TransaccionBase):
    pass

class Transaccion(TransaccionBase):
    id: int | None = None
    #aqui va la relación con el modelo cliente(solo un campo)