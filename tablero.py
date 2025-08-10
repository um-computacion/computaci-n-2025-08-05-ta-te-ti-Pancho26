class PosOcupadaException(Exception):
    ...
class PosFueraException(Exception):
    ...

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        # validar rango simple
        if not (0 <= fil < 3 and 0 <= col < 3):
            raise PosFueraException("Fila y columna deben estar entre 1 y 3.")
        # ver si está ocupado
        if self.contenedor[fil][col] != "":
            raise PosOcupadaException("Posición ocupada!")
        self.contenedor[fil][col] = ficha

    def hay_ganador(self):
        tablero = self.contenedor
        # filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] != "":
                return fila[0]
        # columnas
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] != "":
                return tablero[0][col]
        # diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
            return tablero[0][2]
        return None

    def esta_lleno(self):
        return all(celda != "" for fila in self.contenedor for celda in fila)
