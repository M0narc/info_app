from faker import Faker
import tkinter as tk

fake = Faker()


def agregar_contactos_falsos(lista_contactos, contactos):
    """Genera contactos falsos usando Faker."""
    cantidad = 10
    for _ in range(cantidad):
        nombre = fake.name()
        apellido = fake.last_name()
        nombre_completo = f"{nombre} {apellido}"
        telefono = fake.phone_number().replace("x", " ")
        direccion = fake.address().replace("\n", ", ")

        lista_contactos.insert(tk.END, nombre_completo)
        contactos[nombre_completo] = {
            "nombre": nombre,
            "apellido": apellido,
            "teléfono": telefono,
            "dirección": direccion,
        }
