from LU  import factorizacion_lu, resolver_sistema_lu
from Jacobi import Jacobi
import gauss_jordan


def menu(matriz1, b):
    print("====================================")
    print("menu")
    print("====================================")

    print("1. Gauss Jordan")    
     #GAUSS JORDAN       
    print("2. LU")
    print("3. Jacobi")
    print("4. Salir")
    opcion = input("=>")   
    if opcion == "1":
        print("Gauss Jordan")
        print("====================================")
        gauss_jordan.Gauss_Jordan(matriz1.matriz, b.matriz).x #imprimir la solucion del sistema de ecuaciones con la funcion gauss - jordan 
    elif opcion == "2":
        print("LU")
        print("================================")

        L, U = factorizacion_lu(matriz1.matriz)

        if L and U:
            print("Matriz L:")
            for fila in L:
                print(fila)
            print("\nMatriz U:")
            for fila in U:
                print(fila)

            x = resolver_sistema_lu(L, U, b.matriz)
            if x:
                print("\nVector solución x:", x)
            else:
                print("\nNo se pudo resolver el sistema.")
        else:
            print("La matriz no es factorizable.")
    elif opcion == "3":
        print("Jacobi")
        print("================================") 
        solver = Jacobi(matriz1.matriz, b.matriz)
        solucion = solver.solve()
        if solucion is not None:
            print(f"Solución:" , solucion)

        print("====================================")
    print("1. resolver otro sistema de ecuaciones")
    print("2.resolver otro sistema de ecuaciones con otro metodo")
    print("3. salir")
    print("=====================================")
    
    
    opcion = None
    while opcion != "1" and opcion != "2" and opcion != "3":  
        opcion = input("=>") 
        if opcion == "1":
            app()
        elif opcion == "2":
            menu(matriz1,b)
        elif opcion == "3":
            print("Adios")
            exit()
        

    
    

    
      