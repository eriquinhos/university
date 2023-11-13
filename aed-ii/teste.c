#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct funcionario{
    char nome[15];
    int *projeto;
}TFuncionario;

int main(){
    TFuncionario funcionario;
    int i, N;

    printf("Número de vezes pro teste: ");
    scanf("%d", &N);

    funcionario.projeto = (int*) malloc(sizeof(int));

    for(i=0; i<N; i++){
        printf("Nome do Funcionario: ");
        scanf("%s", &funcionario.nome);

        printf("Projeto: ");
        scanf("%d", &funcionario.projeto);

        printf("%s: %d\n", funcionario.nome, funcionario.projeto);
    }

    return 0;
}