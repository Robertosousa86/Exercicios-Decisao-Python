print('A letra que você digitar é uma consuante ou vogal? ')
vogais = ['a', 'e', 'i', 'o', 'u']
letra = input('Digite uma letra: ')
if letra in vogais:
    print(letra, 'é uma vogal')
else:
    print(letra, 'é uma consoante')
print(type(vogais))
