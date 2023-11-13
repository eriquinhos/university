# Eric Victor - 148000
 
    .text
    
    .globl main
 
main:
    li $t1, 0
    li $t2, 0
    li $t3, 0
    li $t4, 0
    li $t5, 5
    li $t6, 1
    li $t7, 2
 
loop:
    li $v0, 5
    syscall
    move $t0, $v0
 
    div $t0, $t7
    mfhi $t8
    
    beq $t8, $zero, par
    j impar
 
par:
    addi $t1, $t1, 1
    j else
 
impar:
    addi $t2, $t2, 1
    
else:
    bgt $t0, $zero, positivo
    j negativo
 
positivo:
    addi $t3, $t3, 1
    j fim
 
negativo:
    addi $t4, $t4, 1
 
fim:
    sub $t5, $t5, $t6
    beq $t5, $zero, exit
    j loop
 
 
exit:
    li $v0, 1
    move $a0, $t1
    syscall
 
    li $v0, 4
    la $a0, msg1
    syscall
 
    li $v0, 4
    la $a0, msg5
    syscall
 
    li $v0, 1
    move $a0, $t2
    syscall
 
    li $v0, 4
    la $a0, msg2
    syscall
 
    li $v0, 4
    la $a0, msg5
    syscall
 
    li $v0, 1
    move $a0, $t3
    syscall
 
    li $v0, 4
    la $a0, msg3
    syscall
 
    li $v0, 4
    la $a0, msg5
    syscall
 
    li $v0, 1
    move $a0, $t4
    syscall
 
    li $v0, 4
    la $a0, msg4
    syscall
 
    li $v0, 10
    syscall
 
.data
msg1: .asciiz " valor(es) par(es)"
msg2: .asciiz " valor(es) impar(es)"
msg3: .asciiz " valor(es) positivo(s)"
msg4: .asciiz " valor(es) negativo(s)"
msg5: .asciiz "\n"
×