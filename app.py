import gauss_jordan
import matriz







def app():
    filas = int(input("ingrese el numero de filas\n=>"))      #ingresar filas y columnas
    columnas = int(input("ingrese el numero de columnas \n=>")) #ingeresar filas y columnas
    matriz1 = matriz.Matriz(filas,columnas) #crear matriz vacia 
    b = matriz.Matriz(filas,1) #crear matriz soluciones vacia
    matriz1.anadir_valores() #agregar los valores de la matriz
    print(f"Matriz 1= {matriz1.matriz}") #imprimir la matriz para verificar 
    b.anadir_valores() #agregar los valores de la matriz soluciones 
    print(f"Matriz b= {b.matriz}") #imprimir la matriz soluciones para verificar
    print(gauss_jordan.Gauss_Jordan(matriz1.matriz, b.matriz).x) #imprimir la solucion del sistema de ecuaciones
    


app()
