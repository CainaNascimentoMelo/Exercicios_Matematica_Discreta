import math

def area_circunferencia(raio):
    return math.pi * (raio ** 2)

raio = float(input("Digite o raio da circunferência: "))
print(area_circunferencia(raio))
