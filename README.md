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
5. se crea la variable con el metodo *post* para uno mismo crear la lista
