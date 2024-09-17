import openpyxl
from tkinter import filedialog, messagebox


def exportar_contactos(contactos):
    """Función para descargar la lista de contactos como un archivo Excel"""
    if not contactos:
        messagebox.showwarning("Sin contactos", "No hay contactos para descargar.")
        return

    # Crear un archivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Contactos"

    # Crear encabezados
    sheet["A1"] = "Nombre"
    sheet["B1"] = "Apellido"
    sheet["C1"] = "Teléfono"
    sheet["D1"] = "Dirección"

    print(contactos.items())
    # Insertar los datos de los contactos
    for i, (_, info) in enumerate(contactos.items(), start=2):
        # Acceder correctamente a los campos de nombre y apellido
        sheet[f"A{i}"] = info.get("nombre", "")  # Nombre
        sheet[f"B{i}"] = info.get("apellido", "")  # Apellido
        sheet[f"C{i}"] = info.get("teléfono", "")  # Teléfono
        sheet[f"D{i}"] = info.get("dirección", "")  # Dirección

    # Guardar el archivo
    archivo = filedialog.asksaveasfilename(
        defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")]
    )
    if archivo:
        workbook.save(archivo)
        messagebox.showinfo("Éxito", f"Contactos guardados en {archivo}")
