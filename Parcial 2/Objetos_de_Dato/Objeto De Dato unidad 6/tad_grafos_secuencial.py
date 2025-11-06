#Para ambos grafos el objeto de dato es igual

import numpy as np
from codigo_extra import Cola,PilaEncadenada
class Grafo:
    __tamaño : int
    __matriz : np.array
    def __init__(self, vertices : int):
        self.__tamaño = vertices
        self.__matriz = np.zeros((tamaño,tamaño),dtype=int)
