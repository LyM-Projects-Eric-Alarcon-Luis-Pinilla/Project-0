import keyword as ke
import datatype as dt
import simplecom as smc

def check(block:list)->bool:
    """_summary_

    Args:
        block (list): list with tokens of a defvar block

    Returns:
        bool: True if it satisfies defvar criteria
    """
    
    verify = True
    
    if block[0] != "defvar":
        verify = False
    if not(dt.is_def_value(block[1])):
        verify = False
    if not (dt.is_value(block[2])):
        verify = False
    if verify is True:
        smc.add_var(block[1])
        
    return verify
