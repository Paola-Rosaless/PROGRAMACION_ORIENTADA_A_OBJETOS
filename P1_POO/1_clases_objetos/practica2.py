"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
#_ _ para hacerlo privado
#_ para hacerlo protegido

class Coches:
    def init(self,color,marca,velocidad):
        self.__color = color
        self.__marca = marca
        self.__velocidad = velocidad

    def acelerar(self):
        self.__velocidad += 1    

    def frenar(self):
        self.__frenar -= 1

    def tocar_claxon(self):
        print("pi pi pi")

#Instanciar o crear objetos de la clase Coches

coche1=Coches("Blanco", "VW",220)
coche2=Coches("Azul", "Nissan",180)

# print(f"el color del coche 1 es: {coche1.__color}"), no se pueden usar directamente los atributos porque son privados
print(f"el claxon del coche 1 hace:")
coche1.tocar_claxon()

print(f"la velocidad del coche 1 es de:")
coche1.acelerar()

print(f"el claxon del coche 2 hace:")
coche2.tocar_claxon()