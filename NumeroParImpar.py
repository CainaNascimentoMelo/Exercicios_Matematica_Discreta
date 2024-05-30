def par_ou_impar(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um número: "))
print(par_ou_impar(numero))
