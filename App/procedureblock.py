
import simplecom as sc
import model

def sublist_by_command(block:list)->list:
    
    start_pos = 0
    end_pos = 0
    list_of_sublist = []
    
    while end_pos < len(block):
        token = block[end_pos]
        
        if token == "repeat":
            tuple_repeat = sublist_repeat(block[end_pos::])
            if tuple_repeat[1] is None:
                list_of_sublist.append(tuple_repeat[0])
                return list_of_sublist
            end_pos += tuple_repeat[1]
            start_pos = end_pos
            list_of_sublist.append(tuple_repeat[0])
            token = block[end_pos]
        
        if token == ";" and start_pos != end_pos:
            sublist = block[start_pos:end_pos+1]
            list_of_sublist.append(sublist)
            start_pos = end_pos+1
            
        end_pos += 1
            
    sublist = block[start_pos:end_pos+1]
    list_of_sublist.append(sublist)

    return list_of_sublist

def sublist_repeat(block:list)->list:
    
    sublist = []
    counter_close = -1
    start_pos = 0
    end_pos = 0
    flag = True
    
    while end_pos < len(block) and flag:
        token = block[end_pos]
        if token == "}" and counter_close == 0:
            sublist = block[start_pos:end_pos+1]
            flag = False
        if token == "if" or token == "while" or token == "repeat" or token == "else":
            counter_close += 1            
        end_pos += 1
        
    if end_pos == len(block):    
        return sublist,None
    elif block[end_pos] == ";":
        sublist.append(";")
        if end_pos+1 == len(block):
            return sublist,None
        else:
            return end_pos+1
    else:
        return sublist,end_pos
        
        
        
    

def check(block:list,parameters:list)->bool:
        
    i = 0
    flag = True
    
    if block[0] != "{" or block[-1] != "}":
        return False
    
    list_of_commands = sublist_by_command(block[1:len(block)-1])

    while i < len(list_of_commands) and flag:
        
        command = list_of_commands[i]
        if len(command) == 0 or not sc.is_command_present(command[0]):
            if not sc.check_possible_assignment(command):
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


