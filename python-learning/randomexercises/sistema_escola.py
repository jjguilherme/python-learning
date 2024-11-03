alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")

    #validacao da entrada
    if nome.strip() == "":
        print("O nome não pode estar vazio.")
        return

    try:
        idade = int(idade) #converte a idade para um inteiro
    except ValueError:
        print("A idade deve ser um número inteiro.")
        return

    aluno = {"nome": nome, "idade": idade}
    alunos.append(aluno)
    print("Aluno adicionado com sucesso!")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno registrado.")
    else:
        print("Lista de alunos:")
        for aluno in alunos:
            print(f"- {aluno['nome']}, {aluno['idade']} anos")

def buscar_aluno():
    nome = input("Digite o nome do aluno que deseja buscar: ")
    encontrado = False

    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            print(f"Aluno encontrado: {aluno['nome']}, {aluno['idade']} anos")
            encontrado = True
            break
    if not encontrado:
        print("Aluno não encontrado.")

def remover_aluno():
    nome = input("Digite o nome do aluno que deseja remover: ")
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            alunos.remove(aluno)
            print(f"Aluno {nome} removido com sucesso!")
            return
    print("Aluno não encontrado.")

def main():
    print("Bem vindo ao sistema de registro dos alunos!")
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar aluno")
        print("2. Listar alunos")
        print("3. Buscar aluno")
        print("4. Remover aluno")
        print("5. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opçao válida.")

if __name__ == "__main__":
    main()