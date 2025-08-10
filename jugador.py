class Jugador:
    def __init__(self, nombre: str, ficha: str):
        self.nombre = nombre
        self.ficha = ficha

    def __str__(self):
        return f"{self.nombre} ({self.ficha})"