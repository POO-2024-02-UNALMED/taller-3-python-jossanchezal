
class TV:
    __numTV = 0
    def __init__(self, marca, estado: bool, control= None, canal: int = 1, precio: int = 500, volumen: int = 1):
        self.__marca = marca
        self.__canal = canal
        self.__precio = precio
        self.__estado = estado
        self.__volumen = volumen
        self.__control = control
        TV.__numTV += 1
    def getMarca(self):
        return self.__marca
    def setMarca(self, marca):
        self.__marca = marca
    def getCanal(self):
        return self.__canal
    def setCanal(self, canal):
        if self.__estado==True  and 0 <= canal <= 120: 
            self.__canal = canal
    def getPrecio(self):
        return self.__precio
    def setPrecio(self, precio):
        self.__precio = precio
    def getVolumen(self):
        return self.__volumen
    def setVolumen(self, volumen):
        if self.__estado==True and 0 <= volumen <= 7: 
            self.__volumen = volumen
    def getControl(self):
        return self.__control
    def setControl(self, control):
        self.__control = control
    @classmethod
    def getNumTV(cls):
        return cls.__numTV 
    @classmethod
    def setNumTV(cls, numTV):
        cls.__numTV = numTV
    def turnOff(self):
        if self.__estado== True:  
            self.__estado = False  
    def turnOn(self):
        if self.__estado==False:  
            self.__estado = True 
    def getEstado(self):
        return self.__estado
    def canalUp(self):
        if self.__estado==True and 1 <= self.__canal < 120:  
            self.__canal += 1
    def canalDown(self):
        if self.__estado==True and 1 < self.__canal <= 120: 
            self.__canal -= 1
    def volumenUp(self):
        if self.__estado==True and 0 <= self.__volumen < 7: 
            self.__volumen += 1
    def volumenDown(self):
        if self.__estado==True and 1 <= self.__volumen <= 7: 
            self.__volumen -= 1

    
