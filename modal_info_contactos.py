import tkinter as tk
from tkinter import messagebox
from validaciones import validar_telefono


def mostrar_info_contacto(lista_contactos, contactos, ventana):
    seleccion = lista_contactos.curselection()
    if not seleccion:
        messagebox.showwarning(
            "Selección de contacto", "Por favor, selecciona un contacto de la lista."
        )
        return

    nombre_completo = lista_contactos.get(seleccion[0])
    contacto = contactos.get(nombre_completo)

    modal_ventana = tk.Toplevel(ventana)
    modal_ventana.title("Información Detallada del Contacto")
    modal_ventana.geometry("400x300")

    # Mostrar la información sin permitir modificación inicialmente
    tk.Label(modal_ventana, text="Información del Contacto").pack(pady=10)

    # Nombre
    tk.Label(modal_ventana, text=f"Nombre: {contacto['nombre']}").pack(anchor="w", padx=10)

    # Apellido
    tk.Label(modal_ventana, text=f"Apellido: {contacto['apellido']}").pack(anchor="w", padx=10)

    # Teléfono
    tk.Label(modal_ventana, text=f"Teléfono: {contacto['teléfono']}").pack(anchor="w", padx=10)

    # Dirección
    tk.Label(modal_ventana, text=f"Dirección: {contacto['dirección']}").pack(anchor="w", padx=10)

    # Botón para habilitar edición
    tk.Button(
        modal_ventana,
        text="Modificar Contacto",
        command=lambda: habilitar_edicion(
            contacto,
            nombre_completo,
            lista_contactos,
            contactos,
            modal_ventana
        ),
    ).pack(pady=10)

    # Botón para cerrar la ventana
    tk.Button(modal_ventana, text="Cerrar", command=modal_ventana.destroy).pack(pady=10)


def habilitar_edicion(contacto, nombre_completo, lista_contactos, contactos, modal_ventana):
    """Habilita la edición de los campos y muestra un botón para guardar cambios."""

    # Limpiar la ventana modal
    for widget in modal_ventana.winfo_children():
        widget.destroy()

    tk.Label(modal_ventana, text="Modificar Contacto").pack(pady=10)

    # Nombre
    tk.Label(modal_ventana, text="Nombre:").pack(anchor="w")
    entrada_nombre = tk.Entry(modal_ventana)
    entrada_nombre.pack(fill="x", padx=10)
    entrada_nombre.insert(0, contacto["nombre"])

    # Apellido
    tk.Label(modal_ventana, text="Apellido:").pack(anchor="w")
    entrada_apellido = tk.Entry(modal_ventana)
    entrada_apellido.pack(fill="x", padx=10)
    entrada_apellido.insert(0, contacto["apellido"])

    # Validar teléfono
    v_telefono = modal_ventana.register(validar_telefono)

    # Teléfono
    tk.Label(modal_ventana, text="Teléfono:").pack(anchor="w")
    entrada_telefono = tk.Entry(modal_ventana, validate="key", validatecommand=(v_telefono, "%P"))
    entrada_telefono.pack(fill="x", padx=10)
    entrada_telefono.insert(0, contacto["teléfono"])

    # Dirección
    tk.Label(modal_ventana, text="Dirección:").pack(anchor="w")
    entrada_direccion = tk.Entry(modal_ventana)
    entrada_direccion.pack(fill="x", padx=10)
    entrada_direccion.insert(0, contacto["dirección"])

    # guardar cambios
    tk.Button(
        modal_ventana,
        text="Guardar Cambios",
        command=lambda: modificar_contacto(
            nombre_completo,
            entrada_nombre,
            entrada_apellido,
            entrada_telefono,
            entrada_direccion,
            lista_contactos,
            contactos,
            modal_ventana,
        ),
    ).pack(pady=10)

    # Botón para cerrar la ventana
    tk.Button(modal_ventana, text="Cerrar", command=modal_ventana.destroy).pack(pady=10)


def modificar_contacto(
    nombre_completo,
    entrada_nombre,
    entrada_apellido,
    entrada_telefono,
    entrada_direccion,
    lista_contactos,
    contactos,
    modal_ventana,
):
    """Función para modificar un contacto existente y actualizar la lista"""
    nuevo_nombre = entrada_nombre.get().strip()
    nuevo_apellido = entrada_apellido.get().strip()
    nuevo_telefono = entrada_telefono.get().strip()
    nueva_direccion = entrada_direccion.get().strip()

    if (
        not nuevo_nombre
        or not nuevo_apellido
        or not nuevo_telefono
        or not nueva_direccion
    ):
        messagebox.showwarning(
            "Campos vacíos", "Todos los campos deben estar completos."
        )
        return

    # Actualizar los datos del contacto en el diccionario
    contactos.pop(nombre_completo)  # Eliminar el contacto antiguo
    nuevo_nombre_completo = f"{nuevo_nombre} {nuevo_apellido}"
    contactos[nuevo_nombre_completo] = {
        "nombre": nuevo_nombre,
        "apellido": nuevo_apellido,
        "teléfono": nuevo_telefono,
        "dirección": nueva_direccion,
    }

    # Actualizar la lista de contactos visualmente
    index = lista_contactos.get(0, tk.END).index(nombre_completo)
    lista_contactos.delete(index)  # Eliminar el nombre viejo
    lista_contactos.insert(index, nuevo_nombre_completo)  # Insertar el nuevo nombre

    # Cerrar la ventana modal
    modal_ventana.destroy()

    messagebox.showinfo(
        "Éxito", f"El contacto {nuevo_nombre_completo} ha sido actualizado."
    )
