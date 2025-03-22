def factorizacion_lu(matriz):
 
    filas = len(matriz)
    columnas = len(matriz[0])

    if filas != columnas or filas != 3:
        return None, None  

    #Creacion inicial de matrices
   
    u =[]
    l=[]
    for fila in matriz:
        listaf=[]
        for num in fila:
            listaf.append(num)
        u.append(listaf)


    for fila in range(filas):
        listas=[0.0]*columnas
        l.append(listas)
        
        

    for i in range(filas):
        l[i][i] = 1.0

    # Gauss-Jordan
    # i sera el pivote
    for i in range(filas - 1):
        # j sera la fila a modificar
        for j in range(i + 1, filas):
            #siendo u[j][i] el numero a convertir en 0 y u[i][i] el pivote, se obtiene el factor para multicar el pivote y restar al numero
            factor = u[j][i] / u[i][i]
            # Aca se agrega el factor a l ya que sera el valor debajo de la diagonal
            l[j][i] = factor
            for k in range(i, columnas):
                #se actualiza la fila modificada
                u[j][k] -= factor * u[i][k]

    return l, u

def resolver_sistema_lu(L, U, b):

    filas = len(L)
    y = [0.0] * filas
    x = [0.0] * filas

    for i in range(filas):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]


    for i in range(filas - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, filas):
            x[i] -= U[i][j] * x[j]
        if U[i][i] == 0:
            return None  
        x[i] /= U[i][i]

    return x
def obtener_pa(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])


  

    P = [[0.0] * filas for _ in range(filas)]
    for i in range(filas):
        P[i][i] = 1.0

    A = [fila[:] for fila in matriz]
    for i in range(filas):

        pivote_max = abs(A[i][i])
        fila_max = i
        for k in range(i + 1, filas):
            if abs(A[k][i]) > pivote_max:
                pivote_max = abs(A[k][i])
                fila_max = k

        if fila_max != i:
            A[i], A[fila_max] = A[fila_max], A[i]
            P[i], P[fila_max] = P[fila_max], P[i]
        if A[i][i] == 0:
            return None

    PA = [[0.0] * columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            for k in range(filas):
                PA[i][j] += P[i][k] * matriz[k][j]
    return PA
  
def comprobar_matriz_factorizable(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    if filas != columnas or filas > 4:
        print("La matriz debe ser cuadrada y de tamaño 2x2, 3x3 o 4x4.")
        return None  


    determinante = 0
    if filas == 2:
        determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif filas == 3:
        determinante = (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) -
                        matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) +
                        matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))
    elif filas == 4:
        determinante = (matriz[0][0] * (matriz[1][1] * (matriz[2][2] * matriz[3][3] - matriz[2][3] * matriz[3][2]) -
                                        matriz[1][2] * (matriz[2][1] * matriz[3][3] - matriz[2][3] * matriz[3][1]) +
                                        matriz[1][3] * (matriz[2][1] * matriz[3][2] - matriz[2][2] * matriz[3][1])) -
                        matriz[0][1] * (matriz[1][0] * (matriz[2][2] * matriz[3][3] - matriz[2][3] * matriz[3][2]) -
                                        matriz[1][2] * (matriz[2][0] * matriz[3][3] - matriz[2][3] * matriz[3][0]) +
                                        matriz[1][3] * (matriz[2][0] * matriz[3][2] - matriz[2][2] * matriz[3][0])) +
                        matriz[0][2] * (matriz[1][0] * (matriz[2][1] * matriz[3][3] - matriz[2][3] * matriz[3][1]) -
                                        matriz[1][1] * (matriz[2][0] * matriz[3][3] - matriz[2][3] * matriz[3][0]) +
                                        matriz[1][3] * (matriz[2][0] * matriz[3][1] - matriz[2][1] * matriz[3][0])) -
                        matriz[0][3] * (matriz[1][0] * (matriz[2][1] * matriz[3][2] - matriz[2][2] * matriz[3][1]) -
                                        matriz[1][1] * (matriz[2][0] * matriz[3][2] - matriz[2][2] * matriz[3][0]) +
                                        matriz[1][2] * (matriz[2][0] * matriz[3][1] - matriz[2][1] * matriz[3][0])))

    return determinante


A = [[2, 1, 1],
     [4, 1, 0],
     [-2, 2, 1]]

b = [4, 1, 2]

L, U = factorizacion_lu(A)

if L and U:
    print("Matriz L:")
    for fila in L:
        print(fila)
    print("\nMatriz U:")
    for fila in U:
        print(fila)

    x = resolver_sistema_lu(L, U, b)
    if x:
        print("\nVector solución x:", x)
    else:
        print("\nNo se pudo resolver el sistema.")
else:
    print("La matriz no es factorizable.")
