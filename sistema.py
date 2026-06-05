import os
from datetime import datetime

treinos = []
exercicios = []
competicoes = []

ARQUIVO_DADOS = "HYROX_Planner.txt"


def salvar_dados():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("       HYROX PLANNER — DADOS\n")
        f.write("=" * 40 + "\n\n")

        f.write("TREINOS\n")
        f.write("-" * 40 + "\n")
        if len(treinos) == 0:
            f.write("Nenhum treino cadastrado.\n")
        else:
            for t in treinos:
                f.write(f"ID         : {t['id']}\n")
                f.write(f"Nome       : {t['nome']}\n")
                f.write(f"Tipo       : {t['tipo']}\n")
                f.write(f"Data       : {t['data']}\n")
                f.write(f"Duração    : {t['duracao']} minutos\n")
                f.write(f"Intensidade: {t['intensidade']}\n")
                f.write("-" * 40 + "\n")

        f.write("\nEXERCÍCIOS\n")
        f.write("-" * 40 + "\n")
        if len(exercicios) == 0:
            f.write("Nenhum exercício cadastrado.\n")
        else:
            for e in exercicios:
                f.write(f"ID         : {e['id']}\n")
                f.write(f"Nome       : {e['nome']}\n")
                f.write(f"Tempo      : {e['tempo']} min\n")
                f.write(f"Distância  : {e['distancia']} m\n")
                f.write(f"Carga      : {e['carga']} kg\n")
                f.write(f"Repetições : {e['repeticoes']}\n")
                f.write(f"Data       : {e['data']}\n")
                f.write("-" * 40 + "\n")

        f.write("\nCOMPETIÇÕES\n")
        f.write("-" * 40 + "\n")
        if len(competicoes) == 0:
            f.write("Nenhuma competição cadastrada.\n")
        else:
            for c in competicoes:
                f.write(f"ID         : {c['id']}\n")
                f.write(f"Local      : {c['local']}\n")
                f.write(f"Categoria  : {c['categoria']}\n")
                f.write(f"Data       : {c['data']}\n")
                f.write("-" * 40 + "\n")

        f.write("\n" + "=" * 40 + "\n")
        f.write(f"Atualizado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}\n")
        f.write("=" * 40 + "\n")


def carregar_dados():
    global treinos, exercicios, competicoes
    if not os.path.exists(ARQUIVO_DADOS):
        return

    secao = None
    registro = {}

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.rstrip("\n")

            if linha == "TREINOS":
                secao = "treinos"
                continue
            elif linha == "EXERCÍCIOS":
                secao = "exercicios"
                continue
            elif linha == "COMPETIÇÕES":
                secao = "competicoes"
                continue

            if secao and linha.startswith("ID         :"):
                registro = {}
                registro["id"] = int(linha.split(":", 1)[1].strip())
            elif secao and ":" in linha and not linha.startswith("=") and not linha.startswith("-") and not linha.startswith("Atualizado"):
                chave, valor = linha.split(":", 1)
                chave = chave.strip().lower()
                valor = valor.strip()

                mapa = {
                    "nome": "nome", "tipo": "tipo", "data": "data",
                    "intensidade": "intensidade",
                    "duração": "duracao", "distância": "distancia",
                    "tempo": "tempo", "carga": "carga",
                    "repetições": "repeticoes", "local": "local",
                    "categoria": "categoria"
                }

                for k, v in mapa.items():
                    if chave.startswith(k):
                        if v in ("duracao", "tempo", "carga", "repeticoes", "distancia"):
                            registro[v] = int(valor.split()[0])
                        else:
                            registro[v] = valor
                        break

            elif linha.startswith("-" * 10) and registro:
                if secao == "treinos" and "nome" in registro:
                    treinos.append(registro)
                elif secao == "exercicios" and "nome" in registro:
                    exercicios.append(registro)
                elif secao == "competicoes" and "local" in registro:
                    competicoes.append(registro)
                registro = {}


def adicionar_treino(treinos, nome, tipo, data, duracao, intensidade):
    treino = {
        "id": len(treinos) + 1, "nome": nome, "tipo": tipo, "data": data, "duracao": duracao, "intensidade": intensidade
    }
    treinos.append(treino)
    salvar_dados()
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
    print("Não existe treino com esse ID.")


