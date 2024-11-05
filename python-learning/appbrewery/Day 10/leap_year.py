def eh_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

# Teste
ano = 2024
print(f"{ano} é bissexto?" , eh_bissexto(ano))
