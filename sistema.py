import os
from datetime import datetime
treinos = []
exercicios = []
competicoes = []

def adicionar_treino(treinos, nome, tipo, data, duracao, intensidade):
    treino = {
        "id": len(treinos) + 1, "nome": nome, "tipo": tipo, "data": data, "duracao": duracao, "intensidade": intensidade
    }
    treinos.append(treino)
    return "Treino adicionado com sucesso!"


def listar_treinos(treinos):
    if len(treinos) == 0:
        print("Nenhum treino cadastrado")
    else:
        for t in treinos:
            print(f"ID         : {t['id']}")
            print(f"Nome       : {t['nome']}")
            print(f"Tipo       : {t['tipo']}")
            print(f"Data       : {t['data']}")
            print(f"Duração    : {t['duracao']} minutos")
            print(f"Intensidade: {t['intensidade']}")


def treino_por_id(treinos, id):
    for i in range(len(treinos)):
        if treinos[i]["id"] == id:
            t = treinos[i]
            print(f"ID         : {t['id']}")
            print(f"Nome       : {t['nome']}")
            print(f"Tipo       : {t['tipo']}")
            print(f"Data       : {t['data']}")
            print(f"Duração    : {t['duracao']} minutos")
            print(f"Intensidade: {t['intensidade']}")
            return
    print("não existe Treino com esse ID ")


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


def excluir_treinos(treinos, id):
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
    if len(exercicios) == 0:
        print("Nenhum exercício cadastrado.")
    else:
        for e in exercicios:
            print(f"ID         : {e['id']}")
            print(f"Nome       : {e['nome']}")
            print(f"Tempo      : {e['tempo']}")
            print(f"Distância  : {e['distancia']}")
            print(f"Carga      : {e['carga']}")
            print(f"Repetições : {e['repeticoes']}")


def exercicio_por_id(exercicios, id):
    for i in range(len(exercicios)):
        if exercicios[i]["id"] == id:
            e = exercicios[i]
            print("-" * 40)
            print(f"ID         : {e['id']}")
            print(f"Nome       : {e['nome']}")
            print(f"Tempo      : {e['tempo']}")
            print(f"Distância  : {e['distancia']}")
            print(f"Carga      : {e['carga']}")
            print(f"Repetições : {e['repeticoes']}")
            print("-" * 40)
            return
    print("Não existe exercício com esse ID.")


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


def cadastrar_competicao(competicoes, competicao, data, local, categoria):
    competicao = {
        "id": len(competicoes) + 1,
        "local": local,
        "categoria": categoria,
        "data": data
    }
    competicoes.append(competicao)
    return "Competição adicionada com sucesso!"


def listar_competicoes(competicoes):
    if len(competicoes) == 0:
        print("Nenhuma competição cadastrada")
    else:
        for t in competicoes:
            print(f"id         : {t['id']}")
            print(f"local      : {t['local']}")
            print(f"categoria  : {t['categoria']}")
            print(f"Data       : {t['data']}")


def competicao_por_id(competicoes, id):
    for i in range(len(competicoes)):
        if competicoes[i]["id"] == id:
            e = competicoes[i]
            print("-" * 40)
            print(f"ID         : {e['id']}")
            print(f"local       : {e['local']}")
            print(f"categoria   : {e['categoria']}")
            print(f"data        : {e['data']}")
            print("-" * 40)
            return
    print("Não existe competição com esse ID. ")


# CORRIGIDO: era "range(len(exercicios))" — lista errada
def excluir_competicao(competicoes, id):
    for i in range(len(competicoes)):
        if competicoes[i]["id"] == id:
            del competicoes[i]
            return "Competição excluída com sucesso!"
    return "Não existe competição com esse ID."


