import numpy as np
from codigos_extra import obtener_primo,ListaSecuencial
#Aclaraciones: Mi lista secuencial esta inserta por contenido ( ordenada ) para usar busqueda binaria y ademas no admite valores repetidos todo esto dentro de la misma lista
class TablaHash:
    __tamaño : int
    __tabla : np.array
    def __init__(self,tamaño_tabla : int, tamaño_bucket : int):
        self.__tamaño = obtener_primo(round(tamaño_tabla/tamaño_bucket))
        self.__tabla = np.array([ListaSecuencial(tamaño_bucket) for _ in range(self.__tamaño)], dtype=ListaSecuencial)
    def hashing(self, valor:int):
        #Metodo de transformacion hay varios, este especificamente solo funciona para enteros
        return valor % self.__tamaño
    def insertar(self, valor:int):
        indice = self.hashing(valor)
        #Pregunto si el bucket esta lleno 
        if self.__tabla[indice].llena() != True: #si no esta lleno lo inserto en el area primaria 
            self.__tabla[indice].insertarPorContenido(valor)
    def busqueda(self, valor : int):
        indice = self.hashing(valor)
        encontrado = None
        #aqui llamamos a busqueda binaria que retorna true si lo encontrot o None si no lo encontro
        if self.__tabla[indice].busquedaBinaria(valor) != None: #si no lo encuentra en el bucket entonces lo busca en el overflow
            encontrado = True
        return encontrado

