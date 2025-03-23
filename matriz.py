

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
                
                while True:
                    try:
                        self.matriz[i][j] = float(input(f"Valor de la fila {i+1} y columna {j+1}: "))
                        break
                    except ValueError:
                        print("Por favor ingrese un número válido.")
                        continue

    def imprimirMatriz(self):
        for i in range(self.filas):
            print(self.matriz[i])
        

