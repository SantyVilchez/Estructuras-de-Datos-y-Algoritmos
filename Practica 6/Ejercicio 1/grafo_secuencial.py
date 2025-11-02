import numpy as np
from codigo_extra import Cola,PilaEncadenada
class Grafo:
    __tamaño : int
    __matriz : np.array
    def __init__(self, tamaño : int):
        self.__tamaño = tamaño
        self.__matriz = np.zeros((tamaño,tamaño),dtype=int)
        self.__vertices = "ABCD"
    #PUEDE IR AL PARCIAL
    def insertar(self, vertice_inicial : str, vertice_final : str):
        inicial_indice = self.__vertices.index(vertice_inicial)
        final_indice = self.__vertices.index(vertice_final)
        if self.__matriz[inicial_indice][final_indice] == 0:
            self.__matriz[inicial_indice][final_indice] = 1
            self.__matriz[final_indice][inicial_indice] = 1
    def suprimir(self, vertice_inicial : str, vertice_final : str):
        inicial_indice = self.__vertices.index(vertice_inicial)
        final_indice = self.__vertices.index(vertice_final)
        if self.__matriz[inicial_indice][final_indice] == 1:
            self.__matriz[inicial_indice][final_indice] = 0
            self.__matriz[final_indice][inicial_indice] = 0
    def mostrar(self):
        print(self.__matriz)
    #PUEDE IR AL PARCIAL
    def adyacentes(self, vertice : str):
        vertice_indice = self.__vertices.index(vertice)
        adyacentes = []
        for i in range(self.__tamaño):
            if self.__matriz[vertice_indice][i] == 1:
                adyacentes.append(self.__vertices[i])
        return adyacentes
    #PUEDE IR AL PARCIAL
    def BEA(self, vertice : str):
        cola = Cola()
        vertice_indice = self.__vertices.index(vertice)
        visitados = [float('inf')] * self.__tamaño
        visitados[vertice_indice] = 0
        cola.insertar(vertice)
        print(vertice)
        while not cola.vacia():
            actual = cola.suprimir()
            actual_idx = self.__vertices.index(actual)
            vecinos = ""
            for vecino in self.adyacentes(actual):
                vecino_idx = self.__vertices.index(vecino)
                if visitados[vecino_idx] == float('inf'):
                    visitados[vecino_idx] = visitados[actual_idx] + 1
                    cola.insertar(vecino)
                    vecinos += vecino +  " "
            if vecinos != "" : print(vecinos)
    def camino(self, vertice_inicial : str, vertice_final : str):
        cola = Cola()
        vertice_indice = self.__vertices.index(vertice_inicial)
        visitados = [float('inf')] * self.__tamaño
        predecesores = [None] * self.__tamaño  # Para reconstruir caminos
        visitados[vertice_indice] = 0
        cola.insertar(vertice_inicial)
        while not cola.vacia():
            actual = cola.suprimir()
            actual_idx = self.__vertices.index(actual)
            for vecino in self.adyacentes(actual):
                vecino_idx = self.__vertices.index(vecino)
                if visitados[vecino_idx] == float('inf'):
                    visitados[vecino_idx] = visitados[actual_idx] + 1
                    cola.insertar(vecino)
                    predecesores[vecino_idx] = actual
        camino = PilaEncadenada()
        actual = vertice_final
        if predecesores[self.__vertices.index(actual)] != None:
            while actual is not None:
                camino.insertar(actual)
                actual = predecesores[self.__vertices.index(actual)]
            while camino.vacia()!=True:
                print(camino.tope())
                camino.suprimir()
        else:
            print(f"No existe un camino desde {vertice_inicial} a {vertice_final}")




    #PUEDE IR AL PARCIAL
    def BEP_visita(self, v_idx, d, f, tiempo):
        tiempo[0] += 1
        d[v_idx] = tiempo[0]
        for u in range(self.__tamaño):
            if self.__matriz[v_idx][u] == 1 and d[u] == 0:
                self.BEP_visita(u, d, f, tiempo)
        tiempo[0] += 1
        f[v_idx] = tiempo[0]


    def BEP(self, vertice: str):
        d = [0] * self.__tamaño
        f = [0] * self.__tamaño
        tiempo = [0]
        vertice_idx = self.__vertices.index(vertice)
        if d[vertice_idx] == 0:
            self.BEP_visita(vertice_idx, d, f, tiempo)

        for i in range(self.__tamaño):
            print(f"{self.__vertices[i]}: d = {d[i]}, f = {f[i]}")
        return d, f

    def es_conexo(self):
        d, _ = self.BEP(self.__vertices[0])  # Empezamos desde el primer vértice
        return all(valor != 0 for valor in d)
    def es_aciclico(self):
        _, _, clasificacion = self.BEP_clasificacion(self.__vertices[0])
        return all(tipo != "arista hacia atrás" for _, _, tipo in clasificacion)
    def BEP_clasificacion(self, s: str):
        d = [0] * self.__tamaño
        f = [0] * self.__tamaño
        tiempo = [0]
        clasificacion = []
        s_idx = self.__vertices.index(s)
        if d[s_idx] == 0:
            self.BEP_visita_clasificacion(s_idx, d, f, tiempo, clasificacion)
        return d, f, clasificacion
    def BEP_visita_clasificacion(self, v_idx, d, f, tiempo, clasificacion):
        tiempo[0] += 1
        d[v_idx] = tiempo[0]
        for u in range(self.__tamaño):
            if self.__matriz[v_idx][u] == 1:
                if d[u] == 0:
                    clasificacion.append((self.__vertices[v_idx], self.__vertices[u], "arista de árbol"))
                    self.BEP_visita_clasificacion(u, d, f, tiempo, clasificacion)
                elif f[u] == 0:
                    clasificacion.append((self.__vertices[v_idx], self.__vertices[u], "arista hacia atrás"))
        tiempo[0] += 1
        f[v_idx] = tiempo[0]

     
grafo = Grafo(4)
grafo.insertar("A","B")
grafo.insertar("A","C")
grafo.insertar("B","D")
grafo.insertar("C","B")

print(grafo.es_conexo())
print(grafo.es_aciclico())