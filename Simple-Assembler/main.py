import first_run
import second_run
from sys import stdin

#take input, then pass it in first run func. If it returns 0. go for 2nd run to convert, else print error


def main():
    for line in stdin:
        if line=='':
            break
        prog_in=input.split()
    check = first_run(prog_in) 
    if (check==0):
        res=getbinary_code(var_label,list_of_upcodesandtype)
        if(res==[-1]):
            print("------PROGRAM TERMINATED-----")
        else:
            printit(res)
    else: 
        print("------PROGRAM TERMINATED-----")

def printit(prog_out):  # function to print upcodes 10  
    for x in prog_out:
        print(''.join(str(i) for i in x))

if __name__=="__main__":
    main()
    


