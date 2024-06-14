def adicionar_item(menu):
  categoria = int(input("Escolha a categoria:\n| 1 - entradas \n| 2 - pratos principais \n| 3 - sobremesas \n| 4 - bebidas \n "))
  if categoria in menu:
      item = input(f"\nDigite o item que você quer adicionar em {categoria}: ")
      valor_item = float(input(f"\nDigite o valor que você quer adicionar em {item}: "))
      menu[categoria].append({item: valor_item})
      print(f"Item '{item}' adicionado à categoria {categoria}.")
  else:
      print("Categoria não encontrada.")

def remover_item(menu):
  categoria = int(input("Escolha a categoria: \n| 1 - entradas \n| 2 - pratos principais \n| 3 - sobremesas \n| 4 - bebidas \n "))
  if categoria in menu:
      item = input(f"\nDigite o item que você quer remover em {categoria}: ")
      for produto in menu[categoria]:
          if item in produto:
              menu[categoria].remove(produto)
              print(f"Item '{item}' removido da categoria {categoria}.")
              break
      else:
          print("Item não encontrado.")
  else:
      print("Categoria não encontrada.")
      
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