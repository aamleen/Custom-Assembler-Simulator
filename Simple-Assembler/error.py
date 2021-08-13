
line_no=[]
def first_run(prog_in):
    last_line=prog_in[-1].split()
    if(last_line[0]=="hlt"):
        if(len(last_line)!=1):
            flag=1
            #Invalid declaration of hlt
        else:
            for i in range(len(prog_in)-1):
                line=prog_in[i].split()
                flag_var=0
                if(line[0]=="var"):
                    if(len(line)==2):
                        if(flag_var==0):
                            var_label[line[1]]=["variable",i,bin(i)]
                            line_no.append("variable")
                        else:
                            error(1)
                            flag=1
                            break #variable in between
                    else:
                        #More than 1 variables given
                        flag=1
                elif(line[0][-1]==':'):  
                    flag_var=1
                    var_label[line[0]]=["label",i,bin(i)]
                    line_no.append("label")
                    if(checkopcode(line[1:]),i):
                        continue
                    else:
                        #Wrong instruction given at label 
                        pass
                elif(checkopcode(line,i)):  
                    flag_var=1
                    line_no.append("opcode")
                    continue
                elif(line[0]=="hlt"):
                    #halt in between
                    flag=1
                    break
                else:
                    #Error in opcode/label/var naming
                    flag=1
                    break
    else:
        #hlt not present or invalid
        flag=1

    return flag

        
            




            
            
                




