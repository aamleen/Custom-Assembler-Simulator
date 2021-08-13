list_of_upcodesandtype = []
binarycode_out  =[]
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

#3 mylabel: add r1 r0 r3 0011
#6 hlt
# var_label={X:[2,0111]}
#ld r1 X 016576 0011 0111 bin(8)=100
# de0


  #num $54 , $5 then removing $ sign
def get_8bitformat(str0):
    new_str = str0[1:]
    code_len = 8 - (len(bin(int(new_str)))-2)
    new_bin_str = bin(int(new_str))[2:]
    if code_len >= 0 :
        str1="0"*code_len
        final_str =str1+ str(new_bin_str)
        return final_str
    
    else:
        pass #error

def get_8bit(numstr): # 1001 into 00001001
    str_len = 8-len(numstr)
    if str_len >=0:
        str_fin = "0"*str_len
        str_fin = str_fin + numstr
        return str_fin
    else:
        pass 
        #error


def getbinary_code(list_of_upcodesandtype , str , var_label):
    for i in range(len(list_of_upcodesandtype)):
        if list_of_upcodesandtype[i][1]=="A":
            binarycode_out.append([ list_of_upcodesandtype[i][0],"00",reg_address[str[i][1]],reg_address[str[i][2]],reg_address[str[i][3]]])
        
        if list_of_upcodesandtype[i][1]=="B":
            binarycode_out.append([ list_of_upcodesandtype[i][0],reg_address[str[i][1]], get_8bitformat(str[i][2])  ]) 

        if list_of_upcodesandtype[i][1]=="C":
            binarycode_out.append([ list_of_upcodesandtype[i][0],"00000",reg_address[str[i][2]],reg_address[str[i][3]]])
        
        if list_of_upcodesandtype[i][1]=="D":
            binarycode_out.append([ list_of_upcodesandtype[i][0],reg_address[str[i][2]], get_8digit(var_label[str[i][2]][1]) ] )

        if list_of_upcodesandtype[i][1]=="E":
            binarycode_out.append([ list_of_upcodesandtype[i][0],"000", get_8digit(var_label[str[i][2]][1]) ])

        if list_of_upcodesandtype[i][1]=="F":
            binarycode_out.append(list_of_upcodesandtype[i][0],"00000000000")

      
        



