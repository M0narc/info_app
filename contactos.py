import tkinter as tk
from tkinter import messagebox

def agregar_contacto(entrada_nombre, entrada_apellido, entrada_telefono, entrada_direccion, lista_contactos, contactos):
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    telefono = entrada_telefono.get()
    direccion = entrada_direccion.get()

    if nombre and telefono and direccion and apellido:
        lista_contactos.insert(tk.END, nombre)
        contactos[nombre] = {
            "apellido": apellido,
            "teléfono": telefono,
            "dirección": direccion,
        }
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)
        entrada_direccion.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos antes de agregar un contacto.")

def eliminar_contacto(lista_contactos, contactos):
    seleccion = lista_contactos.curselection()
    if seleccion:
        nombre = lista_contactos.get(seleccion[0])
        lista_contactos.delete(seleccion)
        del contactos[nombre]
    else:
        messagebox.showwarning("Selección de contacto", "Por favor, selecciona un contacto de la lista.")

def mostrar_info_contacto(lista_contactos, contactos, ventana):
    seleccion = lista_contactos.curselection()
    if not seleccion:
        messagebox.showwarning("Selección de contacto", "Por favor, selecciona un contacto de la lista.")
        return

    nombre = lista_contactos.get(seleccion[0])
    contacto = contactos.get(nombre)

    modal_ventana = tk.Toplevel(ventana)
    modal_ventana.title("Información Detallada del Contacto")
    modal_ventana.geometry("400x200")

    tk.Label(modal_ventana, text=f"Nombre: {nombre} {contacto['apellido']}").pack(side="top", anchor="nw", padx=(0, 10), pady=5)
    tk.Label(modal_ventana, text=f"Teléfono: {contacto['teléfono']}").pack(side="top", anchor="nw", padx=(0, 10), pady=5)
    tk.Label(modal_ventana, text=f"Dirección: {contacto['dirección']}").pack(side="top", anchor="nw", padx=(0, 10), pady=5)

    tk.Button(modal_ventana, text="Cerrar", command=modal_ventana.destroy).pack(pady=10)

def limpiar_lista(lista_contactos, contactos):
    lista_contactos.delete(0, tk.END)
    contactos.clear()
