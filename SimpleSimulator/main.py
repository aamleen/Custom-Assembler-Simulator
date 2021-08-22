import Operations as op
import operation_file as Op_fl
import Memorydump as mem
import sys

def main():
    prog_in=[]
    for line in sys.stdin:      #takes input from stdin and stores in a list, where each entry(line) is a string 
        prog_in.append(str(line))
    pc=0
    line=prog_in[pc]
    while(pc<len(prog_in)):
        hlt=line[:5]
        if(hlt=="10011"):
            break
        pc=op.calculate(line,pc)
        line=prog_in[pc]
    mem.dump(prog_in,Op_fl.var)

if __name__ =="__main__":
    main()
      


    