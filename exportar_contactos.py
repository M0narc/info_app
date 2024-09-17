import openpyxl
from tkinter import filedialog, messagebox

def exportar_contactos(contactos):
    """Función para descargar la lista de contactos como un archivo Excel"""
    if not contactos:
        messagebox.showwarning("Sin contactos", "No hay contactos para descargar.")
        return

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Contactos"

    # Nombres para las columnas
    sheet["A1"] = "Nombre"
    sheet["B1"] = "Apellido"
    sheet["C1"] = "Teléfono"
    sheet["D1"] = "Dirección"

    # Insertar los datos de los contactos en las columnas correspondientes
    for i, (_, info) in enumerate(contactos.items(), start=2):
        # despues de "nombre" va un , "" en caso de algun error imprevisto
        # en lugar de tirar un error rellena el campo con un espacio
        # en blanco.
        sheet[f"A{i}"] = info.get("nombre", "")
        sheet[f"B{i}"] = info.get("apellido", "")
        sheet[f"C{i}"] = info.get("teléfono", "")
        sheet[f"D{i}"] = info.get("dirección", "")

    # indicar el formato
    archivo = filedialog.asksaveasfilename(
        defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")]
    )
    if archivo:
        workbook.save(archivo)
        messagebox.showinfo("Éxito", f"Contactos guardados en {archivo}")
