from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self, nombre_x="Jugador X", nombre_0="Jugador 0"):
        self.tablero = Tablero()
        self.jugadores = [Jugador(nombre_x, "X"), Jugador(nombre_0, "0")]
        self.jugador_actual = self.jugadores[0]
        self.estado = "EN_JUEGO"  # EN_JUEGO | GANADO | EMPATE
        self.ganador = None       # Jugador o None

    def ocupar_una_de_las_casillas(self, fil, col):
        if self.estado != "EN_JUEGO":
            raise Exception("El juego ya terminó.")
        # pongo la ficha...
        self.tablero.poner_la_ficha(fil, col, self.jugador_actual.ficha)
        # condicion para ganar
        if self.tablero.hay_ganador():
            self.estado = "GANADO"
            self.ganador = self.jugador_actual
            return
        # empate?
        if self.tablero.esta_lleno():
            self.estado = "EMPATE"
            return
        # cambia turno... va a suceder solo si se pudo poner la ficha
        if self.jugador_actual.ficha == "X":
            self.jugador_actual = self.jugadores[1]
        else:
            self.jugador_actual = self.jugadores[0]