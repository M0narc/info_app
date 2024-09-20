# info_app
Aplicacion para la segunda parte del informatorio.

# Recursos
Recursos para poder saber mas sobre tkinter
https://www.pythontutorial.net/tkinter/

# Agenda
Crear una agenda queacepte campos de 
nombre,apellido, numero y direccion

se usa Faker para crear dummy data

# Trello
Charlar con el equipo quien se asigna que tarjeta y los pasos a seguir.
Asignarte la tarjeta y moverla a "en proceso"
https://trello.com/b/P1Cah6xX/proyecto-to-do-list


# Como correr el proyecto
- Clonar el proyecto con el comando -> 
 `git clone https://github.com/M0narc/info_app.git`

- dentro de la carpeta del proyecto crear un virtual environment(entorno virtual o venv) usando la linea de comandos (cmd)
  el comando para crear el virtual environment es el siguiente
  `python -m venv venv`
  o alternativamente
  `python3 -m venv venv`

- Instalar tkinter usando pip
 `pip install -r requirements.txt`
 

- Ejecutar el archivo.
 `python main.py `
 o de forma alternativa
 `python3 main.py`

 # Para comenzar a trabajar tienes que crearte tu propia rama
 - Para revisar la rama en la que te encuentras tienes que usar -> `git branch`
   y veras en la linea de comandos los branches disponibles.

 - Revisar que estas en el branch "`Main`", realizar un "`git pull`" para traer todos los nuevos cambios
  para luego crear tu branch: 
  `git checkout -b <tu_nombre>/<abreviacion_del_nombre_del_ticket>`
  revisar con "`git branch`" que efectivamente estas parado en la branch correcta, una vez confirmado comenzar a trabajar


# Como testear

- Agregar los campos correspondientes para agregar contactos (numero de telefono solo toma numeros y -)
  y agregar el contacto.
- Tambien puedes agregar la data falsa con el boton de fake data.
- Puedes descargar un excel con los contactos.
- Limpiar la agenda.
- Luego de agregar los suficientes contactos puedes usar el scroll de la app en la lista de contactos.
- Puedes revisar toda la info de los usuarios individualmente.
- Puedes actualizar los contactos.
