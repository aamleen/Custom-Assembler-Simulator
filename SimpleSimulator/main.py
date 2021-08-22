import Operations as op
import operation_file as Op_fl
import Memorydump as mem
import sys

def main():
    prog_in=[]
    for line in sys.stdin:      #takes input from stdin and stores in a list, where each entry(line) is a string 
        prog_in.append(str(line)[0:16])
    pc=0
    #prog_in=["0000000000001010","0000000000001010","0000000000001010","1001100000000000"]
    line=prog_in[pc]
    while(pc<len(prog_in)):
        hlt=line[:5]
        line=prog_in[pc]
        pc=op.calculate(line,pc)
        if(hlt=="10011"):
            break
    mem.dump(prog_in,Op_fl.var)

if __name__ =="__main__":
    main()
      


    