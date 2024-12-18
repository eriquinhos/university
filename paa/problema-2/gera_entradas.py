import random

# Número de entradas
num_entradas = 100000

# Limites das coordenadas
x_min, x_max = -100.0, 100.0
y_min, y_max = -100.0, 100.0

# Nome do arquivo de saída
file_name = "entradas_100k.txt"

# Gerar entradas e salvar no arquivo
with open(file_name, "w") as f:
    f.write(f"{num_entradas}\n")  
    for _ in range(num_entradas):
        x = random.uniform(x_min, x_max)  # Gera um número aleatório para x
        y = random.uniform(y_min, y_max)  # Gera um número aleatório para y
        f.write(f"{x:.6f} {y:.6f}\n")  # Escreve as coordenadas

print(f"Arquivo '{file_name}' gerado com sucesso!")
