def tabela_multiplicacao():
    numero = int(input("Digite um número: "))

    print(f"Tabela de multiplicação de {numero}:")

    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabela_multiplicacao()