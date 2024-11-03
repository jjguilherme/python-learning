def tabela_multiplicacao_multiplos():
    # Solicita ao usuário os números desejados
    numeros_input = input("Digite os números para ver suas tabelas de multiplicação, separados por vírgula: ")

    # Converte a entrada do usuário em uma lista de inteiros
    numeros = [int(num.strip()) for num in numeros_input.split(',')]

    # Itera sobre os números de 1 a 10 para criar a tabela
    for i in range(1, 11):
        for numero in numeros:
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}", end="\t")  # Impressão na mesma linha
        print()  # Nova linha após cada iteração do i


# Chama a função
tabela_multiplicacao_multiplos()
