

class Gauss_Jordan():

    def __init__(self, matriz, b):
        self.matriz = matriz
        self.b = b # soluciones a las ecuaciones
        self.n = len(matriz) # numero de ecuaciones
        self.x = [0]*self.n
        self.solve()

    def solve(self):
        print("Gauss Jordan")
        # Operaciones elementales
        for i in range(self.n):
            for j in range(self.n):
                
               
                if  self.matriz[i][i] == 0:
                    for x in range(self.n):
                        if self.matriz[x][i] != 0:
                            self.matriz[i], self.matriz[x] = self.matriz[x], self.matriz[i]
                            self.b[i], self.b[x] = self.b[x], self.b[i]
                            break
                        elif self.matriz[x][i] == 0 and x == self.n-1:
                            print("No se puede resolver el sistema de ecuaciones")
                            

                if i != j:
                    factor = float(self.matriz[j][i]/self.matriz[i][i])
                    for k in range(self.n):
                        self.matriz[j][k] -= float(factor*self.matriz[i][k])
                    self.b[j][0] -= float(factor)*float(self.b[i][0])
                    print(f"Matriz: {self.matriz}")
        # Sustitucion hacia atras
        for i in range(self.n-1, -1, -1):
            self.x[i] = float(self.b[i][0]/self.matriz[i][i])
            for j in range(i-1, -1, -1):
                self.b[j][0] -= float(self.matriz[j][i]*self.x[i])

        
