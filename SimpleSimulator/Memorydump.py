def dump(prog_in,var):
    i=len
    for i in list(var.values()):
        prog_in.append(get_nbit(str(bin(i))[2:],16))

    print(*prog_in,sep="\n")
    total_lines=len(prog_in)
    while(total_lines<256):
        print("0000000000000000")
        total_lines+=1

def get_nbit(numst,n): # converting 1001 into 00001001 basically completing n-digits 
    st_len = n-len(numst)
    if st_len >=0:
        st_fin = "0"*st_len
        st_fin = st_fin + numst
        return st_fin
    else:
        return None