while True:
    print("1- Adicionar Treino\n2- Listar treinos\n3- Buscar treino Por Id\n4- Editar treino\n5- Excluir Treino\n6- Adicionar Exercício\n7- Listar Exercícios\n8- Buscar Exercício por ID\n9- Editar Exercício\n10- Excluir Exercício\n11- Adicionar Competição\n12- Listar Competições\n13- Buscar Competição por ID\n14- Excluir Competição\n0- ENCERRAR ")

    try:
        escolha_menu = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        input()
        continue

    if escolha_menu == 1:
        nome = input("Digite o nome do treino: ")
        tipo = input("Digite o tipo do treino: ")
        while True:
            data = input("Data (Dia/Mes/Ano): ")
            try:
                datetime.strptime(data, "%d/%m/%Y")
                break
            except ValueError:
                print("Formato inválido")
        while True:
            try:
                duracao = int(input("Digite a duração em minutos: "))
                break
            except ValueError:
                print("Digite apenas números")
        intensidade = input("Digite a intensidade do treino: ")
        print(adicionar_treino(treinos, nome, tipo, data, duracao, intensidade))

    elif escolha_menu == 2:
        listar_treinos(treinos)

    elif escolha_menu == 3:
        try:
            id = int(input("Digite o id do treino que deseja pesquisar: "))
            treino_por_id(treinos, id)
        except ValueError:
            print("Digite apenas números")

    elif escolha_menu == 4:
        try:
            id = int(input("Digite o id do treino que deseja editar: "))
            nome = input("Digite o novo nome do treino: ")
            tipo = input("Digite o novo tipo do treino: ")
            while True:
                data = input("Digite a nova data do treino (Dia/Mês/Ano): ")
                try:
                    datetime.strptime(data, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Formato inválido")
            while True:
                try:
                    duracao = int(input("Digite a nova duração em minutos: "))
                    break
                except ValueError:
                    print("Digite apenas números")
            intensidade = input("Digite a nova intensidade : ")
            print(editar_treino(treinos, id, nome, tipo, data, duracao, intensidade))
        except ValueError:
            print("Digite apenas números")

    elif escolha_menu == 5:
        try:
            id = int(input("Digite o id do treino que você deseja excluir: "))
            print(excluir_treinos(treinos, id))
        except ValueError:
            print("Digite apenas números")

    elif escolha_menu == 0:
        break

    elif escolha_menu == 6:
        nome = input("Digite o nome do exercício: ")
        while True:
            try:
                tempo = int(input("Digite o tempo em minutos: "))
                break
            except ValueError:
                print("Digite apenas números")
        while True:
            try:
                distancia = int(input("Digite a distância em metros: "))
                break
            except ValueError:
                print("Digite apenas números")
        while True:
            try:
                carga = int(input("Digite a carga em kg: "))
                break
            except ValueError:
                print("Digite apenas números")
        while True:
            try:
                repeticoes = int(input("Digite o número repetições: "))
                break
            except ValueError:
                print("Digite apenas números")
        print(adicionar_exercicio(exercicios, nome, tempo, distancia, carga, repeticoes))

    elif escolha_menu == 7:
        listar_exercicio(exercicios)

    elif escolha_menu == 8:
        try:
            id = int(input("Digite o id do exercício que deseja pesquisar: "))
            exercicio_por_id(exercicios, id)
        except ValueError:
            print("Digite apenas números")

    elif escolha_menu == 9:
        try:
            id = int(input("Digite o id do exercício que deseja editar: "))
            nome = input("Digite o novo nome do exercício: ")
            while True:
                try:
                    tempo = int(input("Digite o novo tempo em segundos: "))
                    break
                except ValueError:
                    print("Digite apenas números")
            while True:
                try:
                    distancia = int(input("Digite a nova distância em metros: "))
                    break
                except ValueError:
                    print("Digite apenas números")
            while True:
                try:
                    carga = int(input("Digite a nova carga em kg: "))
                    break
                except ValueError:
                    print("Digite apenas números")
            while True:
                try:
                    repeticoes = int(input("Digite as novas repetições: "))
                    break
                except ValueError:
                    print("Digite apenas números")
            print(editar_exercicio(exercicios, id, nome, tempo, distancia, carga, repeticoes))
        except ValueError:
            print("Digite apenas números")

    elif escolha_menu == 10:
        try:
            id = int(input("Digite o id do exercício que deseja excluir: "))
            print(excluir_exercicio(exercicios, id))
        except ValueError:
            print("Digite apenas números")

    elif escolha_menu == 11:
        local = input("Digite o Local da competição: ")
        categoria = input("Digite a categoria da competição: ")
        while True:
            data = input("Digite a data da competição (Dia/Mês/Ano): ")
            try:
                datetime.strptime(data, "%d/%m/%Y")
                break
            except ValueError:
                print("Formato inválido. Tente novamente.")
        print(cadastrar_competicao(competicoes, None, data, local, categoria))

    elif escolha_menu == 12:
        listar_competicoes(competicoes)

    elif escolha_menu == 13:
        try:
            id = int(input("Digite o ID da competição: "))
            competicao_por_id(competicoes, id)
        except ValueError:
            print("Digite apenas números")
            
    elif escolha_menu == 14:
        try:
            id = int(input("Digite o ID da competição para excluir: "))
            print(excluir_competicao(competicoes, id))
        except ValueError:
            print("Digite apenas números")

    else:
        print("Opção inválida. Digite outra opção.")