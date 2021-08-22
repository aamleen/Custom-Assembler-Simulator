import operation_file as opf


# line input -> opcode XX XXXx XXXXx
def calculate(line,pc):     #pc-->int
    opcode=line[:5]
    print(get_nbit(str(bin(pc))[2:],8), end=" ")
    pc=pc+1
    if(opcode=="00000"):
        opf.add(line, pc)     
    elif(opcode=="00001"):
        opf.sub(line, pc) 
    elif(opcode=="00010"):
        opf.move_imm(line)
    elif(opcode=="00011"):
        opf.move_reg(line)
    elif(opcode=="00100"):
        opf.load(line,pc)
    elif(opcode=="00101"):
        opf.store(line,pc)  
    elif(opcode=="00110"):
        opf.mul(line,pc)
    elif(opcode=="00111"):
        opf.operation_div(line,pc)
    elif(opcode=="01000"):
        opf.RightShift(line) 
    elif(opcode=="01001"):
        opf.LeftShift(line)
    elif(opcode=="01010"):
        opf.operation_xor(line,pc) 
    elif(opcode=="01011"):
        opf.operation_or(line,pc)
    elif(opcode=="01100"):
        opf.operation_and(line,pc) 
    elif(opcode=="01101"):
        opf.operation_invert(line,pc) 
    elif(opcode=="01110"):
        opf.operation_compare(line,pc) 
    elif(opcode=="01111"):
        pc = opf.jmp(line,pc) 
    elif(opcode=="10000"):
        pc = opf.jlt(line,pc) 
    elif(opcode=="10001"):
        pc = opf.jgt(line,pc) 
    elif(opcode=="10010"):
        pc = opf.je(line,pc)
    elif(opcode=="10011"):
        pass
    else:
        pass
    for i in list(opf.registers.keys())[0:7]:
        print(get_nbit(str(bin(opf.registers[i]))[2:],16),end=" ")
    print(get_nbit(str(bin(opf.registers["111"]))[2:],16))
    return pc

def get_nbit(numst,n): # converting 1001 into 00001001 basically completing n-digits 
    st_len = n-len(numst)
    if st_len >=0:
        st_fin = "0"*st_len
        st_fin = st_fin + numst
        return st_fin
    else:
        return None