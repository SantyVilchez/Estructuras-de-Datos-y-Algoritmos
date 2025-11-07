#A)
class Grafo:
    __tamaño : int
    __matriz : np.array

    def __init__(self, vertices : int):
        self.__tamaño = vertices
        self.__matriz = np.zeros((tamaño,tamaño),dtype=int)
#B)
    def insertar(self,vertice_inicial : int , vertice_final : int):
        if  self.__matriz[vertice_inicial][vertice_final]==0:
            self.__matriz[vertice_inicial][vertice_final]= 1