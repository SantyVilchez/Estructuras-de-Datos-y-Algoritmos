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
    while reloj < tiempo_simulacion:
        print(f"-------minuto {reloj}--------")
        if random() <= 1 / tiempo_llegada:
            print("********Llego un trabajo**********")
            hojas=randint(1,100)
            cola.insertar(reloj,hojas)
            print(f"llego un trabajo al minuto {reloj} con {hojas} hojas")
            print(f"hay ya {cola.longitud()} trabajos en espera")
        if impresora == 0 and not cola.vacia():
            print("!!!!Impresora Libre!!!!")
            print(f"Entro el trabajo con {cola.recuperar().getHojas()} hojas del minuto {cola.recuperar().getTiempo()}")
            hojas_trabajo = cola.recuperar().getHojas()
            impresora = 3 if hojas_trabajo >= 30 else math.ceil(hojas_trabajo/10)
            print(f"Dio una cantidad de {impresora} quantums!!")
        if impresora > 0:
            print(f"La Impresora lleva {impresora} quantums")
            hojas_trabajo = cola.recuperar().getHojas()
            if impresora == 1 :
                print("Ultima vuelta de la impresora")
                if cola.recuperar().getHojas() > 10: 
                    cola.recuperar().setHojas(hojas_trabajo - 10)
                    tiempo,hojas = cola.suprimir()
                    print(f"luego de suprimir en la cola quedaron {cola.longitud()} en espera")
                    cola.insertar(reloj,hojas)
                    print(f"aqui se inserto el trabjo que supero el quantum y quedo {cola.longitud()}")
                    print(f"la impresora tiene > 10 hojas tiene {hojas_trabajo} - 10 = {hojas}")
                    print(f"la impresora volvio a insertar al final este trabajo")
                else:
                    print(f"Ya queda menos de 10 hojas ,un trabajo termino!!!!!!!!!!!!!!!!!!!!!! con {cola.recuperar().getHojas()}")
                    cola.suprimir()
                    print(f"ya quedan {cola.longitud()} trabajos en cola")
                    trabajos_impresos += 1
            else:
                print(f"Se gasto un quantum y quedaron ya {hojas_trabajo - 10} hojas")
                cola.recuperar().setHojas(hojas_trabajo - 10)
            impresora -= 1
            print(f"la impresora le quedan {impresora} vueltas para estar libre")
        reloj += 1
    
    print(f"La cantidad de trabajos que quedaron sin imprimir fueron {cola.longitud()}")
    print(f"La cantidad de trabajos impresos fueron {trabajos_impresos}")
    
SimuladorImpresora(60,5,cola = ColaEncadenada())
