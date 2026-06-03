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


def excluir_competicao(competicoes, id):
    for i in range(len(competicoes)):
        if competicoes[i]["id"] == id:
            del competicoes[i]
            return "Competição excluída com sucesso!"
    return "Não existe competição com esse ID."


def resumo_frequencia_treinos(treinos):
    print("\nFREQUÊNCIA DE TREINOS\n")
    if len(treinos) == 0:
        print("Nenhum treino cadastrado.")
        return

    total = len(treinos)
    print(f"Total de treinos realizados: {total}")

    tipos = {}
    for i in range(len(treinos)):
        tipo = treinos[i]["tipo"]
        if tipo in tipos:
            tipos[tipo] += 1
        else:
            tipos[tipo] = 1

    print("\nTreinos por tipo:")
    for tipo in tipos:
        print(f"  {tipo}: {tipos[tipo]} treino(s)")

    duracao_total = 0
    for i in range(len(treinos)):
        duracao_total += treinos[i]["duracao"]
    duracao_media = duracao_total / total

    print(f"\nDuração total: {duracao_total} minutos")
    print(f"Duração média por treino: {duracao_media:.1f} minutos")


def resumo_evolucao_exercicios(exercicios):
    print("\nEVOLUÇÃO DOS EXERCÍCIOS\n")
    if len(exercicios) == 0:
        print("Nenhum exercício cadastrado.")
        return

    agrupados = {}
    for i in range(len(exercicios)):
        nome = exercicios[i]["nome"]
        if nome not in agrupados:
            agrupados[nome] = []
        agrupados[nome].append(exercicios[i])

    for nome in agrupados:
        grupo = agrupados[nome]
        print(f"\nExercício: {nome} ({len(grupo)} registro(s))")

        if len(grupo) == 1:
            e = grupo[0]
            print(f"  Tempo       : {e['tempo']} min")
            print(f"  Distância   : {e['distancia']} m")
            print(f"  Carga       : {e['carga']} kg")
            print(f"  Repetições  : {e['repeticoes']}")
        else:
            primeiro = grupo[0]
            ultimo = grupo[len(grupo) - 1]

            var_tempo = ultimo["tempo"] - primeiro["tempo"]
            sinal_tempo = "↓" if var_tempo < 0 else "↑" if var_tempo > 0 else "="
            print(f"  Tempo       : {primeiro['tempo']} min → {ultimo['tempo']} min  {sinal_tempo} ({var_tempo:+} min)")

            var_dist = ultimo["distancia"] - primeiro["distancia"]
            sinal_dist = "↑" if var_dist > 0 else "↓" if var_dist < 0 else "="
            print(f"  Distância   : {primeiro['distancia']} m → {ultimo['distancia']} m  {sinal_dist} ({var_dist:+} m)")

            var_carga = ultimo["carga"] - primeiro["carga"]
            sinal_carga = "↑" if var_carga > 0 else "↓" if var_carga < 0 else "="
            print(f"  Carga       : {primeiro['carga']} kg → {ultimo['carga']} kg  {sinal_carga} ({var_carga:+} kg)")

            var_rep = ultimo["repeticoes"] - primeiro["repeticoes"]
            sinal_rep = "↑" if var_rep > 0 else "↓" if var_rep < 0 else "="
            print(f"  Repetições  : {primeiro['repeticoes']} → {ultimo['repeticoes']}  {sinal_rep} ({var_rep:+})")

            melhor_carga = grupo[0]["carga"]
            for i in range(len(grupo)):
                if grupo[i]["carga"] > melhor_carga:
                    melhor_carga = grupo[i]["carga"]
            print(f"  Maior carga registrada: {melhor_carga} kg")


def resumo_competicoes(competicoes):
    print("\nRESUMO DE COMPETIÇÕES\n")
    if len(competicoes) == 0:
        print("Nenhuma competição cadastrada.")
        return

    print(f"Total de competições: {len(competicoes)}")

    categorias = {}
    for i in range(len(competicoes)):
        cat = competicoes[i]["categoria"]
        if cat in categorias:
            categorias[cat] += 1
        else:
            categorias[cat] = 1

    print("\nCompetições por categoria:")
    for cat in categorias:
        print(f"  {cat}: {categorias[cat]} competição(ões)")

    print("\nLocais:")
    for i in range(len(competicoes)):
        print(f"  - {competicoes[i]['local']} ({competicoes[i]['data']})")


def resumo_completo(treinos, exercicios, competicoes):
    print("\nRESUMO DE EVOLUÇÃO DO ATLETA")
    resumo_frequencia_treinos(treinos)
    resumo_evolucao_exercicios(exercicios)
    resumo_competicoes(competicoes)


while True:
    print("1- Adicionar Treino\n2- Listar treinos\n3- Buscar treino Por Id\n4- Editar treino\n5- Excluir Treino\n6- Adicionar Exercício\n7- Listar Exercícios\n8- Buscar Exercício por ID\n9- Editar Exercício\n10- Excluir Exercício\n11- Adicionar Competição\n12- Listar Competições\n13- Buscar Competição por ID\n14- Excluir Competição\n15- Resumo de Evolução do Atleta\n0- ENCERRAR ")

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

    elif escolha_menu == 15:
        print("Deseja ver qual parte do resumo?")
        print("1- Resumo completo\n2- Frequência de treinos\n3- Evolução dos exercícios\n4- Resumo de competições")
        try:
            escolha_resumo = int(input("Escolha uma opção: "))
            if escolha_resumo == 1:
                resumo_completo(treinos, exercicios, competicoes)
            elif escolha_resumo == 2:
                resumo_frequencia_treinos(treinos)
            elif escolha_resumo == 3:
                resumo_evolucao_exercicios(exercicios)
            elif escolha_resumo == 4:
                resumo_competicoes(competicoes)
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite apenas números")

    else:
        print("Opção inválida. Digite outra opção.")