import first_run as fr 
import check_bind_opcode as ck
import second_run as sr
import sys

#take input, then pass it in first run func. If it returns 0 no errors found. go for 2nd run to convert, else print error


def printit(prog_out):  # function to print final output  
    for x in prog_out:
        print(''.join(str(i) for i in x))
    
def main():
    prog_in=[]
    for line in sys.stdin:      #takes input from stdin and stores in a list, where each entry(line) is a string 
        prog_in.append(str(line))

    end_line=0
    for i in prog_in[::-1]:     #runs the input in reverese order, and removes the empty lines till any instruction is found
        if(i=='' or i=='\n'):
            end_line +=1
        else:
            break
    prog_in=prog_in[:len(prog_in)-end_line]     #removes the last empty lines

    check = fr.first_ru(prog_in) 
    if (check==0):
        res=sr.getbinary_code(fr.var_label,ck.list_of_upcodesandtype)
        if(res==[-1]):      #if any error while converting the code
            print("------PROGRAM TERMINATED-----")
        else:
            printit(res)
    else: 
        print("------PROGRAM TERMINATED-----")

if __name__ =="__main__":
    main()


