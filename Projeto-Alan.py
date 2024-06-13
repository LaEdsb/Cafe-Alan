def adicionar_item(menu):
    categoria = int(input("Escolha a categoria ( 1 - entradas, 2- pratos_principais, 3- sobremesas, 4- bebidas): ").lower())
    if categoria <= 4:
        item = input(f" \nDigite o item que você quer adicionar em {categoria}: ")
        valor_item = float(input(f" \nDigite o valor que você quer adicionar em {item}: "))
        menu[categoria].append({item: valor_item})
        print(f"Item '{item}' adicionado a {categoria}.")
    else:
        print("Categoria não encontrada.")

def alterar_item(menu):
    categoria = int(input("Escolha a categoria ( 1 - entradas, 2- pratos_principais, 3- sobremesas, 4- bebidas): ").lower())
    if categoria <= 4: 
        item = input(f"\n Digite o item que deseja alterar em {categoria}: ")
        valor_item = float(input(f"Digite o valor que você quer adicionar em {item}: "))
        valor_total = {item : valor_item}
        if valor_total in menu.get(categoria, []):
            novo_item = input(f"Qual o novo item no lugar de {item}?")
            novo_valor = float(input(f"Digite o novo valor que você quer adicionar em {novo_item}: "))
            indice = menu[categoria].index(valor_total)
            novo_produto = {novo_item : novo_valor}
            menu[categoria][indice] = novo_produto
            print(f"Item '{item}' modificado por novo item1 {novo_item}.")
        else:
            print('produto não encontrado')
    else:
        print("Categoria não encontrada.")
            

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
        print(' \nVocê escolheu adicionar itens ao cardápio!')
        print('Qual categoria você deseja adicionar o item?')
        print('Qual valor você deseja adicionar ao item?')
        
        adicionar_item(menu)
        print(menu)

    elif opcao == '3':
        print(' \nVocê escolheu alterar itens ao cardápio!')
        print('Qual categoria você deseja alterar o item?')
        print('Qual valor você deseja alterar ao item?')

        alterar_item(menu)
        print(menu)
            
    elif opcao == '99':
        opcao = False
