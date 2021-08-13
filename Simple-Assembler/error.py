
line_no=[]    #?????
var_label={}    #?????
def first_run(prog_in):
    last_line=prog_in[-1].split() #Lastline to check halt
    flag=0  #Flag to point if any error
    if(last_line[0]=="hlt"):
        if(len(last_line)!=1):      #if anything else given with hlt
            #ERROR: Invalid declaration of hlt
            error(13,line_no) #**************Here don't know the variable for line number
            flag=1
            break 
            
        else:
            flag_var=0      #to check if var is not present in b/w
            for i in range(len(prog_in)-1):     #Runs till 2nd last line
                line=prog_in[i].split()
                if(line[0]=="var"):
                    if(len(line)==2):
                        if(flag_var==0):
                            if(checkopcode(line[1],i)):
                                #ERROR: Variable name is an opcode
                                error(14,line_no) #****************************
                                flag=1
                                break
                            if(line[1] in var_label):
                                #ERROR: Label/Variable exists with same name
                                error(6,line_no)
                                flag=1
                                break
                            var_label[line[1]]=["variable",i,bin(i)]    #need to convert to 8 bit
                            
                        else:
                            #ERROR: variable in between
                            error(15,line_no)
                            flag=1
                            break 
                    else:
                        #More than 1 variables given
                        #ERROR: Illegal declaration of variable ---------------------okay?
                        error(16,line_no)
                        flag=1
                        break

                elif(line[0][-1]==':'):  
                    flag_var=1
                    if(checkopcode(line[0][:-1],i)):
                        #ERROR: Label name is opcode
                        #VS COde not pointing out any errors.......................
                        error(17,line_no)
                        flag=1
                        break
                    if(line[0][:-1] in var_label):
                        #ERROR: Label/Variable exists with same name
                        #Misuse of labels as variables??????????????????/
                        error(6,line_no)
                        flag=1
                        break
                    var_label[line[0]]=["label",i,bin(i)]   #convert to 8 bits
                    if(checkopcode(line[1:]),i):        #checks if instruction given at label is correct
                        continue
                    else:
                        #Wrong instruction given at label 
                        #error 10?????????????????????????????????
                        error(10,line_no)
                        flag=1
                        break
                elif(checkopcode(line,i)):  
                    flag_var=1
                    continue
                elif(line[0]=="hlt"):       #checks if hlt present before last line
                    #ERROR: halt in between
                    error(9,line_no)
                    flag=1
                    break
                else:
                    #Error in opcode/label/var naming
                    #14 and 17 both satisfy it...........................
                    error(14,line_no) 
                    error(17,line_no)
                    flag=1
                    break
    else:
        #hlt not present or invalid
        error(8,line_no)
        flag=1
        
    return flag

        
            




            
            
                




