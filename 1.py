capacity = int(input('Informe a capacidade da memória: '))
unity = input('Informe a unidade de medida (B, KB, MB, GB): ')
unityLowercased = unity.lower()

if unityLowercased == 'b':
  print(f"{capacity} bytes.")
elif unityLowercased == 'kb':
  print(f"{capacity * 1024} bytes.")
elif unityLowercased == 'mb':
  print(f"{capacity * (1024 ** 2)} bytes.")
elif unityLowercased == 'gb':
  print(f"{capacity * (1024 ** 3)} bytes.")
else:
  print('Unidade de medida não encontrada.')