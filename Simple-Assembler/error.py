
line_no=[]
var_label={}
def first_run(prog_in):
    last_line=prog_in[-1].split() #Lastline to check halt
    flag=0  #Flag to point if any error
    if(last_line[0]=="hlt"):
        if(len(last_line)!=1):      #if anything else given with hlt
            flag=1
            #ERROR: Invalid declaration of hlt
        else:
            flag_var=0      #to check if var is not present in b/w
            for i in range(len(prog_in)-1):     #Runs till 2nd last line
                line=prog_in[i].split()
                if(line[0]=="var"):
                    if(len(line)==2):
                        if(flag_var==0):
                            if(checkopcode(line[1],i)):
                                flag=1
                                #ERROR: Variable name is an opcode
                                break
                            if(line[1] in var_label):
                                flag=1
                                #ERROR: Label/Variable exists with same name
                                break
                            var_label[line[1]]=["variable",i,bin(i)]    #need to convert to 8 bit
                            
                        else:
                            error(1)
                            flag=1
                            break #variable in between
                    else:
                        #More than 1 variables given
                        flag=1
                elif(line[0][-1]==':'):  
                    flag_var=1
                    if(checkopcode(line[0][:-1],i)):
                        flag=1
                        #ERROR: Label name is opcode
                        break
                    if(line[0][:-1] in var_label):
                        flag=1
                        #ERROR: Label/Variable exists with same name
                        break
                    var_label[line[0]]=["label",i,bin(i)]   #convert to 8 bits
                    if(checkopcode(line[1:]),i):        #checks if instruction given at label is correct
                        continue
                    else:
                        flag=1
                        #Wrong instruction given at label 
                        break
                elif(checkopcode(line,i)):  
                    flag_var=1
                    continue
                elif(line[0]=="hlt"):       #checks if hlt present before last line
                    #ERROR: halt in between
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

        
            




            
            
                




