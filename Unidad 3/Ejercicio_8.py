from random import random,choice,randint
class nodo:
    __tiempo_llegada : int
    __sig : object
    def __init__(self,reloj:int):
        self.__tiempo_llegada = reloj
        self.__sig = None
    def getsiguiente(self):
        return self.__sig
    def setsiguiente(self,new:object):
        self.__sig = new
    def gettiempo(self):
        return self.__tiempo_llegada
    def settiempo(self,nuevo:int):
        self.__tiempo_llegada = nuevo
class Cola:
    __primero : nodo
    __ultimo : nodo
    __cant : int
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def longitud(self):
        return self.__cant
    def insertar(self,reloj:int):
        nuevo = nodo(reloj)
        if self.vacia():
            self.__primero = nuevo
        else:
            self.__ultimo.setsiguiente(nuevo)
        self.__ultimo = nuevo
        self.__cant += 1
    def suprimir(self):
        if self.vacia():
            return 0
        else:
            borrado = self.__primero.gettiempo()
            self.__primero = self.__primero.getsiguiente()
            self.__cant-=1
            return borrado

cajeros = [Cola() for x in range(3)]
def SimuladorBanco(tiempo_simulacion:int,tiempo_promedio_llegada:int,cajeros:list[Cola]):
    reloj = 0
    cajero_1 = 0
    cajero_2 = 0
    cajero_3 = 0
    tiempo_acumulado_espera = 0
    clientes_atentidos = 0
    tiempo_maximo_espera = 0
    while reloj < tiempo_simulacion:

        if random() <= tiempo_promedio_llegada:

            if cajero_1 == 0 or cajero_2 == 0 or cajero_3 == 0: 
                cajero_elegido = choice([i for i,x in enumerate([cajero_1,cajero_2,cajero_3]) if x == 0]) 
                cajeros[cajero_elegido].insertar(reloj)

            else:
                cajero_con_menor_cola = choice([i for i,x in enumerate(cajeros) if x.longitud() == min([cajeros[i].longitud() for i in range(3) ])])
                cajeros[cajero_con_menor_cola].insertar(reloj)

        if cajero_1 == 0  and not cajeros[0].vacia():
            atendido_de_cajero_1 = cajeros[0].suprimir()
            cajero_1 = 5

        if cajero_2 == 0 and not cajeros[1].vacia():
            atendido_de_cajero_2 = cajeros[1].suprimir()
            cajero_2 = 3

        if cajero_3 ==0 and not cajeros[2].vacia():
            atendido_de_cajero_3 = cajeros[2].suprimir()
            cajero_3 = 4

        if cajero_1 > 0:
            if cajero_1 == 1:
                clientes_atentidos += 1
                tiempo_espera = reloj - atendido_de_cajero_1
                tiempo_acumulado_espera += tiempo_espera
                tiempo_maximo_espera = max(tiempo_espera,tiempo_maximo_espera)
            cajero_1 -= 1
        if cajero_2 > 0:
            if cajero_2 == 1:
                clientes_atentidos += 1
                tiempo_espera = reloj - atendido_de_cajero_2
                tiempo_acumulado_espera += tiempo_espera
                tiempo_maximo_espera = max(tiempo_espera,tiempo_maximo_espera)
            cajero_2 -= 1
        if cajero_3 > 0:
            if cajero_3 == 1:
                clientes_atentidos += 1
                tiempo_espera = reloj - atendido_de_cajero_3
                tiempo_acumulado_espera += tiempo_espera
                tiempo_maximo_espera = max(tiempo_espera,tiempo_maximo_espera)
            cajero_3 -= 1
        reloj +=1

    clientes_sin_atender = sum([cajero.longitud() for cajero in cajeros])

    valores_cola = [x.suprimir() for x in cajeros for y in range(x.longitud()) if not x.vacia()]

    tiempo_acumulado_espera_sin_atender = sum(valores_cola)

    valor_maximo_tiempo_cola = 0 if valores_cola == []  else max(valores_cola)

    tiempo_maximo_espera = max(tiempo_maximo_espera,valor_maximo_tiempo_cola)

    print(f"El tiempo maximo de espera de los clientes en la cola fue {tiempo_maximo_espera}m")
    print(f"La cantidad de clientes atendidos fue {clientes_atentidos}")
    print(f"La cantidad de clientes que quedaron sin atender fueron {clientes_sin_atender}")
    print(f"El Promedio de espera de los clientes atendidos fue {tiempo_acumulado_espera/clientes_atentidos:.2f}m")
    print(f"El promedio de espera de los clientes sin atender fue {tiempo_acumulado_espera_sin_atender/clientes_sin_atender if clientes_sin_atender != 0 else 0}m")
SimuladorBanco(120,0.5,cajeros)

