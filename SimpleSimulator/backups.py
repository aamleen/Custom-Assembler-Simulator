from dicts_and_opes import * 
vFlag =0
Gflag =0 # flag of cmp r1 r2 -> 1 if r1 > r2
Lflag =0 # flag od cmp r1 r2 -> is 1 if r1 < r2

def jlt(line,pc):
    if(FLAGS==2):
        return int(line[8:],2)
    else:
        return pc

def jgt(line,pc):
    if(FLAGS==1):
        return int(line[8:],2)
    else:
        return pc

def je(line,pc):
    if(FLAGS==0):
        return int(line[8:],2)
    else:
        return pc

def jmp(line,pc):
    return int(line[8:],2)


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
        FLAGS = 3 

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
        FLAGS = 3 
    registers[reg_str_add] =reg_sub

def mul(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]}
    op = line[:5]
    reg_str_add  = line[7:10]
    reg1_str_add  = line[10:13]
    reg2_str_add  = line[13:]
    reg_mul = registers[reg1_str_add] + registers[reg2_str_add]

    if (reg_mul>255):
        bin_mul = str(bin(reg_mul)[2:])
        str2 = bin_mul[-1:-9:-1]
        str3= str2[-1:-9:-1]
        FLAGS = 3
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

def operation_invert(line ,pc):
    op = line[:5]
    
    reg1_str_in  = line[10:13]
    reg2_str_in   = line[13:]
    registers[reg1_str_in] = -registers[reg2_str_in]

def operation_compare(line ,pc ):
    reg1_str_in  = line[10:13]
    reg2_str_in   = line[13:]
    if registers[reg1_str_in] > registers[reg2_str_in]:
        FLAGS = 1
    elif registers[reg1_str_in] < registers[reg2_str_in]:
        FLAGS =2
    else:
        FLAGS=0

#Move immediate function              
def move_imm(line): #mov reg1 $Imm [Type B] [00010 REG IMM] 
    reg=line[5:8]
    imm_val=line[8:]
    registers[reg]=int(imm_val,2)

def move_reg(line): #mov reg1 reg2 [Type C] [00011(5) 00000(5) REG(3) REG(3)] 
    reg=line[10:13]
    reg2=line[13:]  
    registers[reg]=int(registers[reg2])

def RightShift(line): #rs reg1 $imm [01000 REG IMM(8)] 
    reg = line[5:8]     
    val = line[8:]      #binary value
    val_int = int(val,2) #integer immediate value 
    registers[reg] = registers[reg] >> val_int


def LeftShift(line): #ls reg1 $imm [01001 REG IMM(8)] 
    reg = line[5:8]     
    val = line[8:]      #binary value
    val_int = int(val,2) #integer immediate value 
    registers[reg] = registers[reg] << val_int


def load(line , pc):
    op = line[:5]
    reg  = line[5:8]
    mem_add = line[8:]
    registers[reg] = int(var.get(mem_add))
    


def store(line , pc):
    op = line[:5]
    reg  = line[5:8]
    mem_add = line[8:]
    var[mem_add]   = registers[reg]
    
def operation_div(line , pc):
    op  = line[:5]
    reg1 = line[10: 13]
    reg2 = line[13:]
    registers["000"] = reg1/reg2
    registers["001"]  = reg1%reg2
