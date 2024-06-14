configuracoes = {
'nome_restaurante': 'Alan Café',
'porcentagem_garcom': 2.0
}

def adicionar_item(menu):
    categoria = int(input("Escolha a categoria:\n| 1 - entradas \n| 2 - pratos principais \n| 3 - sobremesas \n| 4 - bebidas \n "))
    if categoria in menu:
        item = input(f"\nDigite o item que você quer adicionar em {categoria}: ").lower()
        valor_item = float(input(f"\nDigite o valor que você quer adicionar em {item}: "))
        menu[categoria].append({item: valor_item})
        print(f"Item '{item}' adicionado à categoria {categoria}.")
    else:
        print("Categoria não encontrada.")

def remover_item(menu):
    categoria = int(input("Escolha a categoria: \n| 1 - entradas \n| 2 - pratos principais \n| 3 - sobremesas \n| 4 - bebidas \n "))
    if categoria in menu:
        item = input(f"\nDigite o item que você quer remover em {categoria}: ").lower()
        for produto in menu[categoria]:
            if item in produto:
                menu[categoria].remove(produto)
                print(f"Item '{item}' removido da categoria {categoria}.")
                break
        else:
            print("Item não encontrado.")
    else:
        print("Categoria não encontrada.")


def alterar_item(menu):
    categoria = int(input("Escolha a categoria: \n| 1 - entradas \n| 2 - pratos principais \n| 3 - sobremesas \n| 4 - bebidas \n "))
    if categoria in menu:
            item_antigo = input(f"\nDigite o item que você quer alterar em {categoria}: ").lower()
            for produto in menu[categoria]:
                if item_antigo in produto:
                    indice = menu[categoria].index(produto)
                    item_novo = input(f"Digite o novo nome para {item_antigo}: ")
                    valor_novo = float(input(f"Digite o novo valor para {item_novo}: "))
                    menu[categoria][indice] = {item_novo: valor_novo}
                    print(f"Item '{item_antigo}' alterado para '{item_novo}' com o valor de R${valor_novo:.2f} na categoria {categoria}.")
                    break
            else:
                print("Item não encontrado.")
    else:
        print("Categoria não encontrada.")


def buscar_itens(menu):
    busca = int(input("Escolha a categoria: \n | 1 - entradas \n| 2 - pratos principais \n| 3 - sobremesas \n| 4 - bebidas \n "))
    if busca in menu:
        print(menu[busca])
    else:
        print("Categoria não encontrada.")

def listar_itens(menu):
    for categoria, itens in menu.items():
        print(f"{categoria}:")
        for item in itens:
            for nome, valor in item.items():
                print(f" - {nome}: R${valor:.2f}")
            print()

def pedido(menu, carrinho):
    categoria = int(input("Escolha a categoria: \n| 1 - entradas \n| 2 - pratos principais \n| 3 - sobremesas \n| 4 - bebidas \n "))
    if categoria in menu:
        item = input("\nDigite o item que você quer adicionar ao pedido: ").lower()
        for produto in menu[categoria]:
            if item in produto:
                carrinho.append(produto)
                print(f"Item '{item}' adicionado ao carrinho.")
                break
        else:
                print("Item não encontrado.")
    else:
        print("Categoria não encontrada.")

def calcular_total(carrinho):
    total = sum(item[next(iter(item))] for item in carrinho)
    total_com_garcom = total + (total * configuracoes['porcentagem_garcom'] / 100)
    return total_com_garcom

menu = {
1: [],
2: [],
3: [],
4: []
}

print('-' * 50)
print(f"Bem-vindo ao {configuracoes['nome_restaurante']}!")
print('-' * 50, '\n')

opcao = True
carrinho = []

while opcao:
    opcao = input("O que você deseja fazer no cardápio? \n| 1 - Adicionar itens \n| 2 - Remover itens \n| 3 - Alterar itens do cardápio \n| 4 - Buscar itens no cardápio \n| 5 - Listar itens do cardápio \n| 6 - Fazer um pedido \n| 99 - Sair \n ")

    if opcao == '1':
        print(' \nVocê selecionou a opção adicionar itens ao cardápio!')
        print('Em qual categoria você quer adicionar o item?')
        print('Qual o valor desse novo item')

        adicionar_item(menu)

    elif opcao == '2':
        print('\nVocê selecionou a opção remover itens do cardápio!')
        print('De qual categoria você deseja remover um item? ')
        remover_item(menu)


    elif opcao == '3':
        print('\nVocê selecionou a opção alterar itens do cardápio!')
        print('Qual categoria você deseja alterar o item?')
        print('Qual valor você deseja alterar ao item?')
        alterar_item(menu)

    elif opcao == '4':
        print('\nVocê selecionou a opção buscar itens no cardápio!')
        print('Por qual categoria você deseja buscar?')
        print(buscar_itens(menu))

    elif opcao == '5':
        print('\nVocê escolheu listar os itens do cardápio!')
        print('Aqui está o cardápio completo:')
        listar_itens(menu)

    elif opcao == '6':
        pedido(menu, carrinho)
        total_a_pagar = calcular_total(carrinho)
        print(f"Total a pagar: R${total_a_pagar:.2f}")

    elif opcao == '99':
        opcao = False

    for categoria, itens in menu.items():
        print(f"{categoria}:")
        for item in itens:
            for nome, valor in item.items():
                print(f" - {nome}: R${valor:.2f}")
        print()

with open("alterações.txt","a") as arquivo:
    arquivo.write("Atualização feita: \n")