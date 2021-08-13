
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




  #-------num $54 , $5 then removing $ sign
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

        

def getbinary_code(var_label,list_of_upcodesandtype):
    binarycode_out  =[]    # output list of binarycodes

    for i in range(len(list_of_upcodesandtype)):
        if list_of_upcodesandtype[i][-1]=="A":
            binarycode_out.append([ list_of_upcodesandtype[i][0],"00",reg_address[list_of_upcodesandtype[i][1]],reg_address[list_of_upcodesandtype[i][2]],reg_address[list_of_upcodesandtype[i][3]]])
        
        if list_of_upcodesandtype[i][-1]=="B":
            bin_var=get_8bitformat(list_of_upcodesandtype[i][2])
            if(bin_var!=None):
                binarycode_out.append([ list_of_upcodesandtype[i][0],reg_address[list_of_upcodesandtype[i][1]],bin_var])
            else: 
                print("Overflow in memory address at line",list_of_upcodesandtype[i][2])
        if list_of_upcodesandtype[i][-1]=="C":
            binarycode_out.append([ list_of_upcodesandtype[i][0],"00000",reg_address[list_of_upcodesandtype[i][1]],reg_address[list_of_upcodesandtype[i][2]]])
        
        if list_of_upcodesandtype[i][-1]=="D":
            
            if(list_of_upcodesandtype[i][2] in var_label):
                bin_var=get_8bit(var_label[list_of_upcodesandtype[i][2]][2])
                if(bin_var!=None):
                    binarycode_out.append([ list_of_upcodesandtype[i][0],reg_address[list_of_upcodesandtype[i][1]], bin_var ] )
                else: 
                    print("Overflow in memory address at line",list_of_upcodesandtype[i][2])
            else:
                #ERROR: Use of undefined variables 
                binarycode_out=[-1]
                print("ERROR at line",list_of_upcodesandtype[i][-2],": Use of undefined variables")
                break

        if list_of_upcodesandtype[i][-1]=="E":
            if(list_of_upcodesandtype[1] in var_label):
                bin_var=get_8bit(var_label[list_of_upcodesandtype[1]][2])
                if(bin_var!=None):
                    binarycode_out.append([ list_of_upcodesandtype[i][0],"000", get_8digit(var_label[list_of_upcodesandtype[i][2]][1])])
                else:    
                    print("Overflow in memory address at line",list_of_upcodesandtype[i][2])
            else:
                #ERROR: Use of undefined variables 
                binarycode_out = [-1]
                print("ERROR at line",list_of_upcodesandtype[i][-2],": Use of undefined variables")
                break
            
        if list_of_upcodesandtype[i][-1]=="F":
            binarycode_out.append([list_of_upcodesandtype[i][0],"00000000000"])
    
    return binarycode_out

      
        



