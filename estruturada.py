nomes = []  
notas1 = []
notas2 = []

def cadastrar () :
    nome = input ("nome do estudante")
    nota1 = float(input("nota 1: ")) # casting (to cast)
    nota2 = float(input("nota 1: "))

    nomes.append (nome)
    notas1.append(nota1)
    notas2.append(nota2)
    nome = nome 
print("aluno cadastrado com sucesso!")

def calcular_media(nota1, nota2): 
    media = (nota1 + nota2) / 2

def situação (indice): 
    media = calcular_media (indice) 
    if media >= 6:
        return "aprovado" 
    elif media >= 4:    
        return "Recuperação" 
    return "reprovado"

def listar ():
    if len(nomes) == 0:
        print ("nenhum estudante cadastro.")
        return 

    print(f"\n{'nome':<16}{'N1':<7}{'N2':7}{'MÉDIA':<8}{'SITUAÇÃO':<14}")


for i in range (len(nomes)): 
    print(f"{nomes [i]:<16}{notas1[1]:<7}{notas2[i]:<7}"f"{calcular_media(i):<8.1f}{situação(i):14}")

def media_da_turma():
    if len(nomes) == 0:
        print ("nenhum estudante cadastrado.")
    return

soma = 0
for i in range(len(nomes)):
    soma = soma +  calcular_media(i)
    print(f"\nMédia da turma: {soma/len(nomes) : . 3f}")

def menu() :
    while True:
        print("\n - cadastrar estudante")
        print("2 - Listar estudantes")
        print("3 - Média da turma")
        print("0 - Sair")

        opcao = input ("Opção: ")

        if opcao == "1" :
            cadastrar
        elif opcao == "2" :
            listar ()
        elif opcao == "3" :
            media_da_turma ()
        elif opcao == "0" : 
            break
        else:
            print ("Opção invalida")

menu ()