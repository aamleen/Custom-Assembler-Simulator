def 

def first_run(overall):
    int i=0
    for i in range(len(overall)):
        line=overall[i].split()
        flag_var=0

        if(line[0]=="var"):
            if(flag_var==0):
                var_label[line[1]]=["variable",i,bin(i)]
            else:
                error(1)
        elif(line[0][-1]=='.'):
            flag_var=1
            var_label[line[0]]=["label",i,bin(i)]
        elif(checkopcode(line[0])):
            




            
            
                




