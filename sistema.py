treinos = []
exercicios = [] 
def adicionar_treino(treinos, nome, tipo, data, duracao, intensidade):
    treino = {
        "id": len(treinos) + 1,"nome": nome,"tipo": tipo,"data": data,"duracao": duracao,"intensidade": intensidade
    }
    treinos.append(treino)
    return "Treino adicionado com sucesso!"


def listar_treinos(treinos):
    for i in range(len(treinos)):
      return print(treinos[i])
    
def treino_por_id(treinos, id):
    for i in range(len(treinos)):
        if treinos[i]["id"] == id:
            return treinos[i]
    return("Não existe Treino com esse ID ")
def editar_treino(treinos, id, nome, tipo, data, duracao, intensidade):
    for i in range(len(treinos)):
        if treinos[i]["id"] == id:
            treinos[i]["nome"] = nome
            treinos[i]["tipo"] = tipo
            treinos[i]["data"] = data
            treinos[i]["duracao"] = duracao
            treinos[i]["intensidade"] = intensidade
            return "Treino editado com sucesso! "
    return "Não existe treino com esse ID "



def excluir_treinos(treinos,id):
    for i in range(len(treinos)):
        if treinos[i]["id"] == id:
            del treinos[i]
            return "Treino Excluído com Sucesso! "
    return "Não existe treino com esse ID "


def adicionar_exercicio(exercicios, nome, tempo, distancia, carga, repeticoes):
    exercicio = {
        "id": len(exercicios) + 1,
        "nome": nome,
        "tempo": tempo,
        "distancia": distancia,
        "carga": carga,
        "repeticoes": repeticoes
    }
    exercicios.append(exercicio)
    return "Exercício adicionado com sucesso!"



def listar_exercicio(exercicios):
    for i in range(len(exercicios)):
        return print(exercicios[i])

def exercicio_por_id(exercicios, id):
    for i in range(len(exercicios)):
        if exercicios[i]["id"] == id:
            return exercicios[i]
    return "Não existe Exercício com esse ID "

def editar_exercicio(exercicios, id, nome, tempo, distancia, carga, repeticoes):
    for i in range(len(exercicios)):
        if exercicios[i]["id"] == id:
            exercicios[i]["nome"] = nome
            exercicios[i]["tempo"] = tempo
            exercicios[i]["distancia"] = distancia
            exercicios[i]["carga"] = carga
            exercicios[i]["repeticoes"] = repeticoes
            return "Exercício editado com sucesso!"
    return "Não existe Exercício com esse ID"


def excluir_exercicio(exercicios, id):
    for i in range(len(exercicios)):
        if exercicios[i]["id"] == id:
            del exercicios[i]
            return "Exercício excluído com sucesso!"
    return "Não existe exercício com esse ID."

while True:
    print("----- MENU -----")
    print(" 1- Adicionar Treino   2- Listar treinos   3- Buscar treino Por Id   4- Editar treino   5- Excluir Treino   6- Adicionar Exercício   7- Listar Exercícios   8- Buscar Exercício por ID   9- Editar Exercício   10- Excluir Exercício   0- ENCERRAR ")
    escolha_menu = int(input("Escolha uma opção: "))
    if escolha_menu == 1:
        nome = input("Digite o nome do treino: ")
        tipo = input("Digite o tipo do treino: ")
        while True:
            data = input("Data (Dia/Mes/Ano): ")
            if len(data) == 10 and data[2] == "/" and data[5] == "/":
                break
            else:
                print("Formato inválido")
        duracao = int(input("Digite a duração em minutos: "))
        intensidade = (input("Digite a intensidade do treino: "))
        print(adicionar_treino(treinos, nome, tipo, data, duracao, intensidade))

    elif escolha_menu == 2:
        listar_treinos(treinos)

    elif escolha_menu == 3:
        id = int(input("Digite o id do treino que deseja pesquisar: "))
        print(treino_por_id(treinos, id))

    elif escolha_menu == 4:
        id = int(input("Digite o id do treino que deseja editar: "))
        nome = input("Digite o novo nome do treino: ")
        tipo = input("Digite o novo tipo do treino: ")
        while True:
            data = input("Digite a nova data do treino (Dia/Mês/Ano): ")
            if len(data) == 10 and data[2] == "/" and data[5] == "/":
                break
            else:
                print("Formato inválido")
        duracao = int(input("Digite a nova duração em minutos: "))
        intensidade = input("Digite a nova intensidade (1 a 10): ")
        print(editar_treino(treinos, id, nome, tipo, data, duracao, intensidade))

    elif escolha_menu == 5:
        id = int(input("Digite o id do treino que você deseja excluir: "))
        print(excluir_treinos(treinos, id))

    elif escolha_menu == 0:
        break

    elif escolha_menu == 6:
        nome = input("Digite o nome do exercício: ")
        tempo = int(input("Digite o tempo em minutos: "))
        distancia = int(input("Digite a distância em metros: "))
        carga = int(input("Digite a carga em kg: "))
        repeticoes = int(input("Digite o número repetições: "))
        print(adicionar_exercicio(exercicios, nome, tempo, distancia, carga, repeticoes))

    elif escolha_menu == 7:
        listar_exercicio(exercicios)

    elif escolha_menu == 8:
        id = int(input("Digite o id do exercício que deseja pesquisar: "))
        print(exercicio_por_id(exercicios, id))

    elif escolha_menu == 9:
        id = int(input("Digite o id do exercício que deseja editar: "))
        nome = input("Digite o novo nome do exercício: ")
        tempo = int(input("Digite o novo tempo em segundos: "))
        distancia = int(input("Digite a nova distância em metros: "))
        carga = int(input("Digite a nova carga em kg: "))
        repeticoes = int(input("Digite as novas repetições: "))
        print(editar_exercicio(exercicios, id, nome, tempo, distancia, carga, repeticoes))

    elif escolha_menu == 10:
        id = int(input("Digite o id do exercício que deseja excluir: "))
        print(excluir_exercicio(exercicios, id))

    else:
        print("Opção inválida. Digite outra opção! ")