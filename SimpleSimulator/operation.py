#yash - move immediate, move register, load, store, right shift, left shift, exclusive OR, OR, AND,Invert, 





# line input -> opcode XX XXXx XXXXx
def calculate(line,pc):     #pc-->int
    opcode=line[:5]
    print
    if():
        pass
    elif(opcode==""):
 



def add(line):
                pass


#Move immediate function              
def move_imm(line): #mov reg1 $Imm [Type B] [00010 REG IMM] 
    reg=line[5:8]
    imm_val=line[8:]
    registers[reg]=int(imm_val,2)


def move_reg(line): #mov reg1 reg2 [Type C] [00011(5) 00000(5) REG(3) REG(3)] 
    reg=line[10:13]
    reg2=line[13:]  
    registers[reg]=int(registers[reg2]








def add(line , pc): # add R1 R2 R3   [type] op[5bit] [2unused] reg[3bit] reg[3bit] reg[3bit]
    opcode = l