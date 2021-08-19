opcode = { "00000" :"add",
"00001" : "sub"  ,
"00010" : "mov",
"00011" : "mov",
"00100" : "ld" ,
"00101" : "st" ,
"00110" : "mul" ,
"00111" : "div" ,
"01000" : "rs" ,
"01001" : "ls" ,
"01010" : "xor"  ,
"01011" : "or" ,
"01100" :"and",
"01101" : "not" ,
"01110" : "cmp" ,
"01111" :"jmp" ,
"10000" : "jlt" ,
"10001" : "jgt",
"10010" : "je" 
}

registers = { "000": 0, #r0
"001" :0,               #r1
"010" :0,               #r2
"011" :0,               #r3
"100" :0,
"101" :0,
"110" :0,
"111" :0                #flag
}

def bit_to_int(num):      ## num must be string taking 8 bit number converting into integer
    return int(num,2)
def int_to_bit(num):     ## pass int value and get its corresponding binary number
    return bin(num)[2:]

int("001",2)    #1
#------->num $54 , then removing $, converting to binary and removing the "2b" from starting
def get_8bitformat(st0):
    new_st = st0[1:]
    new_bin_st = bin(int(new_st))[2:] 
     
    res=get_8bit(str(new_bin_st))
    if(res!=None):
        return res
    else:
        None

def get_8bit(numst): # converting 1001 into 00001001 basically completing 8-digits 
    st_len = 8-len(numst)
    if st_len >=0:
        st_fin = "0"*st_len
        st_fin = st_fin + numst
        return st_fin
    else:
        FLAGS="0000000000001000"
        #overflow FLAGS set
        return None


    
