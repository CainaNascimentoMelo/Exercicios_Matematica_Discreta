def maior_menor(lista):
    return max(lista), min(lista)

lista_numeros = [int(x) for x in input("Digite os números separados por espaço: ").split()]
maior, menor = maior_menor(lista_numeros)
print(f"Maior: {maior}, Menor: {menor}")
