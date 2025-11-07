#A)
class Arbol:
    __raiz : Nodo
    def __init__(self):
        self.__raiz = None

#B)
    #si no te especifican implementar el buscar directamente llamalo
    
    # def buscar(self, nodo : Nodo, valor : int):
    #     if not nodo:
    #         nodo_encontrado = None
    #     elif nodo.getValor() == valor:
    #         nodo_encontrado = nodo
    #     elif valor < nodo.getValor():
    #         nodo_encontrado = self.buscar(nodo.getIzq(),valor)
    #     else:
    #         nodo_encontrado = self.buscar(nodo.getDer(),valor)
    #     return nodo_encontrado
    
    def Mostrar_Nodos_En_Nivel_N(self,nodo : Nodo):
        if nodo:
            if self.grado(nodo) == 0:
                print(nodo.getDato())
            self.Mostrar_Nodos_En_Nivel_N(nodo.getIzq())
            self.Mostrar_Nodos_En_Nivel_N(nodo.getDer())

valor =  int(input("Ingrese valor de nodo para ver sus nodos terminales"))
arbol.Mostrar_Nodos_En_Nivel_N( arbol.buscar(valor) )