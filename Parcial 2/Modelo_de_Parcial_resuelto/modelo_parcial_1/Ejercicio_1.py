#A)
class Arbol:
    __raiz : Nodo
    def __init__(self):
        self.__raiz = None

#B)
def contador_nodos_un_solo_descendiente(self,nodo : Nodo, c):
    if nodo:
        c = contador_nodos_un_solo_descendiente(nodo.getIzq(),c)
        c = contador_nodos_un_solo_descendiente(nodo.getDer(),c)
        if nodo.grado() == 1:
            c +=1
    return c

contador_nodos_un_solo_descendiente(arbol.raiz(),0)
    