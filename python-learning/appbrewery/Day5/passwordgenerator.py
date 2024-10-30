import random

numbes = ['1','2','3','4','5','6','7','8','9','0']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', '<', '>', ',', '.', '?', '/']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letras_aleatorias = ""
for _ in range(nr_letters):
    letras_aleatorias += random.choice(letters)
simbolos_aleatorios = ""
for _ in range(nr_symbols):
    simbolos_aleatorios += random.choice(simbolos)
numero_aleatorio = ""
for _ in range(nr_numbers):
    numero_aleatorio += random.choice(numbes)

senha= letras_aleatorias + simbolos_aleatorios + numero_aleatorio
lista_senha = list(senha)
random.shuffle(lista_senha)
senha_final = ''.join(lista_senha)
print(senha_final)

#ABAIXO ESTÁ UM MODO PYTHONICO FEITO PELO CHAT GPT
#import random  # Importa o módulo random para gerar números aleatórios
#import string  # Importa o módulo string que contém conjuntos de caracteres padrão

#print("Welcome to the PyPassword Generator!")  # Mensagem de boas-vindas
#nr_letters = int(input("How many letters would you like in your password?\n"))  # Solicita ao usuário a quantidade de letras
#nr_symbols = int(input("How many symbols would you like?\n"))  # Solicita ao usuário a quantidade de símbolos
#nr_numbers = int(input("How many numbers would you like?\n"))  # Solicita ao usuário a quantidade de números

#letras_aleatorias = random.choices(string.ascii_lowercase, k=nr_letters)  # Gera letras aleatórias
#simbolos_aleatorios = random.choices("!@#$%^&*()-_+=[]{};:'\"<>,.?/", k=nr_symbols)  # Gera símbolos aleatórios
#numero_aleatorio = random.choices(string.digits, k=nr_numbers)  # Gera números aleatórios

#senha = letras_aleatorias + simbolos_aleatorios + numero_aleatorio  # Junta todas as partes da senha
#random.shuffle(senha)  # Embaralha a lista de caracteres
#senha_final = ''.join(senha)  # Junta os caracteres em uma string final

#print(senha_final)  # Exibe a senha final gerada
