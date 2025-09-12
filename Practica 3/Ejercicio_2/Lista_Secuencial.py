#EN ESTE EJERCICIO CONSIDERO AL NUMERO 0 COMO VALOR NULO
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
    def insertarPorContenido(self,elemento : int):
        if not self.llena():
            if not self.vacia():
                indice = 0
                while self.__arreglo[indice] < elemento and self.__arreglo[indice]!= 0:
                    indice += 1
                for x in range(self.__cant,indice,-1):
                    self.__arreglo[x] = self.__arreglo[x-1]
                self.__arreglo[indice]= elemento
            else:
                self.__arreglo[0] = elemento   
            self.__cant += 1
        else:
            print(f"La lista esta llena el elemento {elemento} no pudo ser insertado")
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
        cant = 0
        x=0
        while cant != self.__cant:
            print(self.__arreglo[x])
            cant+=1 
            x+=1
    def primerElemento(self):
        return self.__arreglo[0]
    def ultimoElemento(self):
        return self.__arreglo[self.__cant-1]
    
