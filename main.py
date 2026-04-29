pecas_aprovadas = []
pecas_reprovadas = []
caixas = []
caixa_atual = []

def avaliar_peca(peso, cor, comprimento):
    motivos = []

    if not (95 <= peso <= 105):
        motivos.append("Peso fora do padrão")
    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida")
    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do padrão")

    if len(motivos) == 0:
        return True, []
    else:
        return False, motivos

def cadastrar_peca():
    id_peca = input("ID da peça: ")
    peso = float(input("Peso: "))
    cor = input("Cor: ")
    comprimento = float(input("Comprimento: "))

    aprovado, motivos = avaliar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    if aprovado:
        pecas_aprovadas.append(peca)
        adicionar_caixa(peca)
        print("Peça APROVADA")
    else:
        peca["motivos"] = motivos
        pecas_reprovadas.append(peca)
        print("Peça REPROVADA:", motivos)

def adicionar_caixa(peca):
    global caixa_atual
    caixa_atual.append(peca)

    if len(caixa_atual) == 10:
        caixas.append(caixa_atual)
        caixa_atual = []
        print("Caixa fechada!")

def listar_pecas():
    print("\nAPROVADAS:")
    for p in pecas_aprovadas:
        print(p)

    print("\nREPROVADAS:")
    for p in pecas_reprovadas:
        print(p)

def remover_peca():
    id_peca = input("Digite o ID para remover: ")

    for lista in [pecas_aprovadas, pecas_reprovadas]:
        for p in lista:
            if p["id"] == id_peca:
                lista.remove(p)
                print("Peça removida!")
                return

    print("Peça não encontrada")

def listar_caixas():
    for i, caixa in enumerate(caixas):
        print(f"Caixa {i+1}: {len(caixa)} peças")

def relatorio():
    print("\nRELATÓRIO FINAL")
    print("Aprovadas:", len(pecas_aprovadas))
    print("Reprovadas:", len(pecas_reprovadas))
    print("Caixas usadas:", len(caixas))

    print("\nMotivos de reprovação:")
    for p in pecas_reprovadas:
        print(p["id"], "->", p["motivos"])

def menu():
    while True:
        print("\n1. Cadastrar peça")
        print("2. Listar peças")
        print("3. Remover peça")
        print("4. Listar caixas")
        print("5. Relatório")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            relatorio()
        elif opcao == "0":
            break
        else:
            print("Opção inválida")

menu()
