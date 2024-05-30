import math

def volume_cilindro(raio, altura):
    return math.pi * raio**2 * altura

raio = float(input("Raio: "))
altura = float(input("Altura: "))
print(f"Volume do cilindro: {volume_cilindro(raio, altura)}")
