import time

def hora(reloj, ventana):
    """Función para mostrar la hora actual."""
    tiempo_actual = time.strftime("%H:%M:%S")
    reloj.config(text=tiempo_actual)
    ventana.after(1000, lambda: hora(reloj, ventana))
