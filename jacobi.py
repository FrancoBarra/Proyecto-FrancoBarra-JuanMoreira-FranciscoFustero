def solve_jacobi(A, b, x0=None, tol=1e-10, max_iter=1000, cond_tol=1e10):
    n = len(b)
    if x0 is None:
        x0 = [0.0 for _ in range(n)]  # Condición inicial clásica (0, ..., 0)
    
    def norma(matrix): # Función para calcular la norma infinita de una matriz
        suma_max = 0
        for r in matrix:
            row_sum = sum(abs(x) for x in r)
            if row_sum > suma_max:
                suma_max = row_sum
        return suma_max
    
    def bien_condicionado(A): # Función para verificar si el sistema está bien condicionado
        norm_A = norma(A)  # Calcular la norma infinita de A
        try: # Calcular la norma infinita de la inversa de A (aproximada)
            inv_A = invertir(A)
            norm_inv_A = norma(inv_A)
            condicion = norm_A * norm_inv_A
            print("Número de condición de la matriz A:", condicion)
            return condicion < cond_tol
        except:
            print("La matriz es singular o no se puede invertir.")
            return False
    
    
    def invertir(A):# Función para invertir una matriz usando eliminación gaussiana
        n = len(A)
        identidad = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        argumento = [row + identidad[i] for i, row in enumerate(A)]
        
        for i in range(n):# Pivoteo parcial
            max_row = i
            for r in range(i, n):
                if abs(argumento
                       [r][i]) > abs(argumento[max_row][i]):
                    max_row = r
            argumento[i], argumento[max_row] = argumento[max_row], argumento[i]
            
            pivot = argumento[i][i]
            if abs(pivot) < 1e-10:
                raise ValueError("La matriz es singular y no se puede invertir.")
            for j in range(2 * n):# Normalizar la fila del pivote
                argumento[i][j] /= pivot
            for j in range(n):# Eliminación hacia adelante
                if j != i:
                    factor = argumento[j][i]
                    for k in range(2 * n):
                        argumento[j][k] -= factor * argumento[i][k]
        
        inv_A = [row[n:] for row in argumento] # Extraer la inversa
        return inv_A
    
    def redefinir_sistema(A, b): # Función para redefinir el sistema (precondicionador simple: escalado diagonal)
        D = [A[i][i] for i in range(n)]
        D_inv = [1.0 / D[i] if D[i] != 0 else 1.0 for i in range(n)]
        A_nuevo = [[D_inv[i] * A[i][j] for j in range(n)] for i in range(n)]
        b_nuevo = [D_inv[i] * b[i] for i in range(n)]
        return A_nuevo, b_nuevo
    
    def jacobi(A, b, x0, tol, max_iter): # Método de Jacobi
        x = x0.copy()
        x_nuevo = [0.0 for _ in range(n)]
        for iteracion in range(max_iter):
            for i in range(n):
                sigma = 0
                for j in range(n):
                    if j != i:
                        sigma += A[i][j] * x[j]
                x_nuevo[i] = (b[i] - sigma) / A[i][i]
            
            converge = True # Verificar convergencia
            for i in range(n):
                if abs(x_nuevo[i] - x[i]) >= tol:
                    converged = False
                    break
            
            if converge:
                return x_nuevo, iteracion + 1
            
            x = x_nuevo.copy()
        
        raise ValueError("El método de Jacobi no convergió después de {} iteraciones".format(max_iter))
    
  
    if not bien_condicionado(A):  # Verificar si el sistema está bien condicionado
        print("El sistema está mal condicionado. Redefiniendo el sistema...")
        A, b = redefinir_sistema(A, b)
   
    print("Resolviendo el sistema con el método de Jacobi...") # Resolver el sistema con el método de Jacobi
    x, iterations = jacobi(A, b, x0, tol, max_iter)
    print("Solución encontrada en {} iteraciones:".format(iterations))
    print("Solución:", x)
    return x

# Ejemplo de uso
A = [
    [4, 1, 2],
    [3, 5, 1],
    [1, 1, 3]
]

b = [4, 7, 3]

# Llamada a la función
solve_jacobi(A, b)