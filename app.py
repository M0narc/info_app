import tkinter as tk
import time

# Función para mostrar la hora actual
def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

# Función para agregar un contacto
def agregar_contacto():
    contacto = entrada_contacto.get()
    if contacto:
        lista_contactos.insert(tk.END, contacto)
        entrada_contacto.delete(0, tk.END)

# Función para eliminar un contacto
def eliminar_contacto():
    seleccion = lista_contactos.curselection()
    if seleccion:
        lista_contactos.delete(seleccion)

# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Función para limpiar la lista de contactos
def limpiar_lista():
    lista_contactos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Agenda de Contactos')
ventana.geometry('400x400')

# Crear el menú desplegable
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Principal', menu=menu_principal)
menu_principal.add_command(label='Limpiar lista', command=limpiar_lista)
menu_principal.add_command(label='Salir', command=salir)

# Crear el reloj
reloj = tk.Label(ventana, font=('Arial', 20), bg='blue', fg='white')
reloj.pack(anchor='n')
hora()

# Crear la entrada para agregar contactos
entrada_contacto = tk.Entry(ventana)
entrada_contacto.pack(pady=10)

# Botón para agregar un contacto
boton_agregar = tk.Button(ventana, text='Agregar Contacto', command=agregar_contacto)
boton_agregar.pack(pady=5)

# Crear el marco para la lista de contactos con scrollbar
marco = tk.Frame(ventana)
marco.pack(padx=10, pady=10)
scrollbar = tk.Scrollbar(marco)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista_contactos = tk.Listbox(marco, yscrollcommand=scrollbar.set)
lista_contactos.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=lista_contactos.yview)

# Botón para eliminar un contacto
boton_eliminar = tk.Button(ventana, text='Eliminar Contacto', command=eliminar_contacto)
boton_eliminar.pack(pady=5)

# Iniciar el bucle de la ventana
ventana.mainloop()
