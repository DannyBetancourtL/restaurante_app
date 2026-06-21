# Clase que representa un cliente

class Cliente:
    def __init__(self, cedula, nombre, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Cédula: {self.cedula} | Nombre: {self.nombre} | Teléfono: {self.telefono}"