#A)
class TablaHash:
    __tamaño : int
    __tabla : np.array
    #ese valor 0.7 es el factor de carga
    def __init__(self,claves_a_almacenar = 500):
        self.__tamaño = obtener_primo(round(claves_a_almacenar/0.7))
        self.__tabla = np.zeros(self.__tamaño,dtype = object)

#B)    
    def hash(self,valor : int):
        return valor % self.__tamaño
    def insertar(self, valor:int):
            indice = self.hashing(valor)
            repetido = False 
            if self.__tabla[indice] == 0: 
                self.__tabla[indice] = valor
            else: 
                final = indice
                indice = (indice + 1) % self.__tamaño 
                while self.__tabla[indice] != None and indice != final:
                    indice = (indice + 1) % self.__tamaño
                if indice != final:
                    self.__tabla[indice] = valor
