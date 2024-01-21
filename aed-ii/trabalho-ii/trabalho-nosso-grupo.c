#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 1000003

// Feito por Maria Clara e Eric

typedef struct noh
{
    char info[13];
    struct noh *prox;
} noh;

noh *hashTable[TABLE_SIZE];

unsigned long hash(const char *str)
{
    unsigned long hash = 0;
    int c;

    while (c = *str++)
        hash = c + (hash << 6) + (hash << 16) - hash;
    return hash % TABLE_SIZE;
}

void insert(const char *str)
{
    unsigned long index = hash(str);
    noh *novoNoh = (noh *)malloc(sizeof(noh));
    strncpy(novoNoh->info, str, sizeof(novoNoh->info) - 1);
    novoNoh->prox = hashTable[index];
    hashTable[index] = novoNoh;
}

int find(const char *str)
{
    unsigned long index = hash(str);
    noh *atual = hashTable[index];
    while (atual != NULL)
    {
        if (strcmp(atual->info, str) == 0)
        {
            return 1;
        }
        atual = atual->prox;
    }

    return 0;
}

void libera()
{
    for (int i = 0; i < TABLE_SIZE; ++i)
    {
        noh *atual = hashTable[i];
        while (atual != NULL)
        {
            noh *temp = atual;
            atual = atual->prox;
            free(temp);
        }
        hashTable[i] = NULL;
    }
}

int main()
{
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; ++i)
    {
        char comando[10], str[13];
        if (scanf("%9s %12s", comando, str) != 2)
        {
            exit(EXIT_FAILURE);
        }

        if (strcmp(comando, "insert") == 0)
        {
            insert(str);
        }
        else if (strcmp(comando, "find") == 0)
        {
            if (find(str))
            {
                printf("yes\n");
            }
            else
            {
                printf("no\n");
            }
        }
    }
    libera();
    return 0;
}