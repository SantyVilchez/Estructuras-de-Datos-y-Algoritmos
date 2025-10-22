from nodo_arbol import Nodo
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

    def buscar(self,valor : int)->Nodo:
        return self._buscar(self.__raiz,valor)

    def _buscar(self, nodo : Nodo, valor : int):
        if not nodo:
            nodo_encontrado = None
        elif nodo.getValor() == valor:
            nodo_encontrado = nodo
        elif valor < nodo.getValor():
            nodo_encontrado = self._buscar(nodo.getIzq(),valor)
        else:
            nodo_encontrado = self._buscar(nodo.getDer(),valor)
        return nodo_encontrado

    def grado(self,nodo : Nodo):
        grado = 0
        if nodo.getIzq():
            grado+=1
        if nodo.getDer():
            grado+=1
        return grado
    def suprimir(self,valor:int):
        self._suprimir(self.__raiz,valor)
    def _suprimir(self,nodo : Nodo, valor : int):
        if not nodo:
            return None
        elif valor < nodo.getValor():
            nodo.setIzq(self._suprimir(nodo.getIzq(),valor))
        elif valor > nodo.getValor():
            nodo.setDer(self._suprimir(nodo.getDer(),valor))
        else :
            if self.grado(nodo) == 0:
                nodo =  None
            if self.grado(nodo) == 1:
                nodo =  nodo.getDer() if nodo.getDer() else nodo.getIzq()
            if self.grado(nodo) == 2:
                maximo = nodo.getIzq()
                while maximo.getDer() != None:
                    maximo = maximo.getDer()
                nodo.setValor(maximo.getValor())
                nodo.setIzq(self._suprimir(nodo.getIzq(), maximo.getValor()))
        return nodo
    
    def hoja(self,valor:int):
        nodo = self.buscar(valor)
        es_hoja = False
        if not nodo:
            es_hoja = False
        elif self.grado(nodo)==0:
            es_hoja = True
        return es_hoja
    
    def hijo(self, hijo : int, padre : int):
        nodo_padre = self.buscar(padre)
        es_hijo = False
        if nodo_padre == None:
            es_hijo = False
        elif nodo_padre.getIzq() != None and nodo_padre.getIzq().getValor() == hijo:
            es_hijo = True
        elif nodo_padre.getDer() != None and nodo_padre.getDer().getValor()==hijo:
            es_hijo = True
        return es_hijo
    def padre(self, padre:int, hijo:int):
        nodo_padre = self.buscar(padre)
        es_padre = False
        if nodo_padre == None:
            es_padre = False
        elif nodo_padre.getIzq() != None and nodo_padre.getIzq().getValor() == hijo:
            es_padre = True
        elif nodo_padre.getDer() != None and nodo_padre.getDer().getValor()==hijo:
            es_padre = True
        return es_padre
    def nivel(self,valor : int):
        return self._nivel(self.__raiz,valor,0)
    def _nivel(self, nodo : Nodo, valor : int,nivel : int):
        if nodo == None:
            nivel = 0
        elif valor < nodo.getValor():
            nivel += 1
            nivel = self._nivel(nodo.getIzq(),valor,nivel)
        elif valor > nodo.getValor():
            nivel += 1
            nivel = self._nivel(nodo.getDer(),valor,nivel)
        else:
            nivel+=1
        return nivel
    def altura(self):
        return self._altura(self.__raiz,0)
    
    def _altura(self, nodo : Nodo, altura : int):
        if nodo:
            if altura < self.nivel(nodo.getValor()):
                altura +=1
            altura = self._altura(nodo.getIzq(),altura)
            altura = self._altura(nodo.getDer(),altura)
        return altura

    def PreOrden(self):
        self._PreOrden(self.__raiz)

    def _PreOrden(self,nodo:Nodo):
        if nodo:
            print(nodo.getValor())
            self._PreOrden(nodo.getIzq())
            self._PreOrden(nodo.getDer())
 
    def PostOrden(self):
        self._PostOrden(self.__raiz)

    def _PostOrden(self,nodo:Nodo):
        if nodo:
            self._PostOrden(nodo.getIzq())
            self._PostOrden(nodo.getDer())
            print(nodo.getValor())
    def raiz(self):
        return self.__raiz
    def antecesor(self,x : int,z : int):
        es_antecesor = False
        if self._buscar(self.buscar(x),z) != None:
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








