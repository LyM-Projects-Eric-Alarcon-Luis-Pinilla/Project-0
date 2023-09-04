import keyword as ke
import parameter
import procedureblock as procedure


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

    list_parameter = parameter.list_parameter_def(block[2::])
    tuple_par = parameter.check(block,2,"str",-1,list_parameter)
    
    verify = tuple_par[0]
    index = tuple_par[1]
    
    if verify is False:
        return False
    else:
        verify = procedure.check(block[index::],list_parameter)
        
        return verify
    
#prueba = ["defproc","putcb","(","c",",","b",")","{",
        #  "if","can","(","walk","(","1",",","west",")",")","{","walk","(",
         # "1","west",")","}","else","{","nop","(",")","}","}"]



prueba = ["defproc","putcb","(","c",",","b",")","{", 
          "while", "can", "(","walk","(","1",",","west",")",")","{",
          "walk","(","1",",","west",")","}","}"]
print(check(prueba))