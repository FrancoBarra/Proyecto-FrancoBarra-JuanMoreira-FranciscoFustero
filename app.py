
from Jacobi import Jacobi
from LU import factorizacion_lu, resolver_sistema_lu
import gauss_jordan
import matriz
import numpy as np




def menu(matriz1,b): #llamar a la funcion menu con las matrices creadas
    
    print("====================================")
    print("menu")
    print("====================================")

    print("1. Gauss Jordan")         
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

        bLista = b.matriz[0]

        if L and U:
            print("Matriz L:")
            for fila in L:
                print(fila)
            print("\nMatriz U:")
            for fila in U:
                print(fila)
            

            x = resolver_sistema_lu(L, U, bLista)
            if x:
                print("\nVector solución x:", x)
            else:
                print("\nNo se pudo resolver el sistema.")
        else:
            print("La matriz no es factorizable.")
    elif opcion == "3":
        print("Jacobi")
        print("================================") 
        bArray = np.array(b.matriz[0])
        matrizArray = np.array(matriz1.matriz)
        solver = Jacobi(matrizArray, bArray)
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
        



def app():
    print("====================================")
    print("Sistema de ecuaciones lineales") 
    print("====================================")
    filas = (input("ingrese el numero de filas\n=>"))      #ingresar filas y columnas  
    while filas.isnumeric() == False: #verificar que sea un numero entero y mayor a 0
        print("Introduce un número entero")
        filas = input("ingrese el numero de filas\n=>")
    filasInt = int(filas) #convertir a entero       
    columnas = filasInt #como la matriz es cuadrada, las columnas son iguales a las filas
    matriz1 = matriz.Matriz(filasInt,columnas) #crear matriz vacia 
    b = matriz.Matriz(1,filasInt) #crear matriz soluciones vacia
    matriz1.anadir_valores() #agregar los valores de la matriz
    matriz1.imprimirMatriz() #imprimir la matriz para verificar 
    b.anadir_valores() #agregar los valores de la matriz soluciones 
    print(f"Matriz b= {b.matriz}") #imprimir la matriz soluciones para verificar
    menu(matriz1,b) #llamar a la funcion menu con las matrices
    
app() 









