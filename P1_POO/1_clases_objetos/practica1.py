"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

## Implementar el paradigma estructurado

def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(5, 3))

## Implementar el paradigma Orientado a Objetos (OO)

class Rectangulos:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

rect = Rectangulos(5, 3)
# Los metodos se invocan mediante el objeto
print(rect.area())

## Variante 2

class Rectangulos:
    def area(self, base, altura):
        areaR = base * altura
        return areaR

#No se le pone ningun valor dentro de los parentesis del 
rectangulo1 = Rectangulos() #Crear o instanciar un objeto "rectangulo1" de la clase "Rectangulos"
print(f"El area del rectangulo es: {rectangulo1.area(5, 6)}")

