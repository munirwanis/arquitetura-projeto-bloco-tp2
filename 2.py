def prompt():
  try:
    return int(input('Insira a capacidade em GBs do seu Pendrive/HD/Cartão de memória: '))
  except NameError:
    return input(msg)


capacityCount = 0
capacity = prompt()
while capacity >= 0:
  capacityCount = capacityCount + capacity
  capacity = prompt()
print(f'Você possui {capacityCount} GBs no total.')