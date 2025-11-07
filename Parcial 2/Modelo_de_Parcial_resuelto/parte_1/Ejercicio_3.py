#A)
class Digrafo:
    __vertices:int
    __matriz_adyacencia:np.array
    def __init__(self, numero_de_vertices : int):
        self.__vertices = numero_de_vertices
        self.__matriz_adyacencia = np.zeros((self.__vertices,self.__vertices),dtype = int)
#B)
    def grado_entrada(self,vertice : int):
        grado = 0
        for i in range(self.__vertices):
            if self.__matriz_adyacencia[i][vertice] == 1:
                grado += 1
        return grado
    def grado_salida(self,vertice: int):
        grado = 0
        for i in self.__vertices:
            if self.__matriz_adyacencia[vertice][i] == 1:
                grado += 1
        return grado
    def todo_nodos_sumideros(self):
        vertices_sumideros= []
        for i in range(self.__vertices):
            if self.grado_salida == 0 and self.grado_entrada > 0:
                vertices_sumideros.append(i)
        return vertices_sumideros