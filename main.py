from fastapi import FastAPI

app = FastAPI()

lista_clientes = [
        {
        "id": 1,
        "nombre": "Chanty",
        "apellido": "Beltran",
        "correo": "ChantyBeltran@gmail.com",
        "telefono": "3214567890",
        "contraseña": "123456789"
    },
    {
     "id": 2,
        "nombre": "Eddy",
        "apellido": "Suarez",
        "correo": "EddySuarez@gmail.com",
        "telefono": "3214567891",
        "contraseña": "987654321"   
    }]

@app.get("/")
def mensaje():
    return {"mensaje": "Este es el proyecto de clientes a desarrollar"}


@app.get("/clientes")
def clientes():
    return lista_clientes

@app.get("/clientes/{idClientes}")
def clientes(cliente_id):
    return lista_clientes