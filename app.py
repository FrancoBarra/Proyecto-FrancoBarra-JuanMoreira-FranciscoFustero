import gauss_jordan
import matriz
from menu import menu







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
    menu(matriz1,b)


app()
