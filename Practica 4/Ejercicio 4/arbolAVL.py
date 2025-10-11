#Informacion necesaria para entender el codigo
#Cuando el arbol crece a la izquierda el balance del nodo es -1
#cuando el arbol crece a la derecha el balance es 1
#cuando el arbol esta balanceado es decir tiene ambos hijos su balane es 0
#el valor del balance nos permite saber que parte esta balanceada
#se actualiza conforme se insertan o suprimen valores, siempre indicando la direccion donde se producira el desbalance
#en resumen la variable balanceo sirve para saber donde se producira el desbalance y cuando se produzca balancear
#la variable contador del nodo cuenta los repetidos
from nodo_arbol import Nodo
from codigo_visualizador import visualizador
class ArbolAVL:
    __raiz : Nodo
    def __init__(self):
        self.__raiz = None
    def mostrar(self): #Buena funcion para debugear el arbol
        visualizador(self.DarRaiz()) #Esta funcion recibe una raiz y grafica el arbol en consola
    def insertar(self,valor : int):
        if self.__raiz == None:
            nuevo = Nodo(valor)
            self.__raiz = nuevo
        else:
            self._insertar(self.__raiz,valor, 0)

    def _insertar(self,nodo : Nodo,valor : int, altura : int):
        if valor < nodo.getValor():
            if nodo.getIzq() is None :
                nodo.setIzq(Nodo(valor))
                altura += 1
            else : 
                altura = self._insertar(nodo.getIzq(),valor,altura)
            #Actualizacion de balanceo en acarreo
            if altura:
                if nodo.getBalance() == 0 : 
                    nodo.setBalance(-1)
                elif nodo.getBalance() == 1 : 
                    nodo.setBalance(0)
                    altura = 0
                elif nodo.getBalance() == -1:
                    nodo_izq : Nodo = nodo.getIzq()
                    if nodo_izq.getBalance() == -1: #Rotacion simple
                        print()
                        nodo.setIzq(nodo_izq.getDer())
                        nodo_izq.setDer(nodo)
                        nodo.setBalance(0)
                        self.intercambio(nodo,nodo_izq)
                    else: #Rotacion Doble
                        nodo_der = nodo_izq.getDer()
                        nodo_izq.setDer(nodo_der.getIzq())
                        nodo_der.setIzq(nodo_izq)
                        nodo.setIzq(nodo_der.getDer())
                        nodo_der.setDer(nodo)
                        if nodo_der.getBalance() == -1:
                            nodo.setBalance(1)
                        else:
                            nodo.setBalance(0)
                        if nodo_der.getBalance() == 1:
                            nodo_izq.setBalance(-1)
                        else:
                            nodo_izq.setBalance(0)
                        self.intercambio(nodo,nodo_der)
                    nodo.setBalance(0)
                    altura = 0
        elif valor > nodo.getValor():
            if nodo.getDer() is None : 
                nodo.setDer(Nodo(valor))
                altura += 1
            else : 
                altura = self._insertar(nodo.getDer(),valor,altura)
            #Actualizacion de balanceo en acarreo
            if altura:
                if nodo.getBalance() == -1 : 
                    nodo.setBalance(0)
                    altura = 0
                elif nodo.getBalance() == 0 : 
                    nodo.setBalance(1)
                elif nodo.getBalance() == 1 :
                    nodo_der : Nodo = nodo.getDer()
                    if nodo_der.getBalance() == 1: #Rotacion simple
                        nodo.setDer(nodo_der.getIzq())
                        nodo_der.setIzq(nodo)
                        nodo.setBalance(0)
                        self.intercambio(nodo,nodo_der)
                    else: #Rotacion doble
                        nodo_izq = nodo_der.getIzq()
                        nodo_der.setIzq(nodo_izq.getDer())
                        nodo_izq.setDer(nodo_der)
                        nodo.setDer(nodo_izq.getIzq())
                        nodo_izq.setIzq(nodo)
                        if nodo_izq.getBalance() == 1:
                            nodo.setBalance(-1)
                        else:
                            nodo.setBalance(0)
                        if nodo_izq.getBalance() == -1:
                            nodo_der.setBalance(1)
                        else:
                            nodo_der.setBalance(0)
                        self.intercambio(nodo,nodo_izq)
                    nodo.setBalance(0)
                    altura = 0
        else:
            #Cuento valor repetido
            nodo.setContador(nodo.getContador()+1)
        return altura
    
    #Esta funcion permite manipular casos en que se modifica la raiz y en los que no
    #Intercambia los valores de las posiciones de memoria que recibe
    def intercambio(self, nodo_base : Nodo, nodo_izq : Nodo):
        tem_valor = nodo_base.getValor()
        tem_con = nodo_base.getContador()
        tem_bal = nodo_base.getBalance()
        tem_izq = nodo_base.getIzq()
        tem_der = nodo_base.getDer()
        nodo_base.setValor(nodo_izq.getValor())
        nodo_base.setContador(nodo_izq.getContador())
        nodo_base.setBalance(nodo_izq.getBalance())
        nodo_base.setIzq(nodo_izq.getIzq())
        nodo_base.setDer(nodo_izq)
        nodo_izq.setValor(tem_valor)
        nodo_izq.setContador(tem_con)
        nodo_izq.setBalance(tem_bal)
        nodo_izq.setIzq(tem_izq)
        nodo_izq.setDer(tem_der)
    def DarRaiz(self):
        return self.__raiz


arbol = ArbolAVL()
arbol.insertar(20)
arbol.insertar(0)
arbol.insertar(40)
arbol.insertar(-10)
arbol.insertar(10)
arbol.insertar(15)
arbol.insertar(5)
arbol.insertar(-20)
arbol.insertar(-5)
arbol.insertar(-30)
arbol.insertar(-15)
arbol.insertar(-40)
arbol.mostrar()
