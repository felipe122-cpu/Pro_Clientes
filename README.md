# Datos personales

- nombre: Jhoan Felipe Hernandez Murcia
- Correo: felipe122pro@gmail.com
- Analisis y desarrolo de software
- ficha: 3407180
- Instructor: Jhonny Gerrero
- Fecha: 25/05/2026

# Paso a paso 

- primero se crea el entorno virtual
- despues activar el entorno virtual
- despues intalar el framework
- despues verificar lo que se instalo
- Luego hacemos el codigo
- Luego iniciamos el servidor
- Y se mira si esta funcionando bien
- ya verificado se crea el repositorio en github para subir el proyecto
- Y se sube el proyecto a github

# Comandos y Descripción

# En la consola
- "python --version"  Para ver la version de python que tengo instalado
- "pip --version"  Para ver la version de pip que tengo instalado

# terminal
- "python -m venv entorno"  Para crear el entorno virtual
- ".\entorno\Scripts\activate"  Para activar el entorno virtual
- "pip install "fastapi[standard]""  Para instalar fastapi
- "pip list"  Para ver que se intalo y las versiones de fastapi que instalo
- "fastapi dev main.py"  Para iniciar el servidor local

# Subirlo al repositorio
## Terminal bash

- "git init -b main"
- "Git config --global --replace-all user.name"
- "Git config --global --replace-all user.email"
- "Git add A"
- "Git commit -m "nombre del commit""
- "git remote add origin https://github.com/felipe122-cpu/Pro_Clientes.git"
- "Git push -u origin main"

# Videos
## Listar clientes
- paso a paso 
1. se importa la libreria de para los modelos "from pydantic import BaseModel"
2. se hace la lista
3. se crea la clase lista
4. se crea la variable para buscar el id
5. se crea la variable con el metodo *post* para uno mismo crear el cliente

## Crear modelos
- paso a paso 
1. se coloca en todos los decoradores "response_model=(cliente)" para que retorne todos los datos del cliente, exempo a el primer decorador, por que es una lista, entonces se pone "response_model=list[cliente]"
2. se crea una carpeta para los modelos, separando las clases
3. se separan
4. se validan los datos con una variable "Validar_cliente = cliente.model_validate(datos_cliente.model_dump())"

## Creación endpoint listar
- paso a paso
1. Habilitar la programación asincrona con "async"
2. Hacer endpoint con patch
3. Generar id
4. Crear clase editar cliente
5. Importar clase
6. Hacer codigo
7. Validar los datos que se van a enviar

## endpoints vacios
- paso a paso
1. Crear listas de factura y transacción
2. Crear los modulos de factura y transacción
3. Hacer codigo

## edicion de endpoint factura
- paso a paso
1. editar el listar facturas
2. importar dependecia status
3. implementar status con "status.HTTP._400_BAD_REQUEST"