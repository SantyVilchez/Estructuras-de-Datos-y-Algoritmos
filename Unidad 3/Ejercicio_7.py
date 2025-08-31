from random import randint,random
import math
class Trabajo:
    __tiempo : int
    __hojas : int
    __sig : None
    def __init__(self,tiempo,hojas):
        self.__tiempo = tiempo
        self.__hojas = hojas
        self.__sig = None
    def getTiempo(self):
        return self.__tiempo
    def setTiempo(self,tiempo : int):
        self.__tiempo = tiempo
    def getHojas(self):
        return self.__hojas
    def setHojas(self,hojas : int):
        self.__hojas = hojas
    def getSig(self):
        return self.__sig
    def setSig(self,sig):
        self.__sig = sig
class ColaEncadenada:
    __primero : Trabajo
    __ultimo : Trabajo
    __cant : int
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def longitud(self):
        return self.__cant
    def insertar(self,tiempo : int,hojas : int):
        nuevo = Trabajo(tiempo,hojas)
        if self.vacia():
            self.__primero = nuevo
        else:
            self.__ultimo.setSig(nuevo)
        self.__ultimo = nuevo
        self.__cant += 1
    def suprimir(self):
        if self.vacia():
            return 0
        else:
            tiempo_eliminado,hojas_eliminadas = self.__primero.getTiempo(),self.__primero.getHojas()
            self.__cant -= 1
            self.__primero = self.__primero.getSig()
            return tiempo_eliminado,hojas_eliminadas
    def recuperar(self)->Trabajo:
        return self.__primero
    def recorrer(self):
        aux = self.__primero
        while aux != None:
            print(aux.getTiempo(),aux.getHojas())
            aux = aux.getSig()
    

def SimuladorImpresora(tiempo_simulacion : int,tiempo_llegada : int,cola:ColaEncadenada):
    reloj = 0
    trabajos_impresos = 0
    impresora = 0
    tiempo_total_atencion = 0
    while reloj < tiempo_simulacion:
        if random() <= tiempo_llegada:
            hojas=randint(1,100)
            cola.insertar(reloj,hojas)
        if impresora == 0 and not cola.vacia():
            hojas_trabajo = cola.recuperar().getHojas()
            impresora = 3 if hojas_trabajo >= 30 else math.ceil(hojas_trabajo/10)
        if impresora > 0:
            hojas_trabajo = cola.recuperar().getHojas()
            if impresora == 1 :
                if hojas_trabajo > 10: 
                    cola.recuperar().setHojas(hojas_trabajo - 10)
                    tiempo,hojas = cola.suprimir()
                    cola.insertar(tiempo,hojas)
                else:
                    tiempo_espera = reloj - cola.recuperar().getTiempo()
                    tiempo_total_atencion += tiempo_espera
                    cola.suprimir()
                    trabajos_impresos += 1
            else:
                cola.recuperar().setHojas(hojas_trabajo - 10)
            impresora -= 1
        reloj += 1
    
    print(f"La cantidad de trabajos que quedaron sin imprimir fueron {cola.longitud()}")
    print(f"La cantidad de trabajos impresos fueron {trabajos_impresos}")
    print(f"El tiempo promedio de impresion fue de {(tiempo_total_atencion / trabajos_impresos):.2f} minutos")
SimuladorImpresora(60,0.2,cola = ColaEncadenada())
