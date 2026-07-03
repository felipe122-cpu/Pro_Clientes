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
        factura_id_actual = getattr(self, "id", None)
        TotalFactura = 0.0
        if not factura_id_actual or not self.transacciones:
            return TotalFactura
            #recorrer lista de transacciones segun el id
            for Transaccion in self.transacciones:
                if Transaccion.factura_id == factura_id_actual: 
                    TotalFactura += Transaccion.vr_unitario * Transaccion.cantidad 
        return TotalFactura


class CrearFactura(FacturarBase):
    pass 

class EditarFactura(FacturarBase):
    pass

class factura(FacturarBase):
    id: int | None = None