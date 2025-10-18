from nodo_arbol import Nodo
class Arbol:
    __raiz : Nodo
    def __init__(self):
        self.__raiz = None
    def vacia(self):
        return self.__raiz == None
    # este metodo devuelve la raiz sera utilizado en todos los llamados a los metodos del arbol
    def darRaiz(self):
        return self.__raiz

    def insertar(self,nodo : Nodo,valor:int):
        if self.vacia() == True:
            self.__raiz = Nodo(valor)
        elif nodo.getValor() == valor:
            print("El valor ya existe")
        elif valor < nodo.getValor():
            if nodo.getIzq():
                self.insertar(nodo.getIzq(),valor)
            else:
                nodo.setIzq(Nodo(valor))
        else:
            if nodo.getDer():
                self.insertar(nodo.getDer(),valor)
            else:
                nodo.setDer(Nodo(valor))
  
    def inOrden(self,nodo:Nodo):
        if nodo:
            self.inOrden(nodo.getIzq())
            print(nodo.getValor())#10/4/
            self.inOrden(nodo.getDer())

    def buscar(self, nodo : Nodo, valor : int):
        if not nodo:
            nodo_encontrado = None
        elif nodo.getValor() == valor:
            nodo_encontrado = nodo
        elif valor < nodo.getValor():
            nodo_encontrado = self.buscar(nodo.getIzq(),valor)
        else:
            nodo_encontrado = self.buscar(nodo.getDer(),valor)
        return nodo_encontrado

    def grado(self,nodo : Nodo):
        grado = 0
        if nodo.getIzq():
            grado+=1
        if nodo.getDer():
            grado+=1
        return grado
    def suprimir(self,nodo : Nodo, valor : int):
        if not nodo:
            return None
        elif valor < nodo.getValor():
            nodo.setIzq(self.suprimir(nodo.getIzq(),valor))
        elif valor > nodo.getValor():
            nodo.setDer(self.suprimir(nodo.getDer(),valor))
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
                nodo.setIzq(self.suprimir(nodo.getIzq(), maximo.getValor()))
        return nodo
    
    def hoja(self,valor:int):
        nodo = self.buscar(self.darRaiz(),valor)
        es_hoja = False
        if not nodo:
            es_hoja = False
        elif self.grado(nodo)==0:
            es_hoja = True
        return es_hoja
    
    def hijo(self, hijo : int, padre : int):
        nodo_padre = self.buscar(self.darRaiz(),padre)
        es_hijo = False
        if nodo_padre == None:
            es_hijo = False
        elif nodo_padre.getIzq() != None and nodo_padre.getIzq().getValor() == hijo:
            es_hijo = True
        elif nodo_padre.getDer() != None and nodo_padre.getDer().getValor()==hijo:
            es_hijo = True
        return es_hijo
    def padre(self, padre:int, hijo:int):
        nodo_padre = self.buscar(self.darRaiz(),padre)
        es_padre = False
        if nodo_padre == None:
            es_padre = False
        elif nodo_padre.getIzq() != None and nodo_padre.getIzq().getValor() == hijo:
            es_padre = True
        elif nodo_padre.getDer() != None and nodo_padre.getDer().getValor()==hijo:
            es_padre = True
        return es_padre

    def nivel(self, nodo : Nodo, valor : int,nivel : int):
        if nodo == None:
            nivel = 0
        elif valor < nodo.getValor():
            nivel += 1
            nivel = self.nivel(nodo.getIzq(),valor,nivel)
        elif valor > nodo.getValor():
            nivel += 1
            nivel = self.nivel(nodo.getDer(),valor,nivel)
        else:
            nivel+=1
        return nivel

    def altura(self, nodo : Nodo, altura : int):
        if nodo:
            if altura < self.nivel(nodo.getValor()):
                altura +=1
            altura = self.altura(nodo.getIzq(),altura)
            altura = self.altura(nodo.getDer(),altura)
        return altura

    def PreOrden(self,nodo:Nodo):
        if nodo:
            print(nodo.getValor())
            self.PreOrden(nodo.getIzq())
            self.PreOrden(nodo.getDer())

    def PostOrden(self,nodo:Nodo):
        if nodo:
            self.PostOrden(nodo.getIzq())
            self.PostOrden(nodo.getDer())
            print(nodo.getValor())

    def antecesor(self,x : int,z : int):
        es_antecesor = False
        if self.buscar(self.buscar(self.darRaiz(),x),z) != None:
            es_antecesor = True
        return es_antecesor
        
    def camino(self,inicio : int,fin : int):
        es_antecesor = self.antecesor(inicio, fin)
        camino = []
        if es_antecesor == True:
            nodo_actual = self.buscar(inicio)
            while nodo_actual != None and nodo_actual.getValor() != fin:
                if fin < nodo_actual.getValor():
                    camino.append(0)
                    nodo_actual = nodo_actual.getIzq()
                else:
                    camino.append(1)
                    nodo_actual = nodo_actual.getDer()
        return camino

arbol = Arbol()
arbol.insertar(arbol.darRaiz(),10)
arbol.insertar(arbol.darRaiz(),1)
arbol.insertar(arbol.darRaiz(),20)
arbol.insertar(arbol.darRaiz(),-2)
arbol.insertar(arbol.darRaiz(),15)
arbol.inOrden(arbol.darRaiz())






