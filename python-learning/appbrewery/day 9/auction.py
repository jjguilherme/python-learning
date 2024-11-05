print("Welcome to the AUCTION PROGRAM!!!!!!!!")

bid={}

while(True):
    name_input = input("What's your name?")
    bid_input = int(input("What's your bid?"))

    bid[name_input] = bid_input

    resposta = input("Someone want to bid again?").lower()
    if resposta != 's':
        break

maior_aposta = max(bid, key=bid.get)
print(f"\nA maior aposta é de {maior_aposta}, com o valor de {bid[maior_aposta]}.")