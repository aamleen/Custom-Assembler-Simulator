## incoding
## [opcode , no. of register ,imm value ,mem addrs, type ]
## cant take upcode as key cuz we have 2 mov commands but with different arguments
## hey yash Hi

##for storing opcode
op_ind=""
##A list which stores a two element list of opcode nd the key binding
l = []

##Function that does something
def checkopcode(str):
    for x in opcode:
        if (opcode[x][0]==str[0]):
            op_ind=x
            checkbinding(str,opcode[x][4])
            l.append( [x , opcode[x][4]])
            return True
        else:
            return False

##A list storing the valid names of registers            
registers=["R0" ,"R1" , "R2" , "R3" , "R4" , "R4" , "R5" , "R6" , "R7" ]

##A function that checks binding
def checkbinding(str,x):
    enc=encoding[x]
    if(len(str)-1==len(enc)):
        for i in range(enc):
            if(enc[i]==1):
                if(str[i+1] in registers):
                    continue
                else:
                    pass
                    #Not a register
            elif(enc[i]==0):
                if(type(str[i+1])==int):
                    if(0<=str[i+1]<=255):
                        continue
                else:
                    #Value not in range
                    pass
            else:
                continue


                
                

    else:
        error()
        
    


      

        

###[add r1 r2 r0]




##A dictionary containing  [opcode : [opcode , no. of register ,imm value ,mem addrs, type ]]
opcode = {"00000" : [ "add", 3, 0 ,0,"A"] ,
"00001"  : ["sub" , 3 , 0 ,0,"A"] ,
"00010" : ["mov" , 1 , 1 ,0,"B"],
"00011" : ["mov" , 2 , 0 ,0, "C"],
"00100" : ["ld" , 1 , 0 , 1, "D"],
"00101" : ["st ", 1 , 0 ,1,"D"],
"00110" : ["mil" , 3 , 0,0 ,"A"],
"00111" : ["div " , 2 , 0 , 0 , "C"],
"01000" : ["rs" , 1 , 1, 0 , "B"],
"01001" : ["ls" , 1 , 1 , 0 , "B"],
"01010" : ["xor" , 3 ,0,0 , "A"],
"01011" : ["or" , 3 , 0 , 0 , "A"],
"01100" : ["and", 3 , 0 , 0 , "A"],
"01101" : ["not" , 2 , 0 , 0 , "C"],
"01110" : ["cmp" , 2 , 0 , 0 , "C"],
"01111" : ["jmp" , 0 , 0 , 1 , "E"],
"10000" : ["jlt" , 0 , 0 , 1 , "E"],
"10001" : ["jgt" , 0 , 0 , 1 , "E"],
"10010" : ["je" , 0 , 0 , 1 , "E"],
"10011" : ["hlt" , 0 , 0 , 0 , "F"],
}



# x = dc[0] 
# x.value()[0] ig

# 1 for regiter  , -1 for mem adddress , 0 for immediate value
encoding = { "A": [1,1,1],
"B": [1,0],
"C": [1,1],
"D": [1,-1],
"E": [-1],
"F": [],
}



reg_address = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111",
}




  