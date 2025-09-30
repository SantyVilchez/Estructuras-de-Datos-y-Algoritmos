import numpy as np
from random import randint
class ListaSecuencial:
    __arrego : np.array
    __filas : int
    __columnas : int
    def __init__(self,filas : int, columnas : int):
        self.__arrego = np.zeros((filas,columnas),dtype = int)
        self.__filas = filas
        self.__columnas = columnas
    def cargaRandom(self):
        for i in range(self.__filas):
            for j in range(self.__columnas):
                self.__arrego[i][j] = randint(1,9)
    def elementos(self):
        return self.__arrego
    def filas(self):
        return self.__filas
    def columnas(self):
        return self.__columnas
def suma(lista_1 : ListaSecuencial, lista_2 : ListaSecuencial):
    aux = np.zeros((lista_1.filas(),lista_1.columnas()),dtype = int)
    for i in range(lista_1.filas()):
        for j in range(lista_1.columnas()):
            aux[i][j] = lista_1.elementos()[i][j] + lista_2.elementos()[i][j]
    print(aux)
lista_1 = ListaSecuencial(100,100)
lista_2 = ListaSecuencial(100,100)
lista_1.cargaRandom()
lista_2.cargaRandom()
print("Lista 1")
print(lista_1.elementos())
print("Lista 2")
print(lista_2.elementos())
print("Lista 1 y 2 sumadas")
suma(lista_1,lista_2)
