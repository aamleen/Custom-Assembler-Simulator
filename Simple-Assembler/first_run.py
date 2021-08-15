import check_bind_opcode as f1
var_label={}    #variable name: [variable/label, line no., mem_addr]

mem_addr=0      #stores memory address of each line

def first_ru(prog_in):
    last_line=prog_in[-1].split() #Lastline to check halt
    flag=0  #Flag to point if any error
    if("hlt" in last_line):
        if(len(last_line)==1):      #if anything else given with hlt 
            flag=check_error(prog_in)
        elif(len(last_line)==2 and last_line[0][-1]==":"):
            label_name=[]
            label_name.append(last_line[0][:-1])
            if(f1.checkopcode(label_name,len(prog_in))):
                flag=1
                print("ERROR at line",len(prog_in),"Label name is an opcode")
            else:
                flag=check_error(prog_in)
                var_label[label_name[0]]=["label",len(prog_in)-1,str(bin(mem_addr))[2:]]
        else:
            print("ERROR at line",(len(prog_in)),": Invalid declaration of hlt")
            flag=1
        f1.list_of_upcodesandtype.append(["10011","F"])
    else:
        print("ERROR at line",len(prog_in),": Missing hlt instruction")
        flag=1
    if(flag==0):
        var_addr()
    return flag

def check_error(prog_in):       #checks error from 1st till 2nd last line
    flag_var=0      #to check if var is not present in b/w
    flag=0
    global mem_addr
        
    for i in range(len(prog_in)-1):     #Runs till 2nd last line
        line=prog_in[i]
        if(line=='' or line=='\n'):     #Skipping the empty lines
            continue
        line=line.split()
        if(line[0]=="var"):
            if(len(line)==2):
                if(flag_var==0):
                    var_name=[]
                    var_name.append(line[1])
                    if(f1.checkopcode(var_name,i+1)):
                        #ERROR: Variable name is an opcode
                        print("ERROR at line",i+1,": GENERAL SYNTAX ERROR: Variable name is an opcode")
                        flag=1
                        break
                    if(line[1] in var_label):
                        #ERROR: Label/Variable exists with same name
                        print("ERROR at line",i+1,": GENERAL SYNTAX ERROR: Label/Variable exists with same name")
                        flag=1
                        break
                    if ((line[1].isdigit()==False) and (line[1].isalnum() or '_' in line[1])):
                        var_label[line[1]]=["variable",i,str(bin(len(prog_in)))[2:]]
                    else:
                        flag=1
                        print("ERROR at line",i+1,"GENERAL SYNTAX ERROR: Variable Naming incorrect")
                        break
                else:
                    #ERROR: variable in between
                    print("ERROR at line",i+1,": Variables not declared at the beginning")
                    flag=1
                    break 
            else:
                #More than 1 variables given
                #ERROR: Illegal declaration of variable ---------------------okay?
                print("ERROR at line",i+1,": GENERAL SYNTAX ERROR: Illegal Declaration of variables")
                flag=1
                break

        elif(line[0][-1]==':'):  
            flag_var=1
            label_name=[]
            label_name.append(line[0][:-1])
            if(f1.checkopcode(label_name,i+1)):
                #ERROR: Label name is opcode
                print("ERROR at line",i+1,": GENERAL SYNTAX ERROR: Label name is opcode")
                flag=1
                break
            if(label_name[0] in var_label):
                #ERROR: Label/Variable exists with same name
                print("ERROR at line",i+1,": Label/Variable exists with same name")
                flag=1
                break
            if(len(line)==2 and line[1] == "hlt"):
                flag=1
                print("ERROR at line",i+1,": hlt not being used as the last instruction")
                break
            elif(f1.checkopcode(line[1:],i+1)):        #checks if instruction given at label is correct
                var_label[label_name[0]]=["label",i,str(bin(mem_addr))[2:]]
                mem_addr+=1
                continue
            else:
                #Wrong instruction given at label 
                print("ERROR at line",i+1,": Wrong instruction given at label")
                flag=1
                break
        elif(f1.checkopcode(line,i+1)):  
            flag_var=1
            mem_addr=mem_addr+1
            continue
        elif(line[0]=="hlt"):       #checks if hlt present before last line
            #ERROR: halt in between
            print("ERROR at line",i+1,": hlt not being used as the last instruction")
            flag=1
            break
        else:
            if(f1.err_print==1):    #Error has already been printed
                flag=1
                break
            #Error in opcode/label/var naming
            print("ERROR at line",i+1,": Error in opcode/label/variable naming")
            flag=1
            break
    return flag

def var_addr():      #allots the memory of variables after halt
    global mem_addr
    for i in var_label:
        if(var_label[i][0]=="variable"):
            mem_addr+=1
            var_label[i][2]=str(bin(mem_addr))[2:]
                