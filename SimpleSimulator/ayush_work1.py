from dicts_and_opes import * 

def add(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]}
    op = line[:5]
    reg_str_add  = line[7:10]              #storing the destination register 
    reg1_str_add  = line[10:13]             # storing these two regis whose data is going to be manipulated
    reg2_str_add  = line[13:]
    reg_sum = registers[reg1_str_add] + registers[reg2_str_add]
    if sum>255:
        vFlag = 3 

    registers[reg_str_add] =reg_sum
    
    


def sub(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]}
    op = line[:5]
    reg_str_add  = line[7:10]
    reg1_str_add  = line[10:13]
    reg2_str_add  = line[13:]
    reg_sum = registers[reg1_str_add] + registers[reg2_str_add]
    if sum>255:
        vFlag = 3 

    registers[reg_str_add] =reg_sum

def mul(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]}
    op = line[:5]
    reg_str_add  = line[7:10]
    reg1_str_add  = line[10:13]
    reg2_str_add  = line[13:]
    reg_sum = registers[reg1_str_add] + registers[reg2_str_add]
    if sum>255:
        vFlag = 3 

    registers[reg_str_add] =reg_sum



    