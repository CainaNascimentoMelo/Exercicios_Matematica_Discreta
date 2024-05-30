def contar_letras(letra, texto):
    return texto.count(letra)

letra = input("Digite uma letra: ")
texto = input("Digite um texto: ")
print(f"A letra '{letra}' aparece {contar_letras(letra, texto)} vezes no texto.")
