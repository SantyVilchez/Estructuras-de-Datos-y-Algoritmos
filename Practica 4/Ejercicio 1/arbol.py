#el suprimir por ahora funca nomas en nodos de grado 0 y 1
from nodo_arbol import Nodo
from estructurador import visualizador
class Arbol:
    __raiz : Nodo
    def __init__(self):
        self.__raiz = None
    def insertar(self, valor :int):
        if not self.__raiz:
            self.__raiz = Nodo(valor)
        else:
            self._insertar(self.__raiz,valor)
    
    def _insertar(self,nodo : Nodo,valor:int):
        if nodo.getValor() == valor:
            print("El valor ya existe")
        elif valor < nodo.getValor():
            if nodo.getIzq():
                self._insertar(nodo.getIzq(),valor)
            else:
                nodo.setIzq(Nodo(valor))
        else:
            if nodo.getDer():
                self._insertar(nodo.getDer(),valor)
            else:
                nodo.setDer(Nodo(valor))
 
                    
    def inOrden(self):
        self._inOrden(self.__raiz)

    def _inOrden(self,nodo:Nodo):
        if nodo:
            self._inOrden(nodo.getIzq())
            print(nodo.getValor())#10/4/
            self._inOrden(nodo.getDer())

    def buscar(self,valor : int):
        self._buscar(self.__raiz,valor)

    def _buscar(self, nodo : Nodo, valor : int):
        if not nodo:
            print("El elemento no existe")
        elif nodo.getValor() == valor:
            print("El elemento existe")
        elif valor < nodo.getValor():
            self._buscar(nodo.getIzq(),valor)
        else:
            self._buscar(nodo.getDer(),valor)

    def grado(self,nodo : Nodo):
        grado = 0
        if nodo.getIzq():
            grado+=1
        if nodo.getDer():
            grado+=1
        return grado
    def suprimir(self,valor:int):
        self.__raiz = self._suprimir(self.__raiz,valor)
    def _suprimir(self,nodo : Nodo, valor : int):
        if not nodo:
            return None
        elif valor < nodo.getValor():
            nodo.setIzq(self._suprimir(nodo.getIzq(),valor))
        elif valor > nodo.getValor():
            nodo.setDer(self._suprimir(nodo.getDer(),valor))
        else :
            if self.grado(nodo) == 0:
                return None
            if self.grado(nodo) == 1:
                return nodo.getDer() if nodo.getDer() else nodo.getIzq()
            if self.grado(nodo) == 2:
                maximo = nodo.getIzq()
                while maximo.getDer() != None:
                    maximo = maximo.getDer()
                nodo.setValor(maximo.getValor())
                nodo.setIzq(self._suprimir(nodo.getIzq(), maximo.getValor()))
        return nodo
    
    def hoja(self,valor:int):
        return self._hoja(self.__raiz,valor)
    def _hoja(self, nodo : Nodo,valor:int ):
        es_hoja = None
        if not nodo:
            return es_hoja
        elif valor < nodo.getValor():
            es_hoja = self._hoja(nodo.getIzq(), valor)
        elif valor > nodo.getValor():
            es_hoja = self._hoja(nodo.getDer(),valor)
        else:
            if self.grado(nodo) == 0:
                es_hoja = True
            return es_hoja
        return es_hoja
    def hijo(self, hijo : int, padre : int):
        return self._hijo(self.__raiz,hijo,padre)
    def _hijo(self, nodo, hijo : int, padre : int):
        es_hijo = None
        if self.grado(nodo) == 0:
            return es_hijo
        elif self.grado(nodo) == 1:
            self._hoja(nodo.getIzq(), hijo)
            if padre == nodo.getValor():
                es_hijo = True
        elif hijo > nodo.getValor():
            self._hoja(nodo.getDer(),hijo)
            if padre == nodo.getValor():
                es_hijo = True
        else:
            return True
        return es_hijo
    def camino(self):
        pass
    def nivel(self):
        pass
    def altura(self):
        pass
    def preOrden(self):
        pass
    def postOrden(self):
        pass
    def raiz(self):
        return self.__raiz
"""La raíz de cada subárbol es un hijo o descendiente directo de r, y r es el padre o antecesor directo de
cada raíz de los subárboles.
 Camino de un nodo ni a otro nk: secuencia de nodos n1, n2, ...., nk , tal que ni es el padre de ni+1 para
1<=i<k. En un árbol existe solamente un camino desde la raíz a cada nodo.
 Si hay un camino entre los nodos n1 y n2, entonces n1 es antecesor de n2 y n2 es descendiente de n1.
 Longitud de camino de un nodo ni a otro nk: Número de aristas que forman el camino, o número de
nodos menos 1 que forman la secuencia. Existe un camino de longitud cero desde cada nodo a sí mismo.
 Nivel de un nodo: si el nodo x está en el nivel i, entonces sus descendientes directos están en el nivel
i+1. La raíz de un árbol, se define como localizada en el nivel 1.
 Profundidad o Altura del árbol: máximo de los niveles de todos los nodos del árbol.
 Grado de un nodo: Número de descendientes directos de un nodo.
 Grado del árbol: Grado máximo en todos los nodos.
 Nodo hoja: nodo de grado 0.
 Nodo Interior: Nodo no hoja.
 Árbol Ordenado: Árbol en el que las ramas de cada nodo están ordenadas"""
arbol = Arbol()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(7)
arbol.insertar(17)
arbol.insertar(1)
arbol.insertar(3)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(9)
arbol.insertar(11)
print("Arbol")
visualizador(arbol.raiz())
print(arbol.hijo(1,2))