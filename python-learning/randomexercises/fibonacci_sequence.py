n_atual = 0
n_proximo = 1
for i in range(1, 10):
    print(n_atual)
    novo_valor = n_atual + n_proximo
    n_atual = n_proximo
    n_proximo = novo_valor