def editar_treino(treinos, id, nome, tipo, data, duracao, intensidade):
    for i in range(len(treinos)):
        if treinos[i]["id"] == id:
            treinos[i]["nome"] = nome
            treinos[i]["tipo"] = tipo
            treinos[i]["data"] = data
            treinos[i]["duracao"] = duracao
            treinos[i]["intensidade"] = intensidade
            salvar_dados()
            return "Treino editado com sucesso!"
    return "Não existe treino com esse ID."


def excluir_treinos(treinos, id):
    for i in range(len(treinos)):
        if treinos[i]["id"] == id:
            del treinos[i]
            salvar_dados()
            return "Treino excluído com sucesso!"
    return "Não existe treino com esse ID."


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
    salvar_dados()
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
            salvar_dados()
            return "Exercício editado com sucesso!"
    return "Não existe exercício com esse ID."


def excluir_exercicio(exercicios, id):
    for i in range(len(exercicios)):
        if exercicios[i]["id"] == id:
            del exercicios[i]
            salvar_dados()
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
    salvar_dados()
    return "Competição adicionada com sucesso!"


def listar_competicoes(competicoes):
    if len(competicoes) == 0:
        print("Nenhuma competição cadastrada.")
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


def excluir_competicao(competicoes, id):
    for i in range(len(competicoes)):
        if competicoes[i]["id"] == id:
            del competicoes[i]
            salvar_dados()
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

    datas = []
    for t in treinos:
        try:
            datas.append((datetime.strptime(t["data"], "%d/%m/%Y"), t["nome"]))
        except ValueError:
            pass
    if len(datas) > 0:
        datas.sort()
        print(f"\nPrimeiro treino: {datas[0][1]} em {datas[0][0].strftime('%d/%m/%Y')}")
        print(f"Ultimo treino  : {datas[-1][1]} em {datas[-1][0].strftime('%d/%m/%Y')}")

        diferenca_dias = (datas[-1][0] - datas[0][0]).days
        if diferenca_dias > 0:
            semanas = diferenca_dias / 7
            meses   = diferenca_dias / 30
            print(f"\nFrequência:")
            print(f"  Período registrado   : {diferenca_dias} dia(s)")
            print(f"  Média por semana     : {len(datas) / semanas:.1f} treino(s)")
            print(f"  Média por mês        : {len(datas) / meses:.1f} treino(s)")
        else:
            print(f"\nFrequência:")
            print(f"  Todos os treinos foram registrados no mesmo dia.")


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
            print(f"  Data        : {e.get('data', 'não informada')}")
            print(f"  Tempo       : {e['tempo']} min")
            print(f"  Distância   : {e['distancia']} m")
            print(f"  Carga       : {e['carga']} kg")
            print(f"  Repetições  : {e['repeticoes']}")
        else:
            registros_com_data = []
            for e in grupo:
                try:
                    registros_com_data.append((datetime.strptime(e["data"], "%d/%m/%Y"), e))
                except (ValueError, KeyError):
                    pass

            if len(registros_com_data) >= 2:
                registros_com_data.sort()
                primeiro = registros_com_data[0][1]
                ultimo   = registros_com_data[-1][1]
                data_inicio_ex    = registros_com_data[0][0]
                data_fim_ex       = registros_com_data[-1][0]
                diferenca_dias_ex = (data_fim_ex - data_inicio_ex).days
                print(f"  Período     : {diferenca_dias_ex} dia(s) ({data_inicio_ex.strftime('%d/%m/%Y')} até {data_fim_ex.strftime('%d/%m/%Y')})")
            else:
                primeiro = grupo[0]
                ultimo   = grupo[len(grupo) - 1]
                print(f"  Período     : não disponível (data ausente em algum registro)")

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


