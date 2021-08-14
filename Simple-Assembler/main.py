import first_run as fr 
import check_bind_opcode as ck
import second_run as sr
import sys

#take input, then pass it in first run func. If it returns 0. go for 2nd run to convert, else print error


def printit(prog_out):  # function to print final output  
    for x in prog_out:
        print(''.join(str(i) for i in x))

prog_in=[]
for line in sys.stdin:
   prog_in.append(str(line))

#prog_in=["var x","mov R1 $4","mov R2 $4", "cmp R1 R2", "mov R3 FLAGS", "mov R4 $1", "cmp R3 R4","jgt label","label: hlt"]

check = fr.first_ru(prog_in) 
if (check==0):
    res=sr.getbinary_code(fr.var_label,ck.list_of_upcodesandtype)
    if(res==[-1]):
        print("------PROGRAM TERMINATED-----")
    else:
        printit(res)
else: 
    print("------PROGRAM TERMINATED-----")


