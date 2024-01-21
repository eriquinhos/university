inserts = finds = 0

with open('input12.txt', 'r') as file:
    testes = int(file.readline())
    for i in range(testes):
        comando = file.readline().split()
        if comando[0] == 'insert':
            inserts += 1
        else:
            finds += 1

print(f'inserts: {inserts}\nfinds: {finds}')