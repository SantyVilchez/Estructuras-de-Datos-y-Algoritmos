#A
class Grafo:
    __tamaño : int
    __matriz : np.array
    def __init__(self, vertices : int):
        self.__tamaño = vertices
        self.__matriz = np.zeros((tamaño,tamaño),dtype=int)

#B
    def adyacentes(self, vertice : str):
        adyacentes = []
        for i in range(self.__tamaño):
            if self.__matriz[vertice_indice][i] == 1:
                adyacentes.append(i)
        return adyacentes