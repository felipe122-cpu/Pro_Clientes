from sqlmodel import Session,SQLModel,create_engine
from fastapi import FastAPI, Depends
from typing import Annotated

nombre_bs = "bs_clientes.sqlite3"
url_bs = f"sqlite:///{nombre_bs}"

motor_bs = create_engine(url_bs)

def crear_tablas(app: FastAPI):
    SQLModel.metadata.create_all(motor_bs)
    yield

def obtener_sesion():
    with Session(motor_bs) as mi_sesion:
        yield mi_sesion

Sesion_dependecia = Annotated[Session, Depends(obtener_sesion)]