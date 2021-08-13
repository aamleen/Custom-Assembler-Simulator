##Ahh
error_dict = {
    1 : "Illegal Instruction Name" ,
    2 : "Illegal Register Name" ,
    3 : "Use of undefined variables" ,
    4 : "Illegal Use of FLAGS Register" ,
    5 : "Immediate Value out of Range" ,
    6 : "Misuse of Labels as variables" ,
    7 : "Variable not declared" ,
    8 : "Halt operation missing" ,
    9 : "Halt is not being used as the last operation" ,
    10 : "Wrong syntax used for instruction (add is used as type B instruction) " ,
    11 : "Illegal Symbol used for Immediate Value (not a $)" ,
    12 : "Immediate Value is not an integer"
}

def error(x,lineno):
    print()