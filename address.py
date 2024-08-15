import tkinter as tk
from tkinter import messagebox
import time

# Función para mostrar la hora actual
def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

# Función para agregar un contacto
def agregar_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    direccion = entrada_direccion.get()
    
    if nombre and telefono and direccion:
        lista_contactos.insert(tk.END, nombre)
        contactos[nombre] = {"teléfono": telefono, "dirección": direccion}
        entrada_nombre.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)
        entrada_direccion.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos antes de agregar un contacto.")

# Función para eliminar un contacto
def eliminar_contacto():
    seleccion = lista_contactos.curselection()
    if seleccion:
        nombre = lista_contactos.get(seleccion[0])
        lista_contactos.delete(seleccion)
        del contactos[nombre]
    else:
        messagebox.showwarning("Selección de contacto", "Por favor, selecciona un contacto de la lista.")

# Función para mostrar la ventana modal con la información del contacto
def mostrar_info_contacto():
    seleccion = lista_contactos.curselection()
    if not seleccion:
        messagebox.showwarning("Selección de contacto", "Por favor, selecciona un contacto de la lista.")
        return

    nombre = lista_contactos.get(seleccion[0])
    contacto = contactos.get(nombre)

    # Crear una ventana modal
    modal_ventana = tk.Toplevel(ventana)
    modal_ventana.title("Información Detallada del Contacto")
    modal_ventana.geometry('300x200')

    tk.Label(modal_ventana, text=f"Nombre: {nombre}").pack(side='top', anchor='nw',padx=(0, 10), pady=5)
    tk.Label(modal_ventana, text=f"Teléfono: {contacto['teléfono']}").pack(side='top', anchor='nw',padx=(0, 10), pady=5)
    tk.Label(modal_ventana, text=f"Dirección: {contacto['dirección']}").pack(side='top', anchor='nw',padx=(0, 10), pady=5)

    tk.Button(modal_ventana, text="Cerrar", command=modal_ventana.destroy).pack(pady=10)


# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Función para limpiar la lista de contactos
def limpiar_lista():
    lista_contactos.delete(0, tk.END)
    contactos.clear()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Agenda de Contactos')
ventana.geometry('500x500')

# Crear el menú desplegable
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Principal', menu=menu_principal)
menu_principal.add_command(label='Limpiar lista', command=limpiar_lista)
menu_principal.add_command(label='Salir', command=salir)

# Crear el reloj en la parte superior derecha
reloj = tk.Label(ventana, font=('Arial', 20), fg='black', bg='white')
reloj.place(relx=1.0, rely=0.0, anchor='ne')
hora()

# Marco para el boton de nombre
marco_nombre = tk.Frame(ventana)
marco_nombre.pack(anchor='nw', padx=10, pady=(10, 0))


# Crear las entradas para los detalles del contacto
tk.Label(marco_nombre, text="Nombre:").pack(side='left', padx=(0, 10))
entrada_nombre = tk.Entry(marco_nombre)
entrada_nombre.pack(side='left')

# Marco para los botones de telefono y direccion
marco_contacto = tk.Frame(ventana)
marco_contacto.pack(anchor='nw', padx=10, pady=(10, 0))

tk.Label(marco_contacto, text="Teléfono:").pack(side='left', padx=(0, 10))
entrada_telefono = tk.Entry(marco_contacto)
entrada_telefono.pack(side='left', padx=(0,10))

tk.Label(marco_contacto, text="Dirección:").pack(side='left', padx=(0, 10))
entrada_direccion = tk.Entry(marco_contacto)
entrada_direccion.pack(side='left', padx=(0, 10))

# Botón para agregar un contacto
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

# Botón para eliminar un contacto
boton_eliminar = tk.Button(marco_botones_abajo, text='Eliminar Contacto', command=eliminar_contacto)
boton_eliminar.pack(side='left', anchor='nw', padx=10, pady=(0,10))

# Botón para mostrar la información detallada del contacto
boton_mostrar_info = tk.Button(marco_botones_abajo, text='Mostrar Info', command=mostrar_info_contacto)
boton_mostrar_info.pack(side='left', anchor='nw', padx=(0, 10))

# Iniciar el bucle de la ventana
ventana.mainloop()
