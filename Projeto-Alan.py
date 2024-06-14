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