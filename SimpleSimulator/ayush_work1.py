from dicts_and_opes import * 
vFlag =0
def add(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]}
    op = line[:5]
    reg_str_add  = line[7:10]              #storing the destination register 
    reg1_str_add  = line[10:13]             # storing these two regis whose data is going to be manipulated
    reg2_str_add  = line[13:]
    reg_sum = registers[reg1_str_add] + registers[reg2_str_add]
    if sum>255:
        bin_sum = str(bin(reg_sum)[2:])
        str2 = bin_sum[-1:-9:-1]
        str3 = str2[-1:-9:-1]
        reg_sum = int(str3)
        vFlag = 3 

    registers[reg_str_add] =reg_sum
    
    


def sub(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]}
    op = line[:5]
    reg_str_add  = line[7:10]
    reg1_str_add  = line[10:13]
    reg2_str_add  = line[13:]
    reg_sub = registers[reg1_str_add] + registers[reg2_str_add]
    if reg_sub>255:
        bin_sum = str(bin(reg_sub)[2:])
        str2 = bin_sum[-1:-9:-1]
        str3 = str2[-1:-9:-1]
        reg_sub = int(str3)
        vFlag = 3 


    registers[reg_str_add] =reg_sub

def mul(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]}
    op = line[:5]
    reg_str_add  = line[7:10]
    reg1_str_add  = line[10:13]
    reg2_str_add  = line[13:]
    reg_mul = registers[reg1_str_add] + registers[reg2_str_add]

    if reg_mul>255:
        bin_mul = str(bin(reg_mul)[2:])
        str2 = bin_mul[-1:-9:-1]
        str3= str2[-1:-9:-1]
        vFlag = 3 
        reg_mul = int(str3)


    registers[reg_str_add] =reg_mul

def operation_and(line , pc): # and operation taking str as input and updating the registers after carrying the and operation
    op = line[:5]
    reg_str_and  = line[7:10]
    reg1_str_and  = line[10:13]
    reg2_str_and  = line[13:]

    registers[reg_str_and] = int(registers[reg1_str_and] and registers[reg2_str_and])

def operation_or(line , pc): # and operation taking str as input and updating the registers after carrying the or operation
    op = line[:5]
    reg_str_or  = line[7:10]
    reg1_str_or  = line[10:13]
    reg2_str_or  = line[13:]

    registers[reg_str_or] = int(registers[reg1_str_or] or registers[reg2_str_or])

def operation_xor(line , pc): # and operation taking str as input and updating the registers after carrying the xor operation
    op = line[:5]
    reg_str_xor  = line[7:10]
    reg1_str_xor  = line[10:13]
    reg2_str_xor  = line[13:]

    registers[reg_str_xor] = int(registers[reg1_str_xor] ^ registers[reg2_str_xor])


    