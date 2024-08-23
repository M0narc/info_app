import tkinter as tk


# Función para mostrar la hora actual


# Función para agregar un contacto


# Función para eliminar un contacto
def eliminar_contacto():
    seleccion=lista_contactos.curselection()
    if seleccion:
        lista_contactos.delete(seleccion)
    else:
        tk.messagebox.showwarning('Atención', 'Seleccione un contacto para eliminar')

# Función para mostrar la ventana modal con la información del contacto



# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Función para limpiar la lista de contactos


# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Agenda de Contactos')
ventana.geometry('500x500')

# Crear el menú desplegable


# Crear el reloj en la parte superior derecha


# Marco para el boton de nombre



# Crear las entradas para los detalles del contacto


# Marco para los botones de telefono y direccion


# Botón para agregar un contacto


# Crear el marco para la lista de contactos con scrollbar


# Crear un marco para contener los botones de abajo
marco_botones_inferiores = tk.Frame(ventana)
marco_botones_inferiores.pack(side=tk.LEFT, padx=10, pady=10)

# Botón para eliminar un contacto
boton_eliminar=tk.Button(marco_botones_inferiores, text='Eliminar contacto', command=eliminar_contacto)
boton_eliminar.pack(anchor='w')


# Botón para mostrar la información detallada del contacto


# Iniciar el bucle de la ventana
ventana.mainloop()
