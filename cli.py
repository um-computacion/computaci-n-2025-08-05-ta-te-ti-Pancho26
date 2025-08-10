from tateti import Tateti

def mostrar_tablero(tablero):
    print("  1   2   3")
    for i, fila in enumerate(tablero.contenedor):
        print(f"{i + 1} {fila[0] or ' '} | {fila[1] or ' '} | {fila[2] or ' '}")
        if i < 2:
            print(" ---|---|---")

def main():
    print("Bienvenidos al Tateti")
    nombre_x = input("Nombre para jugador 1: ").strip() or "Jugador X"
    nombre_0 = input("Nombre para jugador 2: ").strip() or "Jugador 0"
    juego = Tateti(nombre_x, nombre_0)
    while True:
        print("\nTablero:")
        mostrar_tablero(juego.tablero)
        print("Turno:", f"{juego.jugador_actual.nombre} -> {juego.jugador_actual.ficha}")
        try:
            fil = int(input("Ingrese fila (1-3): ")) - 1
            col = int(input("Ingrese columna (1-3): ")) - 1
            if not (0 <= fil < 3 and 0 <= col < 3):
                print("Fila y columna deben estar entre 1 y 3.")
                continue
            juego.ocupar_una_de_las_casillas(fil, col)
            if juego.estado == "GANADO":
                print("\nTablero final:")
                mostrar_tablero(juego.tablero)
                print(f"¡Ganó {juego.ganador.nombre} con {juego.ganador.ficha}!")
                break
            if juego.estado == "EMPATE":
                print("\nTablero final:")
                mostrar_tablero(juego.tablero)
                print("¡Empate!")
                break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()