#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAMANHO_TABELA 1000003

typedef struct No {
    char chave[13];
} No;

unsigned long hash(char *str) {
    unsigned long hash = 5381;

    // Função de hash simples
    while (*str) {
        hash = hash * 33 + *str++;
    }

    return hash % TAMANHO_TABELA;
}

void inserir(No *tabela, char *str) {
    unsigned long indice = hash(str);

    // Tratamento de colisões por sondagem linear
    while (tabela[indice].chave[0] != '\0') {
        indice = (indice + 1) % TAMANHO_TABELA;
    }

    strcpy(tabela[indice].chave, str);
}

char *buscar(No *tabela, char *str) {
    unsigned long indice = hash(str);

    // Tratamento de colisões por sondagem linear
    while (tabela[indice].chave[0] != '\0') {
        if (strcmp(tabela[indice].chave, str) == 0) {
            return "yes";
        }
        indice = (indice + 1) % TAMANHO_TABELA;
    }

    return "no";
}

int main(int argc, char *argv[]) {
    FILE *arquivo = fopen(argv[1], "r");
    if (!arquivo) {
        perror("Erro ao abrir o arquivo");
        return 1;
    }

    int N;
    fscanf(arquivo, "%d", &N);

    // Inicializando a tabela hash
    No *tabelaHash = (No *)malloc(TAMANHO_TABELA * sizeof(No));
    for (int i = 0; i < TAMANHO_TABELA; ++i) {
        tabelaHash[i].chave[0] = '\0';
    }

    // Processando as instruções
    for (int i = 0; i < N; ++i) {
        char comando[7];
        char str[13];

        fscanf(arquivo, "%s %s", comando, str);

        if (strcmp(comando, "insert") == 0) {
            inserir(tabelaHash, str);
        } else if (strcmp(comando, "find") == 0) {
            printf("%s\n", buscar(tabelaHash, str));
        }
    }

    // Liberando a memória da tabela hash
    free(tabelaHash);

    // Fechando o arquivo
    fclose(arquivo);

    return 0;
}