#Tabla de Direccionamiento Abierto
import numpy as np
from codigos_extra import obtener_primo
class TablaHash:
    __tamaño : int
    __tabla : np.array
    def __init__(self,claves_a_almacenar : int):
        self.__tamaño = obtener_primo(round(claves_a_almacenar/0.7))
        self.__tabla = np.full(self.__tamaño,None,dtype = object)
    
 
#Ejemplo si un parcial que dice que debes almacenar 1000 claves en una tabla de direccionamiento abierto :
# claves_a_almacenar = 1000
# factor de carga = 0.7 (como sale en teoria)
# luego haciendo un seguimiento de ese objeto de dato
# self.__tamaño = obtener_primo(1000 / 0.7)  esos valores serian los que contienen las variables anteriores




#Tabla Encadenada

from codigos_extra import obtener_primo,ListaEnlazada
import numpy as np
class TablaHash:
    __tamaño : int
    __tabla : np.array
    def __init__(self,claves_a_almacenar : int, colisiones_esperadas : int):
        self.__tamaño = obtener_primo(round(claves_a_almacenar/colisiones_esperadas))
        self.__tabla = np.array(self.__tamaño, dtype=ListaEnlazada)
        for i in range(self.__tamaño):
            self.__tabla[i]= ListaEnlazada()


#Ejemplo si un parcial que dice que debes almacenar 1000 claves en una tabla encadenada y no especifican colisiones esperadas :
#claves_a_almacenar = 1000
# colisiones_esperadas = 4 (un valor que te saques de los huevos)
# luego haciendo un seguimiento de ese objeto de dato
# self.__tamaño = obtener_primo(1000/4)  esos valores serian los que contienen las variables anteriores


#Ejemplo si un parcial que dice que debes almacenar 1000 claves en una tabla encadenada y especifican  2 colisiones esperadas :
#claves_a_almacenar = 1000
# colisiones_esperadas = 2 
# luego haciendo un seguimiento de ese objeto de dato
# self.__tamaño = obtener_primo(1000/2)  esos valores serian los que contienen las variables anteriores


#Tabla usando Buckets
import numpy as np
from codigos_extra import obtener_primo

class TablaHash:
    __tamaño_tabla : int
    __tamaño_buckets : int
    __tabla : np.array
    def __init__(self,claves_a_almacenar : int, tamaño_buckets : int):
        self.__tamaño_tabla = obtener_primo(round(claves_a_almacenar/tamaño_buckets))
        self.__tamaño_buckets = tamaño_buckets
        self.__tabla = np.zeros( (round(self.__tamaño_tabla * 1.2) , self.__tamaño_buckets) , dtype=int)
        self.__tabla_contadora = np.zeros(self.__tamaño_tabla,dtype=int)

 
#Ejemplo si un parcial que dice que debes almacenar 1000 claves en una tabla usando buckets y especifican tamaño de cada buckets = 4:
# claves_a_almacenar = 1000
# tamaño_buckets = 4 
# luego haciendo un seguimiento de ese objeto de dato
# self.__tamaño = obtener_primo(1000 / 4)  esos valores serian los que contienen las variables anteriores
# self.__tamaño_buckets = 4
#self.__tabla = Matriz Bidimensional de orden MxN siendo M = self.__tamaño_tabla *1.2 ( es el tamaño de la tabla + 20% del ese tamaño y siendo n = self.__tamaño_buckets)
#self.__tabla_contadora = una array del tamaño de self.__tamaño_tabla
