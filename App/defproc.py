import keyword as ke
import parameter

def check(block:list)->bool:
    """_summary_

    Args:
        block (list): List of tokens from the defproc block

    Returns:
        bool: True if it fulfills the defproc criteria
    """
    verify = True
    
    if block[0] != "defproc":
        verify = False
    if ke.iskeyword(block[1]) or block[1].isnumeric():
        verify = False
    
    tuple_par = parameter.check(block)
    verify = tuple_par[0]
    index = tuple_par[1]
    
    if verify is False:
        return False
    else:
        return True
    