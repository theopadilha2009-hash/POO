class Estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        media = self.media()

        if media >= 6:
            return "Aprovado"
        elif media >= 4:
            return "Recuperação"
        else:
            return "Reprovado"

    def descrever(self):
        return f"{self.nome:<16}{self.nota1:<7.1f}{self.nota2:<7.1f}{self.media():<8.1f}{self.situacao():<14}"


estudantes = []


def cadastrar():
    nome = input("Digite o nome do estudante: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))

    estudante = Estudante(nome, nota1, nota2)
    estudantes.append(estudante)

    print("Aluno cadastrado com sucesso!")


def listar():
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    print(f"\n{'Nome':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUAÇÃO':<14}")

    for estudante in estudantes:
        print(estudante.descrever())


def media_da_turma():
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    soma = sum(estudante.media() for estudante in estudantes)
    media = soma / len(estudantes)

    print(f"\nMédia da turma: {media:.2f}")


def menu():
    while True:
        print("\n1 - Cadastrar estudante")
        print("2 - Listar estudantes")
        print("3 - Média da turma")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            listar()

        elif opcao == "3":
            media_da_turma()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


menu()