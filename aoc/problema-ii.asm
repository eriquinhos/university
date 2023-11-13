# Eric Victor - 148000
 
    .text
    
    .globl main
 
main:
    li $t3, 0
    li $t5, 6
    li $t6, 1
 
 
loop:
    li $v0, 5
    syscall
    move $t0, $v0
 
    bgt $t0, $zero, positivo
    j fim
 
positivo:
    addi $t3, $t3, 1
    j fim
 
 
fim:
    sub $t5, $t5, $t6
    beq $t5, $zero, exit
    j loop
 
 
exit:
    li $v0, 1
    move $a0, $t3
    syscall
 
    li $v0, 4
    la $a0, msg2
    syscall
 
    li $v0, 10
    syscall
 
.data
msg2: .asciiz " valores positivos"