import tkinter as tk
from reloj import hora
from contactos import (
    agregar_contacto,
    eliminar_contacto,
    mostrar_info_contacto,
    limpiar_lista,
)
from faker_data import agregar_contactos_falsos
from exportar_contactos import exportar_contactos
from validaciones import validar_telefono


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda de Contactos")
ventana.geometry("500x500")

# Menu desplegable
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Principal", menu=menu_principal)
menu_principal.add_command(
    label="Limpiar lista", command=lambda: limpiar_lista(lista_contactos, contactos)
)
menu_principal.add_command(
    label="Descargar contactos", command=lambda: exportar_contactos(contactos)
)
menu_principal.add_command(label="Salir", command=ventana.quit)

# Reloj en la parte superior derecha
reloj = tk.Label(ventana, font=("Arial", 10), fg="black")
reloj.place(relx=1.0, rely=0.0, anchor="ne")
hora(reloj, ventana)  # Inicia la hora actualizada

# Marco para el nombre y apellido
marco_nombre = tk.Frame(ventana)
marco_nombre.pack(anchor="nw", padx=10, pady=(10, 0))

tk.Label(marco_nombre, text="Nombre:").pack(side="left", padx=(0, 10))
entrada_nombre = tk.Entry(marco_nombre)
entrada_nombre.pack(side="left", padx=(0, 10))

tk.Label(marco_nombre, text="Apellido:").pack(side="left", padx=(2, 10))
entrada_apellido = tk.Entry(marco_nombre)
entrada_apellido.pack(side="left", padx=(6, 10))

# Marco para teléfono y dirección
marco_contacto = tk.Frame(ventana)
marco_contacto.pack(anchor="nw", padx=10, pady=(10, 0))

v_telefono = ventana.register(validar_telefono)

tk.Label(marco_contacto, text="Teléfono:").pack(side="left", padx=(0, 10))
entrada_telefono = tk.Entry(
    marco_contacto, validate="key", validatecommand=(v_telefono, "%P")
)
entrada_telefono.pack(side="left", padx=(0, 10))

tk.Label(marco_contacto, text="Dirección:").pack(side="left", padx=(0, 10))
entrada_direccion = tk.Entry(marco_contacto)
entrada_direccion.pack(side="left", padx=(0, 10))

# Botón para agregar contacto
contactos = {}  # Inicializa el diccionario de contactos

boton_agregar = tk.Button(
    ventana,
    text="Agregar Contacto",
    command=lambda: agregar_contacto(
        entrada_nombre,
        entrada_apellido,
        entrada_telefono,
        entrada_direccion,
        lista_contactos,
        contactos,
    ),
)
boton_agregar.pack(anchor="nw", padx=10, pady=10)

# Crear la lista de contactos con scrollbar
marco = tk.Frame(ventana)
marco.pack(anchor="nw", padx=10, pady=(10, 0), fill="both", expand=True)
scrollbar = tk.Scrollbar(marco)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista_contactos = tk.Listbox(marco, yscrollcommand=scrollbar.set)
lista_contactos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=lista_contactos.yview)

# Crear un marco para contener los botones de abajo
marco_botones_abajo = tk.Frame(ventana).pack(
    side="top", anchor="nw", padx=10, pady=(0, 10)
)

# Boton para eliminar un contacto
boton_eliminar = tk.Button(
    marco_botones_abajo,
    text="Eliminar Contacto",
    command=lambda: eliminar_contacto(lista_contactos, contactos),
)
boton_eliminar.pack(side="left", anchor="nw", padx=10, pady=(0, 10))

# Boton para mostrar la información detallada del contacto
boton_mostrar_info = tk.Button(
    marco_botones_abajo,
    text="Mostrar Info",
    command=lambda: mostrar_info_contacto(lista_contactos, contactos, ventana),
)
boton_mostrar_info.pack(side="left", anchor="nw", padx=(0, 10))

# Boton para agregar dummy info
boton_fake = tk.Button(
    marco_botones_abajo,
    text="F data",
    command=lambda: agregar_contactos_falsos(lista_contactos, contactos),
)
boton_fake.pack(side="left", anchor="nw", padx=(0, 10))

# Iniciar el bucle de la ventana
ventana.mainloop()
