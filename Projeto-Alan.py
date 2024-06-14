def adicionar_item(menu):
    categoria = int(input("Escolha a categoria ( |1 - entradas\n| 2 - pratos_principais\n| 3 - sobremesas\n| 4 - bebidas): ").lower())
    if categoria <= 4:
        item = input(f" \nDigite o item que você quer adicionar em {categoria}: ")
        valor_item = float(input(f" \nDigite o valor que você quer adicionar em {item}: "))
        menu[categoria].append({f"{item} : {valor_item}"})
        print(f"Item '{item}' adicionado a {categoria}.")
    else:
        print("Categoria não encontrada.")

def remover_item(menu):
    categoria = int(input("Escolha a categoria ( |1 - entradas \n| 2 - pratos_principais \n| 3 - sobremesas \n| 4 - bebidas): ").lower())
    if categoria <= 4:
        item = input(f" \nDigite o item que você quer remover em {categoria}: ")
        # menu[categoria].pop(item)
        menu.pop([{item}])
        print(f"Item '{item}' removido de {categoria}.")
    else:
        print("Categoria não encontrada")
        
def alterar_item(menu):
    categoria = int(input("Escolha a categoria ( | 1 - entradas \n| 2 - pratos_principais \n| 3 - sobremesas \n| 4 - bebidas): ").lower())
    if categoria <= 4:
        item = input(f" \nDigite o item que você quer alterar em {categoria}: ")
        valor_item = float(input(f"Digite o valor de {item}: "))
        valor_total = ({f"{item} : {valor_item}"})
        if valor_total in menu.get(categoria, []):
            novo_item = input(f"Qual o novo item no lugar de {item}?")
            novo_valor = float(input(f"Digite o novo valor que você quer adicionar em {novo_item}: "))
            indice = menu[categoria].index(valor_total)
            novo_produto = ({f'{novo_item} : {novo_valor}'})
            menu[categoria][indice] = novo_produto
            print(f"Item '{item}' modificado por novo item {novo_item}.")
        else:
            print("Item não encontrado")
    else:
        print("Categoria não encontrada.")

def pedido(menu,carrinho):
    categoria = int(input("Escolha a categoria ( | 1 - entradas \n| 2- pratos_principais \n| 3- sobremesas \n| 4 - bebidas): ").lower())
    if categoria <= 5:
        item = input("\nDigite o item que você quer adicionar ao pedido: ")
        if item in menu:
            carrinho.append(item)
            print(f"Item '{item}' adicionado ao carrinho.")
            print(sum(carrinho.values))
            
        else:
            print("Item não encontrado.")
    else:
        print("Categoria não encontrada.")

def buscar_itens(menu):
    busca = int(input("Escolha a categoria ( | 1 - entradas \n| 2 - pratos_principais \n| 3 - sobremesas \n| 4 - bebidas): "))
    if busca == 1:
        print(menu[1])

    elif busca == 2:
        print(menu[2])

    elif busca == 3:
        print(menu[3])

    elif busca == 4:
        print(menu[4])


menu = {
    1 : [],
    2 : [],
    3 : [],
    4 : []
}

print('-'*50)
print("Bem-vindo ao restaurante!")
print('-'*50, '\n')

opcao = True

while opcao:
    opcao = str(input("O que você deseja fazer no cardápio? \n| 1 - Adicionar itens \n| 2 - Remover itens \n| 3 - Alterar itens do cardápio \n| 4 - Buscar itens no cardápio \n| 5 - Listar itens do cardápio \n  Digite (99 para sair): "))

    if opcao == '1':
        print(' \nVocê selecionou a opção adicionar itens ao cardápio!')
        print('Em qual categoria você quer adicionar o item?')
        print('Qual o valor desse novo item?')
        
        adicionar_item(menu)
        print(menu)

    elif opcao == '2':
        print(' \nVocê selecionou a opção remover itens do cardápio!')
        print('De qual categoria você deseja remover um item?')
        remover_item(menu)
        print(menu)

    elif opcao == '3':
        print(' \nVocê selecionou a opção alterar itens do cardápio!')
        print('Qual categoria você deseja alterar o item?')
        print('Qual valor você deseja alterar ao item?')
        alterar_item(menu)
        print(menu)
            
    elif opcao == '4':
        print(' \nVocê selecionou a opção buscar itens no cardápio!')
        print('Por qual categoria você deseja buscar?')
        print(buscar_itens(menu))

    elif opcao == '5':
        print(' \nVocê selecionou a opção para realizar um pedido!')
        print('Qual categoria você deseja buscar?')
        carrinho = []
        pedido(menu,carrinho)
        print(carrinho)
        
        
    elif opcao == '99':
        opcao = False