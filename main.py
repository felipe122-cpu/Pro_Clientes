from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def mensaje():
    return {"mensaje": "Este es el proyecto de clientes a desarrollar"}

clientes = []
@app.get("/clientes")
def clientes():
    return {"clientes": ["Jhon", "Pipe", "Suns", "Yoberson", "Quiroga"]}
