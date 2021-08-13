import first_run as fr 
import check_bind_opcode as ck
import second_run as sr

#take input, then pass it in first run func. If it returns 0. go for 2nd run to convert, else print error


def printit(prog_out):  # function to print upcodes 10  
    for x in prog_out:
        print(''.join(str(i) for i in x))

prog_in=["var x","add R1 R2 R3","ld R1 x","hlt","mov R1 R2","mov R1 $69","hlt"]
check = fr.first_ru(prog_in) 
if (check==0):
    res=sr.getbinary_code(fr.var_label,ck.list_of_upcodesandtype)
    if(res==[-1]):
        print("------PROGRAM TERMINATED-----")
    else:
        printit(res)
else: 
    print("------PROGRAM TERMINATED-----")


