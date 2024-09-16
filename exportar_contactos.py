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

    # Insertar los datos de los contactos
    for i, (nombre, info) in enumerate(contactos.items(), start=2):
        sheet[f"A{i}"] = nombre
        sheet[f"B{i}"] = info["apellido"]
        sheet[f"C{i}"] = info["teléfono"]
        sheet[f"D{i}"] = info["dirección"]

    # Guardar el archivo
    archivo = filedialog.asksaveasfilename(
        defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")]
    )
    if archivo:
        workbook.save(archivo)
        messagebox.showinfo("Éxito", f"Contactos guardados en {archivo}")
