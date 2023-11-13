#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct lista{
    int info;
    struct lista *prox;
}TLista;

typedef TLista *PLista;

typedef struct funcionario{
    char nome[15];
    PLista projeto;
} TFuncionario;

typedef struct arvore{
    TFuncionario funcionario;
    struct arvore *esquerda;
    struct arvore *direita;
    int altura;
} TArvore;

typedef TArvore *PArvore;

PLista inicializaLista();

PLista insereLista(PLista, int);

void imprimeLista(PLista);

int max(int, int);

PArvore inicializaArvore();

int alturaArvore(PArvore);

int fatorBalanceamento(PArvore);

PArvore rotacaoRR(PArvore);

PArvore rotacaoLL(PArvore);

PArvore rotacaoLR(PArvore);

PArvore rotacaoRL(PArvore);

PArvore buscaArvore(PArvore, char*);

PArvore insereArvore(PArvore, char*, int);


int main(int argc, char *argv[]){
    int operacao, i, projeto;
    char nome[15];
    PArvore arvore, aux;
    TFuncionario funcionario;


    arvore = inicializaArvore();

    while(1){
        scanf("%d", &operacao);

        switch(operacao){
            case 0:
                return 0;
                break;

            case 1:
                scanf("%s", &nome);
                scanf("%d", &projeto);

                arvore = insereArvore(arvore, nome, projeto);
                break;

            case 2:
                scanf("%s", funcionario.nome);
                aux = buscaArvore(arvore, funcionario.nome);
                if(aux!=NULL){
                    printf("%d ", aux->altura+1);
                    imprimeLista(aux->funcionario.projeto);
                    printf("\n");
                }
                else{
                    printf("0\n");
                }
                break;
        }
    }

    return 0;
}

PLista inicializaLista(){
    return NULL;
}

PLista insereLista(PLista l, int info){
    PLista novo = (PLista) malloc(sizeof(TLista));
    novo->info = info;

    if(l==NULL){
        novo->prox = novo;
        return novo;
    }
    else{
        novo->prox = l->prox;
        l->prox = novo;
        return novo;
    }
    return l;
}

void imprimeLista(PLista l){
    PLista aux = l;
    if(l!=NULL){
        do{
            printf("%d ", aux->prox->info);
            aux = aux->prox;
        }while(aux!=l);
    }
}


int max(int a, int b){
    return (a > b) ? a : b;
}

PArvore inicializaArvore(){
    return NULL;
}

int alturaArvore(PArvore arv){
    if(arv == NULL){
        return -1;
    }else{
        return arv->altura;
    }
}

int fatorBalanceamento(PArvore arv){
    return alturaArvore(arv->esquerda) - alturaArvore(arv->direita);
}


PArvore rotacaoRR(PArvore arv){
    PArvore aux;
    aux = arv->direita;
    arv->direita = aux->esquerda;
    aux->esquerda = arv;
    arv->altura = max(alturaArvore(arv->esquerda), alturaArvore(arv->direita)) + 1;
    aux->altura = max(alturaArvore(aux->esquerda), alturaArvore(aux->direita)) + 1;
    return aux;
}

PArvore rotacaoLL(PArvore arv){
    PArvore aux;
    aux = arv->esquerda;
    arv->esquerda = aux->direita;
    aux->direita = arv;
    arv->altura = max(alturaArvore(arv->esquerda), alturaArvore(arv->direita)) + 1;
    aux->altura = max(alturaArvore(aux->esquerda), alturaArvore(aux->direita)) + 1;
    return aux;
}

PArvore rotacaoLR(PArvore arv){
    arv->esquerda = rotacaoRR(arv->esquerda);
    return rotacaoLL(arv);
}

PArvore rotacaoRL(PArvore arv){
    arv->direita = rotacaoLL(arv->direita);
    return rotacaoRR(arv);
}

PArvore buscaArvore(PArvore arv, char *nome){
    if(arv == NULL){
        return NULL;
    }
    else if(strcmp(nome, arv->funcionario.nome) < 0){
        return buscaArvore(arv->esquerda, nome);
    }
    else if(strcmp(nome, arv->funcionario.nome) > 0){
        return buscaArvore(arv->direita, nome);
    }
    else{
        return arv;
    }
}

PArvore insereArvore(PArvore arv, char *nome, int projeto){
    int tam;
    PArvore aux = buscaArvore(arv, nome);

    if(aux != NULL){
        aux->funcionario.projeto = insereLista(aux->funcionario.projeto, projeto);
        arv = aux;

        return aux;
    }

    else {
        if (arv == NULL) {
            arv = (PArvore) malloc(sizeof(TArvore));

            printf("inseri %s e o projeto %d\n", nome, projeto);

            strcpy(arv->funcionario.nome, nome);
            arv->funcionario.projeto = insereLista(arv->funcionario.projeto, projeto);

            arv->esquerda = NULL;
            arv->direita = NULL;
            arv->altura = 0;
        }

        else if (strcmp(nome, arv->funcionario.nome) < 0) {
            arv->esquerda = insereArvore(arv->esquerda, nome, projeto);
            if (fatorBalanceamento(arv) == 2) {
                if (strcmp(nome, arv->esquerda->funcionario.nome) < 0) {
                    arv = rotacaoLL(arv);
                }
                else {
                    arv = rotacaoLR(arv);
                }
            }
        }

        else if (strcmp(nome, arv->funcionario.nome) > 0) {
            arv->direita = insereArvore(arv->direita, nome, projeto);
            if (fatorBalanceamento(arv) == -2) {
                if (strcmp(nome, arv->direita->funcionario.nome) > 0) {
                    arv = rotacaoRR(arv);
                }
                else {
                    arv = rotacaoRL(arv);
                }
            }
        }

        arv->altura = max(alturaArvore(arv->esquerda), alturaArvore(arv->direita)) + 1;

        return arv;
    }
}
