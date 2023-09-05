import keyword as ke
import parameter
import procedureblock as procedure
import simplecom as smc
import datatype as dt


def check(block:list)->bool:
    """_summary_

    Args:
        block (list): List of tokens from the defproc block

    Returns:
        bool: True if it fulfills the defproc criteria
    """
    verify = True
    
    if block[0] != "defproc":
        return False
    if not(dt.is_def_value(block[1])):
        return False
    list_parameter = parameter.list_parameter_def(block[2::])
    
    smc.add_command(block[1],len(list_parameter))
    
    tuple_par = parameter.check(block,2,"str",-1,list_parameter)
    
    verify = tuple_par[0]
    index = tuple_par[1]
    
    if verify is False:
        return False
    else:
        verify = procedure.check(block[index::],list_parameter)
        
        return verify
    
    