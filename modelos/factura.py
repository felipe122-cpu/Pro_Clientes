from pydantic import BaseModel, computed_field
from .cliente import cliente
from datetime import datetime
from .transaccion import Transaccion

class FacturarBase(BaseModel):
    fecha: str = datetime.now()
      #calcular(cantidad * vr_unitario)
    cliente: cliente  #esta es la relación con el cliente(objeto)
    transacciones: list[Transaccion] = []

    @computed_field  #Permite definir propiedades o metodos que se calculan de otros campos 
    @property  #Para convertir un metodo en una propiedad 
    def vr_total(self) -> float:
        return 0


class CrearFactura(FacturarBase):
    pass 

class EditarFactura(FacturarBase):
    pass

class factura(FacturarBase):
    id: int | None = None