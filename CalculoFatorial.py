def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)

numero = int(input("Digite um número para calcular seu fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")
