def converter_gramas_para_quilogramas(gramas):
    return gramas / 1000

gramas = float(input("Digite quantas gramas: "))
quilogramas = converter_gramas_para_quilogramas(gramas)
print(f"{gramas}g são {quilogramas}kg")
