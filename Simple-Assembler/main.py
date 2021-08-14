import first_run as fr 
import check_bind_opcode as ck
import second_run as sr

#take input, then pass it in first run func. If it returns 0. go for 2nd run to convert, else print error


def printit(prog_out):  # function to print upcodes 10  
    for x in prog_out:
        print(''.join(str(i) for i in x))


prog_in=["var abc","var cde", "var xyz"]
for i in range(4,118):
    prog_in.append("add R0 R1 R2")
prog_in.append("label4: add R0 R1 R2")
for i in range(119,156):
    prog_in.append("add R0 R1 R2")
prog_in.append("label3: add R0 R1 R2")
for i in range(157,190):
    prog_in.append("add R0 R1 R2")
prog_in.append("label2: add R0 R1 R2")
for i in range(191,243):
    prog_in.append("add R0 R1 R2")
prog_in.append("label: add R0 R1 R2")
for i in range(244,256):
    prog_in.append("add R0 R1 R2")
prog_in.append("hlt")

check = fr.first_ru(prog_in) 
if (check==0):
    res=sr.getbinary_code(fr.var_label,ck.list_of_upcodesandtype)
    if(res==[-1]):
        print("------PROGRAM TERMINATED-----")
    else:
        printit(res)
else: 
    print("------PROGRAM TERMINATED-----")


