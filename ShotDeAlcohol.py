class ShotDeAlcohol(Coctel):
     def __init__(self, nombre, precio, grados_alcohol, temperatura):
        super().__init__(nombre, precio, grados_alcohol)
        self.temperatura = temperatura

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
        def grados_alcohol(self):
            return self.__grados_alcohol
        
        @grados_alcohol.setter
        def grados_alcohol(self,dato):
         self.__grados_alcohol

        @property
        def temperatura(self):
            return self.__temperatura
        
        @temperatura.setter
        def temperatura(self,dato):
         self.__temperatura

    
    