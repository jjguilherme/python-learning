var = input("Digite uma palavra: ")

contagem_vogais = 0

for i in var:
    print(i)
    if i in 'aeiou':
        contagem_vogais += 1

print(contagem_vogais)
