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



def get_nbit(numst,n): # converting 1001 into 00001001 basically completing n-digits 
    st_len = n-len(numst)
    if st_len >=0:
        st_fin = "0"*st_len
        st_fin = st_fin + numst
        return st_fin
    else:
        FLAGS="0000000000001000"
        #overflow FLAGS set
        return None


    
