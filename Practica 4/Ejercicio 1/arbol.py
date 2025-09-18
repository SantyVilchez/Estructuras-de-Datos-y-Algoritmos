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
        elif nodo.getValor() > valor:
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
            print(nodo.getValor())
            self.__inOrden(nodo.getDer())

    def buscar(self,valor : int):
        self.__buscar(self.__raiz,valor)

    def __buscar(self, nodo : Nodo, valor : int):
        if not nodo:
            print("El elemento no existe")
        elif nodo.getValor() == valor:
            print("El elemento existe")
        elif nodo.getValor() > valor:
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
    
    # def suprimir(self,valor:int):
    #     self.__suprimir(self.__raiz,valor)

    # def __suprimir(self,nodo : Nodo, valor : int):
    #     if not nodo:
    #         print("El elemento no existe")
    #     elif nodo.getValor() > valor:
    #         self.__suprimir(nodo.getIzq(),valor)
    #     elif nodo.getValor() < valor:
    #         self.__suprimir(nodo.getDer(),valor)
    #     else:
    #         if self.grado(nodo) == 0:
    #             nodo.setValor()
    #         elif self.grado(nodo) == 1:
    #             if nodo.getIzq():
    #                 nodo.setValor(nodo.getIzq().getValor())
    #                 nodo.setIzq(None)
    #             else:
    #                 nodo.setValor(nodo.getDer().getValor())
    #                 nodo.setDer(None)
    #         else:
    #             pass

    def hoja(self):
        pass
    def hijo(self):
        pass
    def padre(self):
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
    def darRaiz(self):
        return self.__raiz
arbol = Arbol()
arbol.insertar(10)
arbol.insertar(4)
arbol.insertar(12)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(1)
arbol.insertar(11)
arbol.insertar(3)
arbol.insertar(5)
arbol.inOrden()

