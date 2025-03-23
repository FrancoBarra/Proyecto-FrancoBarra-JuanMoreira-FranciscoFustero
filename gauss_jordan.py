import matriz 

class Gauss_Jordan():

    def __init__(self,  matrizA , soluciones): 
        self.matrizA = matrizA
        self.soluciones = soluciones # soluciones a las ecuaciones
        self.n = len(matrizA) # numero de ecuaciones
        self.x = [0]*self.n
        self.solve()

    def solve(self):
        matriz = self.matrizA
        b = self.soluciones
        
        print("Gauss Jordan")
        # Operaciones elementales
        for i in range(self.n):
            for j in range(self.n):
                
               
                if  matriz[i][i] == 0:
                    for x in range(self.n):
                        if matriz[x][i] != 0:
                            matriz[i], matriz[x] = matriz[x], matriz[i]
                            b[0][i], b[x] = b[0][x], b[0][i]
                            break
                        elif matriz[x][i] == 0 and x == self.n-1:
                            pass
                            

                if i != j:
                    if matriz[j][i] == 0:
                        continue

                    factor = float(matriz[j][i]/matriz[i][i])
                    for k in range(self.n):
                        matriz[j][k] -= float(factor*matriz[i][k])
                    b[0][j] -= float(factor)*float(b[0][i])
        
        print("Matriz escalonada")
        for i in range(self.n):
            print(matriz[i], b[0][i])

        existesolucion = True
        for i in range(self.n):
            if b[0][i] == 0 and matriz[i][i] == 0:
                print("El sistema tiene infinitas soluciones")
                existesolucion = False
                return 
                break
            elif matriz[i][i] == 0:
                print("El sistema no tiene solucion")
                existesolucion = False
                return 
                break

                
        # Sustitucion hacia atras
        if existesolucion == True:
            for i in range(self.n-1, -1, -1):
                self.x[i] = float(b[0][i]/matriz[i][i])
                for j in range(i-1, -1, -1):
                    b[0][j] -= float(matriz[j][i]*self.x[i])

        print("Soluciones:")
        for i in range(self.n):
            print("x"+str(i+1)+" =", self.x[i])
            

