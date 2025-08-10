import unittest
from tateti import Tateti
from tablero import PosOcupadaException, PosFueraException

class TestTatetiBasico(unittest.TestCase):
    def test_gana_fila(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        juego.ocupar_una_de_las_casillas(1, 0)  # 0
        juego.ocupar_una_de_las_casillas(0, 1)  # X
        juego.ocupar_una_de_las_casillas(1, 1)  # 0
        juego.ocupar_una_de_las_casillas(0, 2)  # X gana
        self.assertEqual(juego.estado, "GANADO")
        self.assertIsNotNone(juego.ganador)
        self.assertEqual(juego.ganador.ficha, "X")

    def test_empate(self):
        juego = Tateti()
        # Secuencia que llena el tablero sin ganador
        jugadas = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2),
        ]
        for fil, col in jugadas:
            juego.ocupar_una_de_las_casillas(fil, col)
        self.assertEqual(juego.estado, "EMPATE")

    def test_posicion_ocupada(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)  # X ocupa (0,0)
        with self.assertRaises(PosOcupadaException):
            juego.ocupar_una_de_las_casillas(0, 0)  # intento sobre misma casilla

    def test_pos_fuera_de_rango(self):
        juego = Tateti()
        with self.assertRaises(PosFueraException):
            juego.ocupar_una_de_las_casillas(-1, 0)
        with self.assertRaises(PosFueraException):
            juego.ocupar_una_de_las_casillas(3, 2)

    def test_no_puede_jugar_despues_de_terminar(self):
        juego = Tateti()
        # Hacer ganar a X rápido
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        juego.ocupar_una_de_las_casillas(1, 0)  # 0
        juego.ocupar_una_de_las_casillas(0, 1)  # X
        juego.ocupar_una_de_las_casillas(1, 1)  # 0
        juego.ocupar_una_de_las_casillas(0, 2)  # X gana
        self.assertEqual(juego.estado, "GANADO")
        with self.assertRaises(Exception):
            juego.ocupar_una_de_las_casillas(2, 2)  # no debería permitir otra jugada

if __name__ == "__main__":
    unittest.main()
