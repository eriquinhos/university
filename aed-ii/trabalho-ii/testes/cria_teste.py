from random import randint

entradas = ['A', 'T', 'C', 'G']

comandos = ['insert', 'insert', 'insert', 'find']

testes = 1000000


with open('input12.txt', 'w') as file:
    file.write(f'{testes}\n')

    for i in range(testes):
        numero_letras = randint(1, 12)

        file.write(f'{comandos[randint(0, 3)]} ')
        for j in range(numero_letras):
            file.write(f'{entradas[randint(0, 3)]}')
            
        file.write('\n')

'''
for num in range(1, 11):
    with open(f'input{num}.txt', 'w') as file:

        file.write(f'{testes}\n')

        for i in range(testes):
            numero_letras = randint(1, 12)

            file.write(f'{comandos[randint(0, 3)]} ')
            for j in range(numero_letras):
                file.write(f'{entradas[randint(0, 3)]}')
            
            file.write('\n')
    testes += 100000
'''