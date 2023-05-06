class CoctelConJugo(Coctel):
    def __init__(self):
        super().__init__(nombre, precio, grados_alcohol,frescura)
        self.frescura = frescura

 
    @property
    def nombre (self):
                return self.__nombre
            
    @nombre.setter
    def nombre(self,dato):
            self.__nombre

    @property
    def precio (self):
                return self.__precio
            
    @precio.setter
    def precio(self,dato):
            self.__precio

    @property
    def frescura (self):
            return self.__frescura
        
    @frescura.setter
    def frescura(self,dato):
         self.__frescura
    
    @property
    def grados_alcohol(self):
            return self.__grados_alcohol
        
    @grados_alcohol.setter
    def grados_alcohol(self,dato):
         self.__grados_alcohol
