
import simplecom as sc

def sublist_by_command(block:list)->list:
    
    start_pos = 0
    end_pos = 0
    list_of_sublist = []
    
    while end_pos < len(block):
        token = block[end_pos]
        
        if token == ";":
            sublist = block[start_pos:end_pos+1]
            list_of_sublist.append(sublist)
            start_pos = end_pos+1
            
        end_pos += 1
            
    sublist = block[start_pos:end_pos+1]
    list_of_sublist.append(sublist)

    return list_of_sublist

def check(block:list,parameters:list)->bool:
        
    i = 0
    flag = True
    
    if block[0] != "{" or block[-1] != "}":
        return False
    
    list_of_commands = sublist_by_command(block[1:len(block)-1])

    while i < len(list_of_commands) and flag:
        
        command = list_of_commands[i]
        if len(command) == 0 or not sc.is_command_present(command[0]):
            print(command)
            return False
        if sc.verify_command(command,parameters):
            i +=1
        else:
            print(command)
            flag = False
        if i-1 != len(list_of_commands)-1 and command[-1] != ";":
            print(command)
            flag = False
        elif i-1 == len(list_of_commands)-1 and command[-1] == ";":
            print(command)
            flag = False
    
    return flag


