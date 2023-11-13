# Eric Victor - 148000
 
        .text
    
        .globl main
main:
 
        # Read the first number
        li $v0, 5
        syscall
        move $t0, $v0
        
        # Read the second number
        li $v0, 5
        syscall
        move $t1, $v0
        
        # Read the third number
        li $v0, 5
        syscall
        move $t2, $v0
        
        # $t3 will save the higher number
        move $t3, $t0
        
        # First comparison
        ble $t3, $t1, else1
        j second
 else1: move $t3, $t1  
        
        
        # Second comparison
second: ble $t3, $t2, else2
        j exit
        
else2: move $t3, $t2
 
 
        # Print string msg1:
 exit:   li $v0, 4
        la $a0, msg1
        syscall
        
        # Print the higher number
        li $v0, 1
        move $a0, $t3
        syscall
        
        .data
msg1: .asciiz "Maior: "
