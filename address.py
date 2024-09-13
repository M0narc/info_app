import tkinter as tk
from tkinter import messagebox
import time
from faker import Faker

fake = Faker()

def hora():
    """Funcion para mostrar la hora actual"""
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

def agregar_contacto():
    """Funcion para agregar un contacto"""
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    telefono = entrada_telefono.get()
    direccion = entrada_direccion.get()
    
    if nombre and telefono and direccion and apellido:
        lista_contactos.insert(tk.END, nombre)
        contactos[nombre] = {"apellido": apellido,"teléfono": telefono, "dirección": direccion}
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)
        entrada_direccion.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos antes de agregar un contacto.")

def agregar_contactos_falsos():
    """Usando Faker creamos unos usuarios"""
    cantidad = 10
    for _ in range(cantidad):
        nombre = fake.name()
        apellido = fake.last_name()
        telefono = fake.phone_number().replace("x", " ")
        dir = fake.address().replace("\n", ", ")
        lista_contactos.insert(tk.END, nombre)
        contactos[nombre] = {"apellido": apellido,"teléfono": telefono, "dirección": dir}

def eliminar_contacto():
    """Función para eliminar un contacto"""
    seleccion = lista_contactos.curselection()
    if seleccion:
        nombre = lista_contactos.get(seleccion[0])
        lista_contactos.delete(seleccion)
        del contactos[nombre]
    else:
        messagebox.showwarning("Selección de contacto", "Por favor, selecciona un contacto de la lista.")

def mostrar_info_contacto():
    """Función para mostrar la ventana modal con la información del contacto"""
    seleccion = lista_contactos.curselection()
    if not seleccion:
        messagebox.showwarning("Selección de contacto", "Por favor, selecciona un contacto de la lista.")
        return

    nombre = lista_contactos.get(seleccion[0])
    contacto = contactos.get(nombre)

    # Modal
    modal_ventana = tk.Toplevel(ventana)
    modal_ventana.title("Información Detallada del Contacto")
    modal_ventana.geometry('400x200')

    tk.Label(modal_ventana, text=f"Nombre: {nombre} {contacto['apellido']}").pack(side='top', anchor='nw',padx=(0, 10), pady=5)
    # tk.Label(modal_ventana, text=f"Apellido: {contacto['apellido']}").pack(side='top', anchor='nw',padx=(0, 10), pady=5)
    tk.Label(modal_ventana, text=f"Teléfono: {contacto['teléfono']}").pack(side='top', anchor='nw',padx=(0, 10), pady=5)
    tk.Label(modal_ventana, text=f"Dirección: {contacto['dirección']}").pack(side='top', anchor='nw',padx=(0, 10), pady=5)

    tk.Button(modal_ventana, text="Cerrar", command=modal_ventana.destroy).pack(pady=10)


def salir():
    """Función para salir de la aplicación"""
    ventana.destroy()

def limpiar_lista():
    """Función para limpiar la lista de contactos"""
    lista_contactos.delete(0, tk.END)
    contactos.clear()

# Validaciones
def validar_telefono(texto):
    """validar que se permitan solo numeros o espacios en blanco"""
    return True if texto == "" or texto.replace("-","").isdigit() else False

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Agenda de Contactos')
ventana.geometry('500x500')

# menu desplegable
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Principal', menu=menu_principal)
menu_principal.add_command(label='Limpiar lista', command=limpiar_lista)
menu_principal.add_command(label='Salir', command=salir)

# reloj en la parte superior derecha
reloj = tk.Label(ventana, font=('Arial', 10), fg='black')
reloj.place(relx=1.0, rely=0.0, anchor='ne')
hora()

# Marco para el boton de nombre y apellido
marco_nombre = tk.Frame(ventana)
marco_nombre.pack(anchor='nw', padx=10, pady=(10, 0))


# Crear las entradas para los detalles del contacto
tk.Label(marco_nombre, text="Nombre:").pack(side='left', padx=(0, 10))
entrada_nombre = tk.Entry(marco_nombre)
entrada_nombre.pack(side='left', padx=(0, 10))

tk.Label(marco_nombre, text="Apellido:").pack(side='left', padx=(2, 10))
entrada_apellido = tk.Entry(marco_nombre)
entrada_apellido.pack(side='left', padx=(6, 10))

# Marco para los botones de telefono y direccion
marco_contacto = tk.Frame(ventana)
marco_contacto.pack(anchor='nw', padx=10, pady=(10, 0))

# Registro de validacion de numero
v_telefono = ventana.register(validar_telefono)

tk.Label(marco_contacto, text="Teléfono:").pack(side='left', padx=(0, 10))
entrada_telefono = tk.Entry(marco_contacto, validate="key", validatecommand=(v_telefono, '%P'))
entrada_telefono.pack(side='left', padx=(0,10))

tk.Label(marco_contacto, text="Dirección:").pack(side='left', padx=(0, 10))
entrada_direccion = tk.Entry(marco_contacto)
entrada_direccion.pack(side='left', padx=(0, 10))

# Boton para agregar un contacto
boton_agregar = tk.Button(ventana, text='Agregar Contacto', command=agregar_contacto)
boton_agregar.pack(anchor='nw', padx=10, pady=10)

# Crear el marco para la lista de contactos con scrollbar
contactos = {}
marco = tk.Frame(ventana)
marco.pack(anchor='nw', padx=10, pady=(10, 0), fill='both', expand=True)
scrollbar = tk.Scrollbar(marco)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista_contactos = tk.Listbox(marco, yscrollcommand=scrollbar.set)
lista_contactos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=lista_contactos.yview)

# Crear un marco para contener los botones de abajo
marco_botones_abajo = tk.Frame(ventana).pack(side='top', anchor='nw', padx=10, pady=(0, 10))

# Boton para eliminar un contacto
boton_eliminar = tk.Button(marco_botones_abajo, text='Eliminar Contacto', command=eliminar_contacto)
boton_eliminar.pack(side='left', anchor='nw', padx=10, pady=(0,10))

# Boton para mostrar la información detallada del contacto
boton_mostrar_info = tk.Button(marco_botones_abajo, text='Mostrar Info', command=mostrar_info_contacto)
boton_mostrar_info.pack(side='left', anchor='nw', padx=(0, 10))

# Boton para agregar dummy info
boton_fake = tk.Button(marco_botones_abajo, text='F data', command=agregar_contactos_falsos)
boton_fake.pack(side='left', anchor='nw', padx=(0, 10))

# Iniciar el bucle de la ventana
ventana.mainloop()
