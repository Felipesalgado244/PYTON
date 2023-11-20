while True:
    nota = float(input("Informe uma nota maior que 0 e menor que 10: "))
    if nota < 0 or nota > 10:
        print("Nota inválida")
    if nota >= 0 and nota <= 10:
        break