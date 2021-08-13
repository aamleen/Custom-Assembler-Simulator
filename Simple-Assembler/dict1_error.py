
# error_dict = {
#     1 : "Illegal Instruction Name" ,
#     2 : "Illegal Register Name" ,
#     3 : "Use of undefined variables" ,
#     4 : "Illegal Use of FLAGS Register" ,
#     5 : "Immediate Value out of Range" ,
#     6 : "Label/Variable exists with same name" ,
#     7 : "Variable not declared" ,
#     8 : "Halt operation missing" ,
#     9 : "Halt is not being used as the last operation" ,
#     10 : "Wrong syntax used for instruction (add is used as type B instruction) " ,
#     11 : "Illegal Symbol used for Immediate Value (not a $)" ,
#     12 : "Immediate Value is not an integer" , 
#     13 : "Invalid Declaration of Halt Operation" , 
#     14 : "Illegal name of variable",
#     15 : "Illegal use of Variable (variable not declared in the beginning)",
#     16 : "Illegal declaration of Variable",
#     17 : "Illegal name of Label"
# }

# def error(x,lineno):
#     print("ERROR: ",error_dict[x],", at line number",lineno)