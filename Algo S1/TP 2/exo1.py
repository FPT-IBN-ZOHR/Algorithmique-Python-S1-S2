#a
n = int(input('entrez un nombre: '))

for i in range(1, 11):
    print(f'n * {i} = {n * i}')
    
#b

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {j * i}')