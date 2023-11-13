# Eric Victor - 148000
 
.text
 
.globl main
 
main:
    li $t1, 30  # Maior numero de entradas
 
    li $t2, 0  # Maior velocidade
 
    li $t3, 1   # Subtracao do loop
 
    li $t4, 0  # Valor de velocidade vigente
 
    li $t5, 50 # Velocidade Maxima
 
    li $t6, 10 # Nivel 1
    li $t7, 20 # Nivel 2
    li $t8, 2
    li $t9, 3
 
    li $v0, 5
    syscall
    move $t0, $v0
 
    bgt $t0, $t1, tamerror
 
loop:
    li $v0, 5
    syscall
    move $t4, $v0
 
    bgt $t4, $t5, valerror
 
    blt $t2, $t4, troca
    j fim
 
troca:
    move $t2, $t4
 
fim:
    sub $t0, $t0, $t3
    beq $t0, $zero, nivel
    j loop
 
 
tamerror:
    li $v0, 1
    move $a0, $t0
    syscall
 
    li $v0, 4
    la $a0, msg1
    syscall
 
    j exit
 
valerror:
    li $v0, 1
    move $a0, $t4
    syscall
 
    li $v0, 4
    la $a0, msg2
    syscall
 
    li $v0, 4
    la $a0, msg3
    syscall
 
    sub $t0, $t0, $t3
    beq $t0, $zero, nivel
    j loop
 
nivel:
    blt $t2, $t6, nvl1
    blt $t2, $t7, nvl2
    j nvl3
 
nvl1:
    move $t2, $t3
    j output
 
nvl2:
    move $t2, $t8
    j output
 
nvl3:
    move $t2, $t9
 
 
output:
    li $v0, 4
    la $a0, msg4
    syscall
 
    li $v0, 1
    move $a0, $t2
    syscall
 
exit:
    li $v0, 10
    syscall
 
 
.data
msg1: .asciiz ": valor invalido." 
msg2: .asciiz ": velocidade invalida"
msg3: .asciiz "\n"
msg4: .asciiz "Maior nivel: velocidade "