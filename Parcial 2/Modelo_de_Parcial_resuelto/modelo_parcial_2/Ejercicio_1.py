#A)
class Arbol:
    __raiz : Nodo
    def __init__(self):
        self.__raiz = None
#B)
    #si no te especifican implementar el nivel directamente llamalo

    # def nivel(self, nodo : Nodo, valor : int,nivel : int):
    #     if nodo == None:
    #         nivel = 0
    #     elif valor < nodo.getValor():
    #         nivel += 1
    #         nivel = self.nivel(nodo.getIzq(),valor,nivel)
    #     elif valor > nodo.getValor():
    #         nivel += 1
    #         nivel = self.nivel(nodo.getDer(),valor,nivel)
    #     else:
    #         nivel+=1
    #     return nivel
    
    def Mostrar_Nodos_En_Nivel_N(self,nodo : Nodo , N : int):
        if nodo:
            if self.nivel(nodo,0) == N:
                print(nodo.getDato())
            self.Mostrar_Nodos_En_Nivel_N(nodo.getIzq())
            self.Mostrar_Nodos_En_Nivel_N(nodo.getDer())
    
    