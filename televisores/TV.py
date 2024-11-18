from televisores import Marca
class TV:
    numTV = 0
    def __init__(self, control, estado,marca: Marca,  canal: int=1, precio: int=500, volumen: int=1):
        self.marca= marca
        self.canal= canal
        self.precio= precio
        self.estado= estado
        self.volumen= volumen
        self.control= control
        TV.numTV+=1
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca=marca
    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        if canal <= 120 or canal >= 0:
            self.canal=canal
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio=precio
    def getVolumen(self):
        return self.volumen
    def setVolumen(self, volumen):
        if self.volumen <= 7 or self.volumen >= 0:
            self.volumen=volumen
    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control=control
    @classmethod
    def getNumTV(cls):
        return cls.numTV 
    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV=numTV
    def turnOff(self,estado):
        if self.estado==True:
            estado==False
    def turnOn(self,estado):
        if self.estado==False:
            estado==True
    def getEstado(self):
        return self.estado
    def canalUp(self):
        if self.canal < 120 or self.canal >= 0:
            self.canal+=1
    def canalDown(self):
        if self.canal <= 120 or self.canal > 0:
             self.canal-=1
    def volumenUp(self):
        if self.volumen < 7 or self.volumen >= 0:
            self.volumen+=1
    def volumenDown(self):
        if self.volumen <= 7 or self.volumen > 0:
            self.volumen-=1

    
    


    
    
    