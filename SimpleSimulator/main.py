import Operations as op
import operation_file as Op_fl
import Memorydump as mem
import sys
import matplotlib.pyplot as plt

def main():
    prog_in=[]
    for line in sys.stdin:      #takes input from stdin and stores in a list, where each entry(line) is a string 
        prog_in.append(str(line)[0:16])
    pc=0
    #prog_in=["0000000000001010","0000000000001010","0000000000001010","1001100000000000"]
    cycle=0
    line=prog_in[pc]
    while(pc<len(prog_in)):
        hlt=line[:5]
        line=prog_in[pc]
        temp_pc=op.calculate(line,pc)
        bonus(cycle, pc, line)
        cycle+=1
        if(hlt=="10011"):
            break
        pc=temp_pc
    mem.dump(prog_in,Op_fl.var)
    bonus_plot()

x_cycle=[]
y_mem=[]

def bonus(cyc,mem,line):
    global x_cycle
    global y_mem
    x_cycle.append(cyc)
    y_mem.append(mem)
    if(line[0:5]=="00100" or line[0:5]=="00101"):
        x_cycle.append(cyc)
        y_mem.append(int(line[8:16],2))

def bonus_plot():
    plt.scatter(x_cycle,y_mem)
    plt.xlabel("cycles ->")
    plt.ylabel("Memory Address ->")
    plt.title("Mem Addr vs Cycle No.")
    plt.savefig("Bonus_Image.png")

if __name__ =="__main__":
    main()
      


    