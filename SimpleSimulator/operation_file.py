registers = { "000":0, "001":0, "010":0, "011":0, "100":0, "101":0, "110":0, "111":0}

var={}      #"mem_addr":value

def jlt(line,pc):
    if(FLAGS==4):
        return int(line[8:],2)
    else:
        return pc

def jgt(line,pc):
    if(FLAGS==2):
        return int(line[8:],2)
    else:
        return pc

def je(line,pc):
    if(FLAGS==1):
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
    reg_sum = registers[reg1_str_add]+registers[reg2_str_add]
    if reg_sum>255:
        bin_sum = str(bin(reg_sum))[2:]
        str3 = bin_sum[-8:]
        reg_sum = int(str3,2)
        registers["111"] = 8 
    else:
        registers["111"]=0

    registers[reg_str_add] =reg_sum

def sub(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]}
    op = line[:5]
    reg_str_add  = line[7:10]
    reg1_str_add  = line[10:13]
    reg2_str_add  = line[13:]
    reg_sub = registers[reg1_str_add] - registers[reg2_str_add]
    if reg_sub<0:
        reg_sub = 0
        registers["111"] = 8
    else:
        registers['111']=0
    registers[reg_str_add] =reg_sub

def mul(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]}
    op = line[:5]
    reg_str_add  = line[7:10]
    reg1_str_add  = line[10:13]
    reg2_str_add  = line[13:]
    reg_mul = registers[reg1_str_add] * registers[reg2_str_add]

    if (reg_mul>255):
        bin_mul = str(bin(reg_mul)[2:])
        str3 = bin_mul[-8:]
        registers["111"] = 8
        reg_mul = int(str3,2)
    else:
        registers['111']=0
    registers[reg_str_add] =reg_mul

def operation_and(line , pc): # and operation taking str as input and updating the registers after carrying the and operation
    op = line[:5]
    reg_str_and  = line[7:10]
    reg1_str_and  = line[10:13]
    reg2_str_and  = line[13:]

    registers[reg_str_and] = int(registers[reg1_str_and] and registers[reg2_str_and])
    registers['111']=0

def operation_or(line , pc): # and operation taking str as input and updating the registers after carrying the or operation
    op = line[:5]
    reg_str_or  = line[7:10]
    reg1_str_or  = line[10:13]
    reg2_str_or  = line[13:]

    registers[reg_str_or] = int(registers[reg1_str_or] or registers[reg2_str_or])
    registers['111']=0

def operation_xor(line , pc): # and operation taking str as input and updating the registers after carrying the xor operation
    op = line[:5]
    reg_str_xor  = line[7:10]
    reg1_str_xor  = line[10:13]
    reg2_str_xor  = line[13:]

    registers[reg_str_xor] = int(registers[reg1_str_xor] ^ registers[reg2_str_xor])
    registers['111']=0

def operation_invert(line ,pc):
    op = line[:5]
    
    reg1_str_in  = line[10:13]
    reg2_str_in   = line[13:]
    registers[reg1_str_in] = -registers[reg2_str_in]
    registers['111']=0

def operation_compare(line ,pc ):
    reg1_str_in  = line[10:13]
    reg2_str_in   = line[13:]
    if registers[reg1_str_in] > registers[reg2_str_in]:
        registers["111"] = 4
    elif registers[reg1_str_in] < registers[reg2_str_in]:
        registers["111"] = 8
    else:
        registers["111"] = 1

#Move immediate function              
def move_imm(line): #mov reg1 $Imm [Type B] [00010 REG IMM] 
    reg=line[5:8]
    imm_val=line[8:]
    registers[reg]=int(imm_val,2)
    registers['111']=0

def move_reg(line): #mov reg1 reg2 [Type C] [00011(5) 00000(5) REG(3) REG(3)] 
    reg=line[10:13]
    reg2=line[13:]  
    registers[reg]=int(registers[reg2])
    registers['111']=0

def RightShift(line): #rs reg1 $imm [01000 REG IMM(8)] 
    reg = line[5:8]     
    val = line[8:]      #binary value
    val_int = int(val,2) #integer immediate value 
    registers[reg] = registers[reg] >> val_int
    registers['111']=0


def LeftShift(line): #ls reg1 $imm [01001 REG IMM(8)] 
    reg = line[5:8]     
    val = line[8:]      #binary value
    val_int = int(val,2) #integer immediate value 
    registers[reg] = registers[reg] << val_int
    registers['111']=0


def load(line , pc ):
    op = line[:5]
    reg  = line[5:8]
    mem_add = line[8:]
    registers[reg] = int(var.get(mem_add))
    registers['111']=0

def store(line , pc ):
    op = line[:5]
    reg  = line[5:8]
    mem_add = line[8:]
    var[mem_add]   = registers[reg]
    registers['111']=0
    
def operation_div(line , pc):
    op  = line[:5]
    reg1 = line[10: 13]
    reg2 = line[13:]
    registers["000"] = int(reg1/reg2)
    registers["001"]  = reg1%reg2
    registers['111']=0
