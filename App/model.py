import regex as re 
import keywords as key
import defvar
import defproc
import procedureblock as bl
import tokenizer as tk


def verify_code(text:str)->bool:  
    """Main Function

    Args:
        text (string): the code in form of text

    Returns:
        _boolean: True/False 
    """
    tokenizer = tk.tokenize(text)
    list_of_components = create_blocks(tokenizer)
    
    if list_of_components is None:
        return False
    else:
        verify = individual_verification(list_of_components)
    return verify

def individual_verification(list_of_components:list)->bool:
    
    """_summary_
    Args:
        list of componentes: list of sublists which are blocks of commands or procedure

    Returns:
        flag(bool): if each of the blocks has a correct syntax is True else False.
    """
    
    flag = True
    i = 0
    while i < len(list_of_components) and flag:
        
        block = list_of_components[i]
        if key.clasificadorKeyWord(block[0]) == 1:
            flag = defvar.check(block)
        if key.clasificadorKeyWord(block[0]) == 2:
            flag = defproc.check()
        if key.clasificadorKeyWord(block[0]) == 3:
            flag = bl.check()
        i +=1
        
    return flag
    
def block_def_var(i,tokenizer)->tuple:
    
    """_summary_

    Returns:
        _tuple: The firs element is a list of the block defvar, second element is the
        new position where the tokenizer will start reading again.
    """
    
    sublist = []
    new_i = i+3
    
    for pos in range(i,new_i):
        sublist.append(tokenizer[pos])

    return sublist,new_i


def block_commandProc(i,tokenizer)->tuple:
    
    """_summary_

    Returns:
        tuple: The firs element is a list of the block defproc or a block of command {}, second element is the
        new position where the tokenizer will start reading again.
    """
    sublist = []
    counter_close = 0
    counter_open = 1
    new_i = i+1
    flag = True
    
    while i < len(tokenizer) and flag:
        token = tokenizer[new_i]
            
        if token == "if" or token == "while" or token == "else":
            counter_close += 1
            counter_open += 1
        
        if token == "defvar" or token == "defproc":
            sublist = tokenizer[i:new_i]
            flag = False
            
        elif token == "{":
            if counter_open == 0:
                sublist = tokenizer[i:new_i]
                flag = False
            else:
                counter_open -= 1
        
        elif token == "}":
            if counter_close == 0:
                sublist = tokenizer[i:new_i+1]
                flag = False
            else:
                counter_close -= 1
        
        new_i += 1
        
    return sublist,new_i

def create_blocks(tokenizer:list) -> list:
    """_summary_

    Args:
        tokenizer (list): List of tokens
    Returns:
        list: List where each element is a sublist of the blocks of command
        such as defvar, defproc and {}
    """
    
    list_of_components = []
    flag = True
    i = 0

    while i < len(tokenizer) and flag:
        
        if key.isKeyWord(tokenizer[i]):
            
            if tokenizer[i] == "defvar":
                tuple = block_def_var(i,tokenizer)
            else:
                tuple = block_commandProc(i,tokenizer)
            
            sublist = tuple[0]
            i = tuple[1]
            list_of_components.append(sublist)
                
        else:
            list_of_components = None
            flag = False
        
        
    return list_of_components    
