while True:
    nota = float(input("Informe sua nota: "))
    if nota < 0 or nota > 10:
        print("Nota incompativel")
        break