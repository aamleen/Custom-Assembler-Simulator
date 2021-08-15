
## cant take upcode as key cuz we have 2 mov commands but with different arguments
##A dictionary containing  [opcode(bin) : [opcode , no. of register ,imm value ,mem addrs, type ]]
opcode = {"00000" : [ "add", 3, 0 ,0,"A"] ,
"00001"  : ["sub" , 3 , 0 ,0,"A"] ,
"00010" : ["mov" , 1 , 1 ,0,"B"],
"00011" : ["mov" , 2 , 0 ,0, "C"],
"00100" : ["ld" , 1 , 0 , 1, "D"],
"00101" : ["st", 1 , 0 ,1,"D"],
"00110" : ["mul" , 3 , 0,0 ,"A"],
"00111" : ["div" , 2 , 0 , 0 , "C"],
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
}

# A dictionary containing the encoding syntax = 1 for register  , -1 for mem adddress , 0 for immediate value
encoding = { "A": [1,1,1],
"B": [1,0],
"C": [1,1],
"D": [1,-1],
"E": [-1],
"F": [],
}

#A list where each entry is again a list containing opcode, regs/imm/mem_addr, line no. and type of encoding
#eg- add R1 R2 R3 = ["00000","R1","R2","R3",lineno.,"A"]
list_of_upcodesandtype = []     

err_print=0     #to check if the error hsa been printed already (if any)

##Function that checks the opcode, st is [add, r1 ,r2 ,r3]
def checkopcode(st,linenum): #[add, r1 ,r2 ,r3]
    global err_print
    for x in opcode:
        #If instruction is matching eg. add
        if (opcode[x][0]==st[0]):
            if(len(st)==1):
                return True            
            bind=opcode[x][4]
            if(st[0]=="mov"):       #explicit definition because there are 2 types of mov
                if(st[-1] in registers or st[-1]=="FLAGS"):
                    x="00011"
                    bind="C"
                else:
                    x="00010"
                    bind="B"
            res=checkbinding(st,bind,linenum)
            st=st[1:]
            st.insert(0,x)
            st.append(linenum)
            st.append(bind) 
            list_of_upcodesandtype.append(st)
            if(res==False):
                print("ERROR at line",linenum,": Wrong syntax used for instructions")
                err_print=1
            #True ->no errors in instructions
            #False ->Error found and printed
            return res
    return False

##A list storing the valid names of registers            
registers=["R0" ,"R1" , "R2" , "R3" , "R4" , "R4" , "R5" , "R6"]

##A function that checks encoding
def checkbinding(st,x,linenum): #st -> [add, r1 ,r2 ,r3] x -> "A"
    flag = 0 
    enc=encoding[x]
    #enc -> [1,1,1] where 1 for register  , -1 for mem adddress , 0 for immediate value
    # if the instruction matches its type (A,B,C...)
    if(len(st)-1==len(enc)):
        for i in range(len(enc)):  #i goes from 0 to max 2  
            #Check for valid register            
            if(enc[i]==1):  
                #if register
                if(st[i+1]=="FLAGS"):
                    if(st[0]=="mov" and i==(len(enc)-1)):       #flags only allowed for mov
                        continue
                    else:
                        #ERROR: FLAGS registered use without mov instruction
                        print("ERROR at line",linenum,": Illegal use of FLAGS register") 
                        flag=1
                        break
                if(st[i+1] in registers):  
                    #if valid register
                    continue
                else:
                    #2->Illegal register name 
                    #ERROR: Not a valid register
                    print("ERROR at line",linenum,": Illegal register name ")
                    flag=1
                    break                 

            #Check for valid immediate value        
            elif(enc[i]==0): 
                #if immediate value starts with $  
                if(st[i+1][0]=='$'):   
                    #if immediate value is int
                    if(st[i+1][1:].isdigit()):
                        #if value in range
                        if(0<=int(st[i+1][1:])<=255):
                            continue
                            #valid
                        else:
                            #ERROR: 
                            print("ERROR at line",linenum,": Illegal Immediate values (less than 0 or more than 255)")
                            flag = 1
                            break 
                    else:
                        #ERROR:
                        print("ERROR at line",linenum,": Illegal Immediate Values (Not an integer) ")
                        flag =1 
                        break 

                else:
                    #ERROR:
                    print("ERROR at line",linenum,": Illegal Symbol used for Immediate Value (not a $) ")
                    flag = 1
                    break 
            #Check for valid memory address
            #Will be checked later, during 2nd run
            else:
                continue
    else:
        #ERROR: 
        print("ERROR at line",linenum,": Invalid statement - exceeded number of registers or invalid syntax for a register ")
        flag =1 
    
    #Check if there are errors or not
    if (flag==1) :
        return False
    else: 
        return True
