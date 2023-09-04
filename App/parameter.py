import datatype as dt
import keywords as ke
 
 
def structure_parameter(sublist:list,num_parameter:int, type_parameter:str,variables:list)->bool:
    
    """_summary_
    Args:
        sublist(list): list of tokens that are between () in a defproc statemente

    Returns:
        verify(bool): True if the list fulfills the parameters criteria
    """
        
    verify = True
    pos = 1
    count_parameter = 0
    
    if sublist[0] != "(" or sublist[-1] != ")":
        return False
    
    while pos < len(sublist)-1 and verify:
        token = sublist[pos]
        
        if (pos == len(sublist)-2) and (not dt.is_def_value(token) or token == ","):
            verify = False
        elif pos%2 == 1: 
            if (not dt.is_def_value(token)):
                verify = False
                
            elif type_parameter == "int":
            
                if not(token.isnumeric()):
                    if token not in variables:
                        verify = False
            count_parameter += 1
    
        elif pos%2 == 0 and token != ",":
            verify = False 
        pos += 1
        
    if num_parameter != -1 and count_parameter != num_parameter:
        verify = False
        
    return verify


def check(parameters:list,start:int,type_parameter:str,num_parameter:int,variables:list)->tuple:
    
    """_summary_
    Args:
        paramteres(list): the full list of the command block
    Returns:
        (tuple): First value is a boolean that tells if the parameters criteria is fulfilled
        and the Second value is the new position where the parameters end in the tokenizer. 
        None if the program has error in the parameters.    
    """
    start_pos = start
    end_pos = start
    flag = True
    sublist = []
    
    while end_pos < len(parameters) and flag:
        
        token = parameters[end_pos]
        if token == ")":
            sublist = parameters[start_pos : end_pos+1]
            flag = False
        elif flag:
            end_pos +=1
                
    if len(sublist) != 0:
        verify = structure_parameter(sublist,num_parameter,type_parameter,variables)
        return verify,end_pos+1
    else:
        return False,None
    
def list_parameter_def(sublist:list)->list:
    
    i = 0
    flag = True
    parameter_list = []
    
    while i < len(sublist) and flag:
        token = sublist[i]
        
        if token == ")":
            flag = False
        
        elif token != "," and token != "(":
            parameter_list.append(token)
            
        i += 1
        
    return parameter_list
    
   
   
   