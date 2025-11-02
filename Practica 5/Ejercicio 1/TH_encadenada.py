import numpy as np
from codigos_extra import obtener_primo,ListaEnlazada

class TablaHash:
    __tamaño : int
    __tabla : np.array
    def __init__(self,claves_a_almacenar : int, colisiones_esperadas : int):
        self.__tamaño = obtener_primo(round(claves_a_almacenar/colisiones_esperadas))
        self.__tabla = np.array([ListaEnlazada() for _ in range(self.__tamaño)], dtype=ListaEnlazada)
    def hashing(self, valor:int):
        #Metodo de transformacion hay varios, este especificamente solo funciona para enteros
        return valor % self.__tamaño
    def insertar(self, valor:int):
        indice = self.hashing(valor)

        self.__tabla[indice].insertar(valor)
    def busqueda(self, valor : int):
        indice = self.hashing(valor)
        nodo = self.__tabla[indice].obtener_cabeza()
        while nodo != None and nodo.getElem() != valor:
            nodo = nodo.getSig()
        return nodo
    def mostrar(self):
        #Este metodo es solo para debug no es oficial de la estructura, te muestra la lista entera de cada posicion del array
        print(self.__tabla)
        for x in self.__tabla:
            print(x)
