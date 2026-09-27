"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares (Marca, color, modelo, velocidad, potencia y numero de asientos) y con las operaciones de acelerar y frenar. Que los atributos y metodos sean publicos
#Muestre el color de los coches
#Que las operaciones disminuyan o aumenten la valocidad segun sea el caso y hay que jugar con los metodos e imprimes la velocidad final


class coches:
    marca=""
    color=""
    velocidad=0
    potencia=0
    asientos=0

    def acelerar(self):
        self.velocidad+= 1

    def frenar(self):
        self.velocidad-= 1

coche1 = coches()
coche2 = coches()

print(f"el color del coche 1 es: {coche1.color}")
coche1.color = "Rojo"
print(f"el color del coche 1 es: {coche1.color}")
coche2.color = "Blanco"
print(f"el color del coche 2 es: {coche2.color}")
print(f"La velocidad inicial del coche es de: {coche1.velocidad}")

for i in range(0, 10):
    coche1.acelerar()

print(f"La velocidad final del coche es de: {coche1.velocidad}")

