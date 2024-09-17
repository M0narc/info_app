def validar_telefono(texto):
    """validar que se permitan solo numeros o espacios en blanco"""
    return True if texto == "" or texto.replace("-", "").isdigit() else False
