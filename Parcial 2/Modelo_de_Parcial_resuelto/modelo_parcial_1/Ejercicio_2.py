import numpy as np
#A)
class TablaHash:
    __tamaño_tabla: int
    __tamaño_buckets : int
    __matriz : np.array
    __lista_contadores: int
    #como el tamaño de los buckets no me lo especifican me lo saco de los huevos
    def __init__(self,cantidad_claves= 800, tamaño_buckets = 4 ):
        self.__tamaño_area_primaria = primo(cantidad_claves / tamaño_buckets)
        self.__tamaño_buckets = tamaño_buckets
        self.__matriz = np.zeros((self.__tamaño_tabla * 1.2, self.__tamaño_buckets),dtype = int)
        self.__lista_contadores = [0] * self.__tamaño_tabla
#B)
    def hash(self,clave : int):
        return clave % self.__tamaño_tabla
#C)
    def insertar(self,valor : int):
        indice = self.hash(valor)
        disponible = self.__lista_contadores[indice]
        if disponible < self.__tamaño_buckets:
            self.__matriz[indice][disponible] = valor
            self.__lista_contadores[indice] += 1
        else:
            indice_overflow = self.__tamaño_area_primaria
            j = 0
            while indice_overflow < len(self.__matriz) and self.__matriz[indice_overflow][j] != 0:
                if j < self.__tamaño_buckets:
                    indice_overflow+=1
                    j = 0
            if indice_overflow < len(self.__matriz):
                self.__matriz[indice_overflow][j] = valor

