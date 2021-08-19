def main():
    prog_in=[]
    for line in sys.stdin:      #takes input from stdin and stores in a list, where each entry(line) is a string 
        prog_in.append(str(line))
    pc=0
    for line in prog_in:
        hlt=line[:5]
        if(hlt=="10011"):
            break

        pc=Operations.calculate(line)  
        
    