import check_bind_opcode as f1
var_label={}    #stores variable name, labels
def first_ru(prog_in):
    last_line=prog_in[-1].split() #Lastline to check halt
    flag=0  #Flag to point if any error
    if(last_line[0]=="hlt"):
        if(len(last_line)!=1):      #if anything else given with hlt 
            print("ERROR at line",(len(prog_in)-1),": Invalid declaration of hlt")
            flag=1
        else:
            flag_var=0      #to check if var is not present in b/w
            for i in range(len(prog_in)-1):     #Runs till 2nd last line
                line=prog_in[i].split()
                print(line)
                if(line[0]=="var"):
                    if(len(line)==2):
                        if(flag_var==0):
                            if(f1.checkopcode(line[1],i)):
                                #ERROR: Variable name is an opcode
                                print("ERROR at line",i,": Variable name is an opcode")
                                flag=1
                                break
                            if(line[1] in var_label):
                                #ERROR: Label/Variable exists with same name
                                print("ERROR at line",i,": Label/Variable exists with same name")
                                flag=1
                                break
                            var_label[line[1]]=["variable",i,str(bin(i+len(prog_in)-1))[2:]]    
                            
                        else:
                            #ERROR: variable in between
                            print("ERROR at line",i,": Variable declared in between the code")
                            flag=1
                            break 
                    else:
                        #More than 1 variables given
                        #ERROR: Illegal declaration of variable ---------------------okay?
                        print("ERROR at line",i,": More than one variables given")
                        flag=1
                        break

                elif(line[0][-1]==':'):  
                    flag_var=1
                    if(f1.checkopcode(line[0][:-1],i)):
                        #ERROR: Label name is opcode
                        print("ERROR at line",i,": Label name is opcode")
                        flag=1
                        break
                    if(line[0][:-1] in var_label):
                        #ERROR: Label/Variable exists with same name
                        print("ERROR at line",i,": Label/Variable exists with same name")
                        flag=1
                        break
                    var_label[line[0]]=["label",i,str(bin(i))[2:]]   #convert to 8 bits
                    if(f1.checkopcode(line[1:]),i):        #checks if instruction given at label is correct
                        continue
                    else:
                        #Wrong instruction given at label 
                        print("ERROR at line",i,": Wrong instruction given at label")
                        flag=1
                        break
                elif(f1.checkopcode(line,i)):  
                    flag_var=1
                    continue
                elif(line[0]=="hlt"):       #checks if hlt present before last line
                    #ERROR: halt in between
                    print("ERROR at line",i,": halt operation used in between")
                    flag=1
                    break
                else:
                    #Error in opcode/label/var naming
                    print("ERROR at line",i,": Error in opcode/label/variable naming")
                    flag=1
                    break
            f1.list_of_upcodesandtype.append(["10011","F"])
    else:
        print("ERROR at line",i,": Halt operation missing")
        flag=1
        
    return flag

        
            




            
            
                




