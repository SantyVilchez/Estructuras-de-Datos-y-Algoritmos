from nodo_lista_en import Nodo
class ListaEncadenada:
    __cabeza : Nodo
    __cant : int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self,elem:int):
        nuevo = Nodo(elem)
        if self.__cant:
            anterior = None
            actual = self.__cabeza
            while actual != None and actual.getElem() < elem:
                anterior = actual
                actual = actual.getSig()
            if anterior:
                nuevo.setSig(anterior.getSig())
                anterior.setSig(nuevo)
            else:
                nuevo.setSig(self.__cabeza)
                self.__cabeza = nuevo
        else:
            self.__cabeza = nuevo
        self.__cant += 1
    def suprimir(self,posicion:int):
        if 1 <= posicion <= self.__cant:
            if not self.vacia():
                posicion -= 1
                indice = 0
                anterior = None
                actual = self.__cabeza
                while indice != posicion:
                    anterior = actual
                    actual = anterior.getSig()
                    indice += 1
                if anterior:
                    anterior.setSig(actual.getSig())
                else:
                    self.__cabeza = actual.getSig()
                self.__cant-=1
            else:
                print("La lista esta vacia")
        else:
            print("indice fuera de rango")
    def recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getElem())
            aux = aux.getSig()
    def buscar(self,elemento):
        encontrado = False
        aux = self.__cabeza
        while aux != None and aux.getElem() != elemento:
            aux = aux.getSig()
        if aux:
            encontrado = True
        return encontrado

print("Lista encadenada ")
LE = ListaEncadenada()
LE.insertar(1)
LE.insertar(2)
LE.insertar(4)
LE.insertar(4)
LE.insertar(0)
LE.insertar(10)
LE.insertar(7)
LE.recorrer()