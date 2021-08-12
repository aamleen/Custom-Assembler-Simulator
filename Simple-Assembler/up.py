## incoding
## [opcode , no. of register ,imm value ,mem addrs, type ]
## cant take upcode as key cuz we have 2 mov commands but with different arguments
## hey yash
dc = {00000 : [ "add", 3, 0 ,0,"A"] ,
1  : ["sub" , 3 , 0 ,0,"A"] ,
10 : ["mov" , 1 , 1 ,0,"B"],
11 : [ "mov" , 2 , 0 ,0, "C"],
100 : ["ld" , 1 , 0 , 1, "D"],
101 : ["st ", 1 , 0 ,1,"D"],
110 : ["mil" , 3 , 0,0 ,"A"],
111 : ["div " , 2 , 0 , 0 , "C"],
1000: ["rs" , 1 , 1, 0 , "B"],
1001: ["ls" , 1 , 1 , 0 , "B"],
1010: ["xor" , 3 ,0,0 , "A"],
1011:["or" , 3 , 0 , 0 , "A"],
1100:["and", 3 , 0 , 0 , "A"],
1101:["not" , 2 , 0 , 0 , "C"],
1110:["cmp" , 2 , 0 , 0 , "C"],
1111:["jmp" , 0 , 0 , 1 , "E"],
10000:["jlt" , 0 , 0 , 1 , "E"],
10001:["jgt" , 0 , 0 , 1 , "E"],
10010:["je" , 0 , 0 , 1 , "E"],
10011:["hlt" , 0 , 0 , 0 , "F"],


}   