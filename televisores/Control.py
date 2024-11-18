from televisores import TV

class Control:
    def __init__(self,tv: TV):
        self.tv = tv
    
    def turnOff(self):
        self.tv.turnOff
    def turnOn(self):
        self.tv.turnOn
    def canalUp(self):
        self.tv.turnOff
    def canalDown(self):
        self.tv.canalDown
    def volumenUp(self):
        self.tv.volumenUp
    def volumenDown(self):
        self.tv.volumenDown
    def setCanal(self):
        self.tv.setCanal
    def setvolumen(self):
        self.tv.setVolumen
    def enlazar(self, tv):
        self.tv = tv
        tv.setControl = self