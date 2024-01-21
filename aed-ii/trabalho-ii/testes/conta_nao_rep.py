sem_rep = set()


with open('input10.txt', 'r') as file:
    testes = int(file.readline())
    for i in range(testes):
        comando = file.readline().split()
        if comando[0] == 'find':
            sem_rep.add(comando[1])

print(len(sem_rep))