def menu_treinos():
    while True:
        print("\nTREINOS\n1- Adicionar\n2- Listar\n3- Buscar por ID\n4- Editar\n5- Excluir\n0- Voltar")
        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números")
            continue

        if op == 1:
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

        elif op == 2:
            listar_treinos(treinos)

        elif op == 3:
            try:
                id = int(input("Digite o ID do treino: "))
                treino_por_id(treinos, id)
            except ValueError:
                print("Digite apenas números")

        elif op == 4:
            try:
                id = int(input("Digite o ID do treino que deseja editar: "))
                nome = input("Digite o novo nome do treino: ")
                tipo = input("Digite o novo tipo do treino: ")
                while True:
                    data = input("Digite a nova data (Dia/Mês/Ano): ")
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
                intensidade = input("Digite a nova intensidade: ")
                print(editar_treino(treinos, id, nome, tipo, data, duracao, intensidade))
            except ValueError:
                print("Digite apenas números")

        elif op == 5:
            try:
                id = int(input("Digite o ID do treino que deseja excluir: "))
                print(excluir_treinos(treinos, id))
            except ValueError:
                print("Digite apenas números")

        elif op == 0:
            break
        else:
            print("Opção inválida.")


def menu_exercicios():
    while True:
        print("\nEXERCÍCIOS\n1- Adicionar\n2- Listar\n3- Buscar por ID\n4- Editar\n5- Excluir\n0- Voltar")
        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números")
            continue

        if op == 1:
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
                    repeticoes = int(input("Digite o número de repetições: "))
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

        elif op == 2:
            listar_exercicio(exercicios)

        elif op == 3:
            try:
                id = int(input("Digite o ID do exercício: "))
                exercicio_por_id(exercicios, id)
            except ValueError:
                print("Digite apenas números")

        elif op == 4:
            try:
                id = int(input("Digite o ID do exercício que deseja editar: "))
                nome = input("Digite o novo nome do exercício: ")
                while True:
                    try:
                        tempo = int(input("Digite o novo tempo em minutos: "))
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
                    data = input("Digite a nova data (Dia/Mes/Ano): ")
                    try:
                        datetime.strptime(data, "%d/%m/%Y")
                        break
                    except ValueError:
                        print("Formato inválido")
                print(editar_exercicio(exercicios, id, nome, tempo, distancia, carga, repeticoes, data))
            except ValueError:
                print("Digite apenas números")

        elif op == 5:
            try:
                id = int(input("Digite o ID do exercício que deseja excluir: "))
                print(excluir_exercicio(exercicios, id))
            except ValueError:
                print("Digite apenas números")

        elif op == 0:
            break
        else:
            print("Opção inválida.")


def menu_competicoes():
    while True:
        print("\nCOMPETIÇÕES\n1- Adicionar\n2- Listar\n3- Buscar por ID\n4- Excluir\n0- Voltar")
        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números")
            continue

        if op == 1:
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

        elif op == 2:
            listar_competicoes(competicoes)

        elif op == 3:
            try:
                id = int(input("Digite o ID da competição: "))
                competicao_por_id(competicoes, id)
            except ValueError:
                print("Digite apenas números")

        elif op == 4:
            try:
                id = int(input("Digite o ID da competição que deseja excluir: "))
                print(excluir_competicao(competicoes, id))
            except ValueError:
                print("Digite apenas números")

        elif op == 0:
            break
        else:
            print("Opção inválida.")


def menu_resumo():
    while True:
        print("\nRESUMO\n1- Resumo completo\n2- Frequência de treinos\n3- Evolução dos exercícios\n4- Resumo de competições\n0- Voltar")
        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números")
            continue

        if op == 1:
            resumo_completo(treinos, exercicios, competicoes)
        elif op == 2:
            resumo_frequencia_treinos(treinos)
        elif op == 3:
            resumo_evolucao_exercicios(exercicios)
        elif op == 4:
            resumo_competicoes(competicoes)
        elif op == 0:
            break
        else:
            print("Opção inválida.")


carregar_dados()

while True:
    print("\nMENU PRINCIPAL\n1- Treinos\n2- Exercícios\n3- Competições\n4- Resumo de Evolução\n0- Encerrar")
    try:
        escolha_menu = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if escolha_menu == 1:
        menu_treinos()
    elif escolha_menu == 2:
        menu_exercicios()
    elif escolha_menu == 3:
        menu_competicoes()
    elif escolha_menu == 4:
        menu_resumo()
    elif escolha_menu == 0:
        print("Encerrando o programa. Dados salvos.")
        salvar_dados()
        break
    else:
        print("Opção inválida. Digite outra opção.")
