import os
os.system("cls")
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


def adicionar_exercicio(exercicios, nome, tempo, distancia, carga, repeticoes, data):
    exercicio = {
        "id": len(exercicios) + 1,
        "nome": nome,
        "tempo": tempo,
        "distancia": distancia,
        "carga": carga,
        "repeticoes": repeticoes,
        "data": data
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
            print(f"Data       : {e['data']}")


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
            print(f"Data       : {e['data']}")
            print("-" * 40)
            return
    print("Não existe exercício com esse ID.")


def editar_exercicio(exercicios, id, nome, tempo, distancia, carga, repeticoes, data):
    for i in range(len(exercicios)):
        if exercicios[i]["id"] == id:
            exercicios[i]["nome"] = nome
            exercicios[i]["tempo"] = tempo
            exercicios[i]["distancia"] = distancia
            exercicios[i]["carga"] = carga
            exercicios[i]["repeticoes"] = repeticoes
            exercicios[i]["data"] = data
            return "Exercício editado com sucesso!"
    return "Não existe Exercício com esse ID"


def excluir_exercicio(exercicios, id):
    for i in range(len(exercicios)):
        if exercicios[i]["id"] == id:
            del exercicios[i]
            return "Exercício excluído com sucesso!"
    return "Não existe exercício com esse ID."


def cadastrar_competicao(competicoes, data, local, categoria):
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
            print(f"ID         : {t['id']}")
            print(f"Local      : {t['local']}")
            print(f"Categoria  : {t['categoria']}")
            print(f"Data       : {t['data']}")


def competicao_por_id(competicoes, id):
    for i in range(len(competicoes)):
        if competicoes[i]["id"] == id:
            e = competicoes[i]
            print("-" * 40)
            print(f"ID         : {e['id']}")
            print(f"Local      : {e['local']}")
            print(f"Categoria  : {e['categoria']}")
            print(f"Data       : {e['data']}")
            print("-" * 40)
            return
    print("Não existe competição com esse ID.")


def resumo_evolucao(treinos, exercicios):
    if len(treinos) == 0 and len(exercicios) == 0:
        print("Nenhum dado registrado.")
        return

    print("===== RESUMO DE EVOLUÇÃO =====")

    if len(treinos) > 0:
        print(f"Total de treinos: {len(treinos)}")

        tipos = {}
        for t in treinos:
            if t["tipo"] in tipos:
                tipos[t["tipo"]] += 1
            else:
                tipos[t["tipo"]] = 1
        for tipo, quantidade in tipos.items():
            print(f"{tipo}: {quantidade} treino(s)")

        total_duracao = 0
        for t in treinos:
            total_duracao += t["duracao"]
        print(f"Duração média dos treinos: {total_duracao / len(treinos):.1f} minutos")

        datas = []
        for t in treinos:
            try:
                datas.append((datetime.strptime(t["data"], "%d/%m/%Y"), t["nome"]))
            except ValueError:
                pass
        if len(datas) > 0:
            datas.sort()
            print(f"Primeiro treino: {datas[0][1]} em {datas[0][0].strftime('%d/%m/%Y')}")
            print(f"Ultimo treino: {datas[-1][1]} em {datas[-1][0].strftime('%d/%m/%Y')}")

            data_inicio = datas[0][0]
            data_fim = datas[-1][0]
            diferenca_dias = (data_fim - data_inicio).days

            if diferenca_dias > 0:
                semanas = diferenca_dias / 7
                meses = diferenca_dias / 30

                frequencia_semanal = len(datas) / semanas
                frequencia_mensal = len(datas) / meses

                print(f"\nFrequência de treinos:")
                print(f"  Período registrado   : {diferenca_dias} dia(s)")
                print(f"  Média por semana     : {frequencia_semanal:.1f} treino(s)")
                print(f"  Média por mês        : {frequencia_mensal:.1f} treino(s)")
            else:
                print(f"\nFrequência de treinos:")
                print(f"  Todos os treinos foram registrados no mesmo dia.")

    if len(exercicios) > 0:
        grupos = {}
        for e in exercicios:
            if e["nome"] not in grupos:
                grupos[e["nome"]] = []
            try:
                grupos[e["nome"]].append((datetime.strptime(e["data"], "%d/%m/%Y"), e))
            except ValueError:
                pass

        print("\nEvolucao por exercicio:")
        for nome, registros in grupos.items():
            if len(registros) < 2:
                continue
            registros.sort()
            primeiro = registros[0][1]
            ultimo = registros[-1][1]

            print(f"\n  {nome}")

            data_inicio_ex = registros[0][0]
            data_fim_ex = registros[-1][0]
            diferenca_dias_ex = (data_fim_ex - data_inicio_ex).days
            print(f"  Período: {diferenca_dias_ex} dia(s) ({data_inicio_ex.strftime('%d/%m/%Y')} até {data_fim_ex.strftime('%d/%m/%Y')})")

            diff_carga = ultimo["carga"] - primeiro["carga"]
            if diff_carga > 0:
                print(f"  Carga: {primeiro['carga']} kg -> {ultimo['carga']} kg (+{diff_carga} kg)")
            elif diff_carga < 0:
                print(f"  Carga: {primeiro['carga']} kg -> {ultimo['carga']} kg ({diff_carga} kg)")
            else:
                print(f"  Carga: {primeiro['carga']} kg (sem alteracao)")

            diff_tempo = ultimo["tempo"] - primeiro["tempo"]
            if diff_tempo < 0:
                print(f"  Tempo: {primeiro['tempo']} min -> {ultimo['tempo']} min (melhorou {abs(diff_tempo)} min)")
            elif diff_tempo > 0:
                print(f"  Tempo: {primeiro['tempo']} min -> {ultimo['tempo']} min (+{diff_tempo} min)")
            else:
                print(f"  Tempo: {primeiro['tempo']} min (sem alteracao)")

            diff_rep = ultimo["repeticoes"] - primeiro["repeticoes"]
            if diff_rep > 0:
                print(f"  Repeticoes: {primeiro['repeticoes']} -> {ultimo['repeticoes']} (+{diff_rep})")
            elif diff_rep < 0:
                print(f"  Repeticoes: {primeiro['repeticoes']} -> {ultimo['repeticoes']} ({diff_rep})")
            else:
                print(f"  Repeticoes: {primeiro['repeticoes']} (sem alteracao)")

            diff_dist = ultimo["distancia"] - primeiro["distancia"]
            if diff_dist > 0:
                print(f"  Distancia: {primeiro['distancia']} m -> {ultimo['distancia']} m (+{diff_dist} m)")
            elif diff_dist < 0:
                print(f"  Distancia: {primeiro['distancia']} m -> {ultimo['distancia']} m ({diff_dist} m)")
            else:
                print(f"  Distancia: {primeiro['distancia']} m (sem alteracao)")
            print()


while True:
    print("1- Adicionar Treino\n2- Listar treinos\n3- Buscar treino Por Id\n4- Editar treino\n5- Excluir Treino\n6- Adicionar Exercício\n7- Listar Exercícios\n8- Buscar Exercício por ID\n9- Editar Exercício\n10- Excluir Exercício\n11- Adicionar Competição\n12- Listar Competições\n13- Buscar Competição por ID\n14- Resumo de Evolução\n0- ENCERRAR ")
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
        while True:
            data = input("Data (Dia/Mes/Ano): ")
            try:
                datetime.strptime(data, "%d/%m/%Y")
                break
            except ValueError:
                print("Formato inválido")
        print(adicionar_exercicio(exercicios, nome, tempo, distancia, carga, repeticoes, data))

    elif escolha_menu == 7:
        listar_exercicio(exercicios)

    elif escolha_menu == 8:
        try:
            id = int(input("Digite o id do exercício que deseja pesquisar: "))
            print(exercicio_por_id(exercicios, id))
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
            while True:
                data = input("Digite a nova data do exercicio (Dia/Mes/Ano): ")
                try:
                    datetime.strptime(data, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Formato inválido")
            print(editar_exercicio(exercicios, id, nome, tempo, distancia, carga, repeticoes, data))
        except ValueError:
            print("Digite apenas números")

    elif escolha_menu == 10:
        try:
            id = int(input("Digite o id do exercício que deseja excluir: "))
            print(excluir_exercicio(exercicios, id))
        except ValueError:
            print("Digite apenas números")

    elif escolha_menu == 11:
        local = input("Digite o local da competição: ")
        categoria = input("Digite a categoria da competição: ")
        while True:
            data = input("Digite a data da competição (Dia/Mês/Ano): ")
            try:
                datetime.strptime(data, "%d/%m/%Y")
                break
            except ValueError:
                print("Formato inválido. Tente novamente.")
        print(cadastrar_competicao(competicoes, data, local, categoria))

    elif escolha_menu == 12:
        listar_competicoes(competicoes)

    elif escolha_menu == 13:
        try:
            id = int(input("Digite o ID da competição: "))
            competicao_por_id(competicoes, id)
        except ValueError:
            print("Digite apenas números")

    elif escolha_menu == 14:
        resumo_evolucao(treinos, exercicios)

    else:
        print("Opção inválida. Digite outra opção.")
