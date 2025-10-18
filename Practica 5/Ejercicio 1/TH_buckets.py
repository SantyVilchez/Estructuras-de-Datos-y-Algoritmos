import numpy as np
from codigos_extra import obtener_primo
#Aclaraciones: Mi lista secuencial esta inserta por contenido ( ordenada ) para usar busqueda binaria y ademas no admite valores repetidos todo esto dentro de la misma lista
class TablaHash:
    __tamaño_tabla : int
    __tamaño_buckets : int
    __tabla : np.array
    def __init__(self,tamaño_tabla : int, tamaño_buckets : int):
        self.__tamaño_tabla = obtener_primo(round(tamaño_tabla/tamaño_buckets))
        self.__tamaño_buckets = tamaño_buckets
        self.__tabla = np.zeros( (round(self.__tamaño_tabla * 1.2) , self.__tamaño_buckets) , dtype=int)
        self.__tabla_contadora = np.zeros(self.__tamaño_tabla,dtype=int)
    def hashing(self, valor:int):
        #Metodo de transformacion hay varios, este especificamente solo funciona para enteros
        return valor % self.__tamaño_tabla
    def insertar(self, valor:int):
        indice = self.hashing(valor)
        indice_bucket = self.__tabla_contadora[indice]
        if indice_bucket < self.__tamaño_buckets:
            self.__tabla[indice][indice_bucket] = valor
            self.__tabla_contadora[indice] += 1
        else:
            indice_overflow = self.__tamaño_tabla 
            indice_bucket = 0
            while indice_overflow < len(self.__tabla) and self.__tabla[indice_overflow][indice_bucket] != 0:
                indice_bucket+=1
                if indice_bucket < self.__tamaño_buckets:
                    indice_overflow += 1
                    indice_bucket = 0
            if indice < len(self.__tabla):
                self.__tabla[indice_overflow][indice_bucket] = valor
    def buscar(self,valor : int):
        indice = self.hashing(valor)
        indice_buckets = 0
        buscado = 0
        while indice_buckets < self.__tamaño_buckets and self.__tabla[indice][indice_buckets] != valor:
            indice_buckets += 1
        if indice_buckets < self.__tamaño_buckets:
            buscado = self.__tabla[indice][indice_buckets]
        elif self.__tabla_contadora[indice] != indice_buckets:
            indice_overflow = self.__tamaño_tabla 
            indice_buckets = 0
            while indice_overflow < len(self.__tabla) and self.__tabla[indice_overflow][indice_buckets] != valor:
                indice_buckets+=1
                if indice_buckets < self.__tamaño_buckets:
                    indice_overflow += 1
                    indice_buckets = 0
            if indice < len(self.__tabla):
               buscado = self.__tabla[indice][indice_buckets]
        return buscado
    def mostrar(self):
        print(self.__tabla)
        print(self.__tabla_contadora)
if __name__=="__main__":
    tabla = TablaHash(10,2)
    tabla.insertar(44526532)
    tabla.insertar(46726832)
    tabla.insertar(20533432)
    tabla.mostrar()
    print(tabla.buscar(46726832))