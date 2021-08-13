
## [opcode , no. of register ,imm value ,mem addrs, type ]
## cant take upcode as key cuz we have 2 mov commands but with different arguments


##for storing opcode
op_ind = ""
##A list which stores a two element list of opcode nd the key binding
list_of_upcodesandtype = []

##Function that checks the opcode, str is [add, r1 ,r2 ,r3]
def checkopcode(str,linenum): #[add, r1 ,r2 ,r3]
    for x in opcode:
        #If instruction is matching eg. add
        if (opcode[x][0]==str[0]):
            if(len(str)==1):
                return True            
            op_ind=x    #op_ind = "00000"
            res=checkbinding(str,opcode[x][4],linenum) 
            list_of_upcodesandtype.append([x , opcode[x][4]])
            #True ->no errors in instructions
            #False ->Error found and printed
            return res
        else:   
            #instruction is not an opcode
            return False

##A list storing the valid names of registers            
registers=["R0" ,"R1" , "R2" , "R3" , "R4" , "R4" , "R5" , "R6" , "R7" ]

##A function that checks binding
def checkbinding(str,x,linenum): #str -> [add, r1 ,r2 ,r3] x -> "A"
    flag = 0 
    enc=encoding[x]
    #enc -> [1,1,1] where 1 for register  , -1 for mem adddress , 0 for immediate value
    # if the instruction matches its type (A,B,C...)
    if(len(str)-1==len(enc)):
        for i in range(enc):  #i goes from 0 to max 2  
            #Check for valid register            
            if(enc[i]==1):  
                #if register
                if(str[i+1]=="FLAGS"):
                    if(str[0]=="mov" and i==(len(enc)-1)):
                        continue
                    else:
                        flag=1
                        #ERROR: Use of FLAGS register is prohibited at the required place
                        break
                if(str[i+1] in registers):  
                    #if valid register
                    continue
                else:
                    #2->illegal register name 
                    #Not a valid register
                    error(2,linenum) 
                    flag=1
                    break                 

            #Check for valid immediate value        
            elif(enc[i]==0): 
                #if immediate value starts with $  
                if(str[i+1][0]=='$'):   
                    #if immediate value is int
                    if(str[i+1][1:].isdigit):
                        #if value in range
                        if(0<=int(str[i+1])<=255):
                            continue
                            #valid
                        else:
                            #Value not in range
                            #5-> immediate value out of range
                            error(5,linenum) 
                            flag = 1
                            break 
                    else:
                        #Immediate Value not integer
                        error(12,linenum) 
                        flag =1 
                        break 

                else:
                    #Value should start with $
                    #11 -> "Illegal Symbol used for Immediate Value (not a $)
                    error(11,linenum) 
                    flag = 1
                    break 
            

            #Check for valid memory address
            else:
                continue

    else:
        #Invalid statement - exceeded number of registers or invalid syntax for a register 
        error(10,linenum)
        flag =1 
    
    #Check if there are errors or not
    if (flag==1) :
        return False
    else: 
        return True
        

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


# 1 for register  , -1 for mem adddress , 0 for immediate value
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




  