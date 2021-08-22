def dump(prog_in,var):
    i=len
    print(*prog_in,sep="\n")
    print(*(var.keys()),sep="\n")
    total_lines=len(prog_in)+len(var)
    while(total_lines<256):
        print("0000000000000000")
        total_lines+=1