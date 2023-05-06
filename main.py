from escuderias import Escuderia

escuderias = []
contador = 1
numeroEscuderias = int(input("Digite el numero de escuderias: "))
while contador <= numeroEscuderias:
    escuderia = Escuderia()
    escuderia.nombre = input("digite el nombre de la escuderia: ")
    escuderia.casaMotor = input("digite el nombre del casamotor: ")
    escuderia.pilotoPrincipal.nombre = input("digita el nombre del piloto: ")
    escuderia.pilotoPrincipal.salarioAnual = input("digita el salario: ")
    escuderia.pilotoPrincipal.fechaNacimiento = input(
        "digita la fecha de nacimiento: ")
    escuderia.pilotoPrincipal.pais = input("digita el pais: ")
    escuderia.piloto2.nombre = input("digita el nombre del piloto: ")
    escuderia.piloto2.salarioAnual = input("digita el salario: ")
    escuderia.piloto2.fechaNacimiento = input(
        "digita la fecha de nacimiento: ")
    escuderia.piloto2.pais = input("digita el pais del piloto: ")
    escuderia.costos = input("ingrese los costos: ")


escuderias.append(escuderia)

contador = contador + 1

# Recorriendo la Lista de escuderías

for escuderia in escuderias:
    print(escuderia.nombre, escuderia.costos)

costoMayor = 0
nombreEscuderiaMasCara = None

for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
        nombreEscuderiaMasCara = escuderia.nombre