import tkinter as tk
from tkinter import messagebox


def agregar_contacto(
    entrada_nombre,
    entrada_apellido,
    entrada_telefono,
    entrada_direccion,
    lista_contactos,
    contactos,
):
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    telefono = entrada_telefono.get()
    direccion = entrada_direccion.get()

    if nombre and telefono and direccion and apellido:
        nombre_completo = f"{nombre} {apellido}"
        lista_contactos.insert(tk.END, nombre_completo)
        contactos[nombre_completo] = {
            "nombre": nombre,
            "apellido": apellido,
            "teléfono": telefono,
            "dirección": direccion,
        }
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)
        entrada_direccion.delete(0, tk.END)
    else:
        messagebox.showwarning(
            "Campos vacíos",
            "Por favor, completa todos los campos antes de agregar un contacto.",
        )


def eliminar_contacto(lista_contactos, contactos):
    seleccion = lista_contactos.curselection()
    if seleccion:
        nombre_completo = lista_contactos.get(seleccion[0])
        lista_contactos.delete(seleccion)
        del contactos[nombre_completo]
    else:
        messagebox.showwarning(
            "Selección de contacto", "Por favor, selecciona un contacto de la lista."
        )



def limpiar_lista(lista_contactos, contactos):
    lista_contactos.delete(0, tk.END)
    contactos.clear()
