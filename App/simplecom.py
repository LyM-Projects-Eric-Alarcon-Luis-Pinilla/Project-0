import parameter as par
import datatype as dt 
import ifconditional as ifc
import whilecycle
import keywords as ke

regular_command = {
    "jump":{"quantity":2 ,"type": "int"},
    "turn":{"quantity":1 , "type": "str"},
    "turnto":{"quantity":1 , "type": "str"},
    "drop":{"quantity":1 , "type": "int"},
    "get":{"quantity":1 , "type": "int"},
    "grab":{"quantity":1 , "type": "int"},
    "letgo": {"quantity":1 , "type": "int"},
    "nop":{"quantity":0 , "type": "None"},
    }

defined_command = {
        
}

defined_var = []

special_command = ["walk","leap"]

conditional_command = ["if"]

cycle_command = ["while","repeat"]

allowed_D = ["front", "right", "left","back"]
allowed_O= ["north", "south", "west", "east"]


def verify_command(command:list,parameters:list) -> bool:
    
    verify = check_possible_assignment(command)
    
    if command[0] in regular_command:
        verify = check_Regular_Command(command,parameters)
        return verify
    elif command[0] in special_command:
        verify = check_Special_Command(command,parameters)
        return verify
    elif command[0] in conditional_command:
        verify = check_conditional_command(command,parameters)
        return verify 
    elif command[0] in cycle_command:
        verify = check_cycle_command(command,parameters)
    elif command[0] in defined_command:
        verify = check_defined_command(command)
    else:
        return False
    
    return verify
    


def check_Regular_Command(sublist:list,parameters:list)->bool:

    """
    Function: checks if the syntax of the function declaration is correct
    Args: A sublist with the tokenized elements of the command
    Return: True/False if the syntax is correct. 
    """
    
    command_dic = regular_command[sublist[0]]
    verify_parameter = par.check(sublist,1,command_dic["type"],command_dic["quantity"],parameters)
    
    if verify_parameter[0] is False:
        return False
    else:
        last_index = verify_parameter[1]
        if last_index == len(sublist) or (last_index+1 == len(sublist) and sublist[-1] == ";"):
            return True
        else:
            return False
    
def check_Special_Command(sublist:list,parameters:list)->bool:

    """ Aquí se usa un criterio especial para walk y leap"""
    
    verify = walk_leap_possibilities(sublist,parameters)
    
    return verify

def is_command_present(text:str):
    
    if text in (regular_command) or text in special_command or text in conditional_command or text in cycle_command:
        return True
    else:
        return False

def walk_leap_possibilities(command:list,parameters:list)->bool:
    
    inner_parameter = par.list_parameter_def(command[1::])
    num_inner_parameter = len(inner_parameter)
    
    if num_inner_parameter == 1:
        
        if dt.is_value(inner_parameter[0]):
            verify = par.check(command,1,"None",1,parameters)
        else:
            return False
    
    elif num_inner_parameter == 2:
        
        if dt.is_value(inner_parameter[0]):
            if inner_parameter[1] in allowed_D or inner_parameter[1] in allowed_O:
                verify = par.check(command,1,"None",2,parameters)
            else:
                return False
        else:
            return False    
    else:
        return False
    
    return verify

def check_conditional_command(command:list,parameters:list)->bool:

    verify =  ifc.check(command,parameters)
    
    return verify

def check_cycle_command(command:list,parameters:list)->bool:
    
    if command[0] == "while":
        verify = whilecycle.check(command[1::],parameters)
        
    elif command[0] == "repeat":
        verify = whilecycle.check_repeat(command[1::],parameters)
    
    return verify
        

def check_possible_assignment(command:list):
    
    verify = True

    if len(command) > 4 or len(command) < 3:
        return False
    if ke.isKeyWord(command[0]) or command[0].isnumeric():
        return False
    if command[1] != "=":
        return False
    if not (command[2].isnumeric()):
        return False
    
    return verify
        
def check_defined_command(command:list)->bool:
    
    verify_parameter = par.check(command,1,"None",defined_command[command[0]]["quantity"],[])
    
    return verify_parameter[0]

def add_command(name:str,num_par:int)->None:
    
    defined_command[name] = {"quantity":num_par}
    
    pass

def add_var(name:str)->None:
    
    defined_var.append(name)

    pass

def get_var()->list:
    return defined_var



