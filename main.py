from Coctel import Coctel
from ContelConJugo import CoctelConJugo
from ShotDeAlcohol import ShotDeAlcohol

def calcular_costo_venta(self, cantidad):
        costo = cantidad * self.precio
        return costo


def calcular_costo_venta(self, cantidad, dias_anejamiento):
        if dias_anejamiento == 1:
            costo = cantidad * self.precio
        elif dias_anejamiento == 2:
            costo = cantidad * self.precio * 0.8
        elif dias_anejamiento == 3:
            costo = cantidad * self.precio * 0.5
        else:
            costo = 0
        
        return costo

coctel_con_jugo = CoctelConJugo("Mojito", 120, 10, "Alta")
shot = ShotDeAlcohol("Tequila", 50, 40, "Frio")

costo_coctel_con_jugo = coctel_con_jugo.calcular_costo_venta(5, 2)
costo_shot = shot.calcular_costo_venta(10)

print("Costo de venta del coctel con jugo:", costo_coctel_con_jugo)
print("Costo de venta del shot:", costo_shot)
