import datatype as dt
 
 
def structure_parameter(sublist:list)->bool:
    
    """_summary_
    Args:
        sublist(list): list of tokens that are between () in a defproc statemente

    Returns:
        verify(bool): True if the list fulfills the parameters criteria
    """
        
    verify = True
    pos = 1
    
    if sublist[0] != "(" or sublist[-1] != ")":
        return False
    
    while pos < len(sublist)-1 and verify:
        token = sublist[pos]
        
        if (pos == len(sublist)-2) and (not dt.is_def_value(token) or token == ","):
            verify = False
        elif pos%2 == 1 and (not dt.is_def_value(token)):
            verify = False
        elif pos%2 == 0 and token != ",":
            verify = False 
        pos += 1
        
    return verify


def check(parameters:list)->tuple:
    
    """_summary_
    Args:
        paramteres(list): the full list of the command block
    Returns:
        (tuple): First value is a boolean that tells if the parameters criteria is fulfilled
        and the Second value is the new position where the parameters end in the tokenizer. 
        None if the program has error in the parameters.
    """
    start_pos = 2
    end_pos = 2
    flag = True
    sublist = []
    
    while end_pos < len(parameters) and flag:
        
        token = parameters[end_pos]
        if token == ")":
            sublist = parameters[start_pos : end_pos+1]
        end_pos +=1
                
    if len(sublist) != 0:
        verify = structure_parameter(sublist)
        return verify,end_pos+1
    else:
        return False,None
    
   
   
   