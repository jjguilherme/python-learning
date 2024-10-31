def contar_letras_true_love(nome1, nome2):

    palavras = ["TRUE", "LOVE"]

    resultado = {letra: 0 for palavra in palavras for letra in palavra}  # Inicializa contagem para cada letra

    nomes_concatenados = (nome1 + nome2).lower()

    for palavra in palavras:
        for letra in palavra:
            resultado[letra] += nomes_concatenados.count(letra)

    return resultado

nome1 = "Kanye West"
nome2 = "John Doe"
resultado = contar_letras_true_love(nome1, nome2)
print(resultado)
