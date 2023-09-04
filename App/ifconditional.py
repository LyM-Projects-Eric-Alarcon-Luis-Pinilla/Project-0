import procedureblock as pb
import simplecom as sc

allowed_D = ["front", "right", "left","back"]
allowed_O= ["north", "south", "west", "east"]
conditional_command = ["can","facing","not"]

def check(command:list,parameters:list)->bool:
    
    if command[0] != "if":
        return False
    
    if command[1] in conditional_command:
        
        if command[1] == "can" or command[1] == "not":
            tuple_check = check_can_not(command,parameters)
            if tuple_check[0] is False:
                return False
            new_i = tuple_check[1]
        
        elif command[1] == "facing":
            if check_facing(command) is False:
                return False
            new_i = 5
    else:
        return False
    
    
    
    pass

def check_can_not(command:list,parameters:list)->bool:
    
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
        
    verify = sc.verify_command(simple_com,parameters)
    
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
    
def submit_bloc(command:list,parameters:list):
   
    pos = 1
    flag = True
    
    while pos < len(command) and flag:
        token = command[pos]
        if token == "}":
            simple_com = command[1:pos+1]
            flag = False
            
        pos +=1
    pass