#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM_MAX 15

typedef int *PInt;

typedef struct noh
{
    PInt array;
    int tamanho;
    struct noh *next;
} TNo;

typedef TNo *PNo;

unsigned int funcao_hash(const PInt, int);
int verifica_se_contem(PNo, const PInt, int);
void adiciona_na_lista(PNo *, const PInt, int);
void libera_lista(PNo);
void dobra_vetor(const PInt, int, int, PInt *, PInt);
int verifica_sequencia(const PInt, int, const PInt, int, PNo *);

int main()
{
    int n, m;
    int senha[TAM_MAX], resultado[TAM_MAX];

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &senha[i]);

    scanf("%d", &m);
    for (int i = 0; i < m; i++)
        scanf("%d", &resultado[i]);

    TNo *dobras = NULL;

    if (verifica_sequencia(senha, n, resultado, m, &dobras))
        printf("S\n");
    else
        printf("N\n");

    libera_lista(dobras);
    return 0;
}

unsigned int funcao_hash(const PInt vetor, int tamanho)
{
    unsigned int hash = tamanho;
    for (int i = 0; i < tamanho; i++)
    {
        hash += vetor[i] * ((hash >> 4) + (hash << 2));
    }
    return hash;
}

int verifica_se_contem(PNo inicio, const PInt vetor, int tamanho)
{
    TNo *atual = inicio;
    while (atual != NULL)
    {
        if (atual->tamanho == tamanho && memcmp(atual->array, vetor, tamanho * sizeof(int)) == 0)
        {
            return 1;
        }
        atual = atual->next;
    }
    return 0;
}

void adiciona_na_lista(PNo *inicio, const PInt vetor, int tamanho)
{
    TNo *new_node = (PNo)malloc(sizeof(TNo));
    new_node->array = (PInt)malloc(tamanho * sizeof(int));
    memcpy(new_node->array, vetor, tamanho * sizeof(int));
    new_node->tamanho = tamanho;
    new_node->next = *inicio;
    *inicio = new_node;
}

void libera_lista(PNo inicio)
{
    while (inicio != NULL)
    {
        PNo temp = inicio;
        inicio = inicio->next;
        free(temp->array);
        free(temp);
    }
}

void dobra_vetor(const PInt senha, int tamanho, int indice, PInt *resultado, PInt res_tamanho)
{
    PInt prim_parte = (PInt)malloc(indice * sizeof(int));
    PInt seg_parte = (PInt)malloc((tamanho - indice) * sizeof(int));
    int prim_tamanho = indice, seg_tamanho = tamanho - indice;
    int i, j, diff;

    for (i = 0; i < prim_tamanho; i++)
        prim_parte[i] = senha[i];
    for (i = 0; i < seg_tamanho; i++)
        seg_parte[i] = senha[tamanho - 1 - i];

    if (prim_tamanho >= seg_tamanho)
    {
        diff = prim_tamanho - seg_tamanho;
        *res_tamanho = prim_tamanho;
        *resultado = (PInt)malloc((*res_tamanho) * sizeof(int));
        for (i = 0; i < diff; i++)
            (*resultado)[i] = prim_parte[i];
        for (i = 0; i < seg_tamanho; i++)
            (*resultado)[i + diff] = prim_parte[i + diff] + seg_parte[i];
    }
    else
    {
        diff = seg_tamanho - prim_tamanho;
        *res_tamanho = seg_tamanho;
        *resultado = (PInt)malloc((*res_tamanho) * sizeof(int));
        for (i = 0; i < diff; i++)
            (*resultado)[i] = seg_parte[i];
        for (i = 0; i < prim_tamanho; i++)
            (*resultado)[i + diff] = prim_parte[i] + seg_parte[i + diff];
    }

    free(prim_parte);
    free(seg_parte);
}

int verifica_sequencia(const PInt atual, int tamanho_atual, const PInt resultado, int tar_tamanho, PNo *dobras)
{
    if (tamanho_atual == tar_tamanho && memcmp(atual, resultado, tamanho_atual * sizeof(int)) == 0)
        return 1;
    if (tamanho_atual == 1)
        return 0;

    adiciona_na_lista(dobras, atual, tamanho_atual);

    for (int i = 0; i <= tamanho_atual; i++)
    {
        PInt proximo_vetor;
        int next_tamanho;
        dobra_vetor(atual, tamanho_atual, i, &proximo_vetor, &next_tamanho);

        if (!verifica_se_contem(*dobras, proximo_vetor, next_tamanho))
        {
            if (verifica_sequencia(proximo_vetor, next_tamanho, resultado, tar_tamanho, dobras))
            {
                free(proximo_vetor);
                return 1;
            }
        }
        free(proximo_vetor);
    }
    return 0;
}