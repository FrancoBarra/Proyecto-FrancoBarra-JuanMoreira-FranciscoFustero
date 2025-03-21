import numpy as np

class Jacobi:
    def __init__(self, A, b, x0=None, tol=1e-10, max_iter=1000):
        self.A = A
        self.b = b
        self.x0 = x0 if x0 is not None else np.zeros_like(b)
        self.tol = tol
        self.max_iter = max_iter

    def is_diagonally_dominant(self): #Verifica si la matriz A es diagonalmente dominante.
        for i in range(self.A.shape[0]):
            if np.abs(self.A[i, i]) <= np.sum(np.abs(self.A[i, :])) - np.abs(self.A[i, i]):
                return False
        return True

    def is_well_conditioned(self): #Verifica si la matriz A está bien condicionada.
        cond_num = np.linalg.cond(self.A)
        print(f"Número de condición: {cond_num}")
        return cond_num < 1e10  # Umbral para bien condicionado

    def recondition_system(self): #Mejora el condicionamiento de la matriz A.
        print("Redefiniendo el sistema para mejorar el condicionamiento...")
        self.A = self.A + np.eye(self.A.shape[0]) * 1e-5  # Regularización

    def check_system(self):#Verifica si el sistema tiene solución y si es única.
        A_augmented = np.column_stack((self.A, self.b))
        rank_A = np.linalg.matrix_rank(self.A)
        rank_A_augmented = np.linalg.matrix_rank(A_augmented)

        if rank_A != rank_A_augmented:
            print("El sistema no tiene solución.")
            return False

        # Verificar unicidad de la solución
        n = self.A.shape[0]  # Número de incógnitas
        if rank_A == n:
            print("El sistema tiene una solución única.")
            return True
        else:
            print("El sistema tiene infinitas soluciones.")
            return True

    def solve(self): #Resuelve el sistema de ecuaciones lineales usando el método de Jacobi.
        if not self.check_system():
            return None

        if not self.is_diagonally_dominant():
            print("La matriz no es diagonalmente dominante. Usando descomposición LU...")
            return np.linalg.solve(self.A, self.b)

        if not self.is_well_conditioned():
            self.recondition_system()

        D = np.diag(np.diag(self.A))
        LU = self.A - D
        x = self.x0
        for i in range(self.max_iter):
            x_new = np.linalg.inv(D) @ (self.b - LU @ x)
            if np.linalg.norm(x_new - x) < self.tol:
                print(f"Convergencia alcanzada en {i + 1} iteraciones.")
                return x_new
            x = x_new
        print("Máximo de iteraciones alcanzado.")
        return x

# Ejemplo de uso
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
b = np.array([1, 2, 3])

solver = JacobiSolver(A, b)
solucion = solver.solve()
if solucion is not None:
    print("Solución:", solucion)
