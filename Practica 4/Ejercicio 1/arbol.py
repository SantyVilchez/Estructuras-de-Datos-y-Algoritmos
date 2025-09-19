#el suprimir por ahora funca nomas en nodos de grado 0 y 1
from nodo_arbol import Nodo
class Arbol:
    __raiz : Nodo
    def __init__(self):
        self.__raiz = None
    def insertar(self, valor :int):
        if not self.__raiz:
            self.__raiz = Nodo(valor)
        else:
            self.__insertar(self.__raiz,valor)
    
    def __insertar(self,nodo : Nodo,valor:int):
        if nodo.getValor() == valor:
            print("El valor ya existe")
        elif valor < nodo.getValor():
            if nodo.getIzq():
                self.__insertar(nodo.getIzq(),valor)
            else:
                nodo.setIzq(Nodo(valor))
        else:
            if nodo.getDer():
                self.__insertar(nodo.getDer(),valor)
            else:
                nodo.setDer(Nodo(valor))
 
                    
    def inOrden(self):
        self.__inOrden(self.__raiz)

    def __inOrden(self,nodo:Nodo):
        if nodo:
            self.__inOrden(nodo.getIzq())
            print(nodo.getValor())#10/4/
            self.__inOrden(nodo.getDer())

    def buscar(self,valor : int):
        self.__buscar(self.__raiz,valor)

    def __buscar(self, nodo : Nodo, valor : int):
        if not nodo:
            print("El elemento no existe")
        elif nodo.getValor() == valor:
            print("El elemento existe")
        elif valor < nodo.getValor():
            self.__buscar(nodo.getIzq(),valor)
        else:
            self.__buscar(nodo.getDer(),valor)

    def grado(self,nodo : Nodo):
        grado = 0
        if nodo.getIzq():
            grado+=1
        if nodo.getDer():
            grado+=1
        return grado
    
    def suprimir(self,valor:int):
        self.__suprimir(self.__raiz,valor)

    def __suprimir(self,nodo : Nodo, valor : int):
        grado = -1
        if not nodo:
           return -1
        elif valor < nodo.getValor():
            grado =  self.__suprimir(nodo.getIzq(),valor)
        elif valor > nodo.getValor():
            grado = self.__suprimir(nodo.getDer(),valor)
        else :
            if self.grado(nodo) == 0:
                return 0
            elif self.grado(nodo) == 1:
                return 1
            else:
                pass
        print(f"en el nodo con valor {nodo.getValor()} el grado es {grado}")
        if grado == 0:
            if nodo.getDer() != None:
                if valor == nodo.getDer().getValor():
                    nodo.setDer(None)
            if nodo.getIzq() != None:
                if valor == nodo.getIzq().getValor():
                    nodo.setIzq(None)
            grado =-1
        elif grado == 1:
            if nodo.getDer() != None:
                if valor == nodo.getDer().getValor():
                    nodo.setDer(nodo.getDer().getDer() if nodo.getDer().getDer() else nodo.getDer().getIzq())
            if nodo.getIzq() != None:
                if valor == nodo.getIzq().getValor():
                    nodo.setIzq(nodo.getIzq().getDer() if nodo.getDer().getDer() else nodo.getIzq().getIzq())
        else:
            pass
            

    def raiz(self):
        return self.__raiz
    def hoja(self):
        pass
    def hijo(self):
        pass
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

arbol = Arbol()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(7)
arbol.insertar(17)

print("Lista")
arbol.inOrden()
arbol.suprimir(15)
print("Lista Luego de suprimir")
arbol.inOrden()