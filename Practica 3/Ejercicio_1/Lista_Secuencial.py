#EN ESTE EJERCICIO CONSIDERO AL NUMERO 0 COMO VALOR NULO
import numpy as np
class ListaSecuencial:
    __cant : int
    __maximo : int
    __arrego : np.ndarray
    def __init__(self,maximo : int):
        self.__maximo = maximo
        self.__cant = 0
        self.__arreglo = np.zeros(maximo,dtype=int)
    def vacia(self):
        return self.__cant == 0
    def llena(self):
        return self.__cant == self.__maximo
    def insertar(self,elemento : int):
        if not self.llena():
            self.__arreglo[self.__cant] = elemento
            self.__cant += 1
        else :
            print("Se lleno la lista")
    def insertarPorPosicion(self,posicion:int,elemento : int):
        if not self.llena():
            if 0 <= posicion <= self.__cant:
                if self.__arreglo[posicion]:
                    for x in range(self.__cant,posicion,-1):
                        self.__arreglo[x] = self.__arreglo[x-1]
                self.__arreglo[posicion] = elemento
                self.__cant +=1
            else:
                print("La posicion esta fuera del rango del arreglo")
        else:
            print(f"La lista se lleno por lo que el elemento {elemento} no pudo ser insertado")

    def suprimir(self,posicion:int):
        if 0 <= posicion <= self.__cant:
            for x in range(self.__cant - posicion):
                self.__arreglo[posicion] = self.__arreglo[posicion+1]
                posicion += 1
            self.__cant -=1
        else:
            print("El indice esta fuera de rango")
    def buscar(self,elemento : int):
        i =0
        while elemento != self.__arreglo[i] and i < self.__cant:
            i+=1
        return i+1
    def recuperar(self,posicion : int):
        if 0 <= posicion <= self.__cant:
            if self.__arreglo[posicion]:
                elemento = self.__arreglo[posicion]
            else:
                elemento = 0
        else:
            print("Poisicion fuera de rango")
        return elemento        
    def recorrer(self):
        for indice in range(self.__cant):
            print(self.__arreglo[indice])
    def primerElemento(self):
        return self.__arreglo[0]
    def ultimoElemento(self):
        return self.__arreglo[self.__cant-1]
    


