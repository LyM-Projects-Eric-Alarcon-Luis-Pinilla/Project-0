import procedureblock as pb
import simplecom as sc

allowed_D = ["front", "right", "left","back"]
allowed_O= ["north", "south", "west", "east"]
conditional_command = ["can","facing","not"]


def check(command:list,parameters:list)->bool:
    
    verify = True
    
    if command[0] != "if":
        return False
    
    tuple_cond_check = check_condition(command,parameters,1)
    if tuple_cond_check[0] is False:
        return False
    new_i = tuple_cond_check[1]
    
    if command[new_i] != ")":
        return False
    new_i +=1
    
    tuple_block_check = submit_block(command[new_i::],parameters)
    if tuple_block_check[0] is False:
        return False
    new_i += tuple_block_check[1]
    
    if command[new_i] != "else":
        return False
    
    tuple_else_check = submit_block(command[new_i+1::],parameters)
    
    if tuple_else_check[0] is False:
        return False
        
    new_i += tuple_else_check[1] + 1
    
    return verify

def check_can_not(command:list,parameters:list)->tuple:
    
    pos = 1
    flag = True
    
    if command[0] != "(":
        return False
    
    while pos < len(command) and flag:
        
        token = command[pos]
        if token == ")":
            simple_com = command[1:pos+1]
            flag = False
            
        pos +=1
        
    verify = sc.verify_command(simple_com,parameters)[0]
    
    return verify,pos
    
def check_facing(command:list)->bool:
    
    if command[2] != "(":
        return False
    if command[3] not in allowed_O:
        return False
    if command[4] != ")":
        return False
    else:
        return True
    
def submit_block(command:list,parameters:list)->tuple:
   
    pos = 0
    flag = True
    
    while pos < len(command) and flag:
        token = command[pos]
        if token == "}":
            simple_com = command[0:pos+1]
            flag = False
            
        pos +=1
        
        
    verify = pb.check(simple_com,parameters)
    
    return verify,pos

def check_condition(command:list,parameters:list,start_word:int)->tuple:
    
    verify = True
    
    if command[start_word] in conditional_command:
        
        if command[start_word] == "can" or command[start_word] == "not":
            tuple_check = check_can_not(command[start_word+1::],parameters)
            if tuple_check[0] is False:
                return False,0
            new_i = tuple_check[1] + 2
        
        elif command[1] == "facing":
            if check_facing(command) is False:
                return False,0
            new_i = 5
    else:
        return False,0
    
    return verify,new_i
    
    