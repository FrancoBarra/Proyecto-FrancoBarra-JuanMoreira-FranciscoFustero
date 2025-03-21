import numpy as np

class JacobiSolver:
    def __init__(self, A, b, x0=None, tol=1e-10, max_iter=1000):
        self.A = A
        self.b = b
        self.x0 = x0 if x0 is not None else np.zeros_like(b)
        self.tol = tol
        self.max_iter = max_iter

    def is_well_conditioned(self):
        cond_num = np.linalg.cond(self.A)
        print(f"Número de condición: {cond_num}")
        return cond_num < 1e10  # Umbral para bien condicionado

    def recondition_system(self):
        print("Redefiniendo el sistema para mejorar el condicionamiento...")
        self.A = self.A + np.eye(self.A.shape[0]) * 1e-5  # Regularización

    def solve(self):
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
print("Solución:", solucion)
