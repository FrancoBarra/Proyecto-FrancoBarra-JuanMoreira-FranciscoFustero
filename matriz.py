

class Matriz():

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        for i in range(filas):
            self.matriz.append([0]*columnas)

    def anadir_valores(self):

        for i in range(self.filas):
            for j in range(self.columnas):
                try:
                
                    self.matriz[i][j] = float(input(f"Introduce el valor de la fila {i+1} y columna {j+1}: "))

                except ValueError:
                    print("Introduce un número entero") 
                    self.matriz[i][j] = float(input(f"Introduce el valor de la fila {i+1} y columna {j+1}: "))


