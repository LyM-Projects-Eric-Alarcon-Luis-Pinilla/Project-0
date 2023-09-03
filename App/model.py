import regex as re 
import keywords as key
import defvar
import defproc
import block


def verify_code(text:str)->bool:  
    """Main Function

    Args:
        text (string): the code in form of text

    Returns:
        _boolean: True/False 
    """
    tokenizer = tokenize(text)
    list_of_components = create_blocks(tokenizer)
    
    if list_of_components is None:
        return False
    else:
        individual_verification(list_of_components)
    return True

def individual_verification(list_of_components):
    
    flag = True
    i = 0
    while i < len(list_of_components) and flag:
        
        blocks = list_of_components[i]
        if key.clasificadorKeyWord(blocks[0]) == 1:
            flag = defvar.check()
        if key.clasificadorKeyWord(blocks[0]) == 2:
            flag = defproc.check()
        if key.clasificadorKeyWord(blocks[0]) == 3:
            flag = block.check()
        i +=1
        
    return flag

def tokenize(text:str)->list:
    """_summary_

    Args:
        text (str): one string of the whole txt

    Returns:
        list: tokenized list
    """
    
    raw_list = re.split("\s",text)
    tokenized_list = []
    
    for token in raw_list:
        token = token.lower()
        
        if token!= "":
            if has_separator(token):
                sub_token = ""
                for small_token in token:
                    if (small_token == "(" or small_token == "{") and sub_token == "":
                        tokenized_list.append(small_token)
                        if len(sub_token) != 0:
                            tokenized_list.append(sub_token)
                            sub_token = ""
                    elif (small_token == ")" or small_token == "}") or ((small_token == "(" or small_token == "{") and sub_token != ""):
                        if len(sub_token) != 0:
                            tokenized_list.append(sub_token)
                            sub_token = ""
                        tokenized_list.append(small_token)
                    else:
                        sub_token += small_token    
                        
                if len(sub_token) != 0:
                            tokenized_list.append(sub_token)
                            sub_token = ""      
            else:
                tokenized_list.append(token)

    return tokenized_list

def has_separator(token:str)->bool:
    """_summary_

    Args:
        token (str): Any token in form of str

    Returns:
        bool: Returns if a separator is present in the token
    """
    
    if ("(") in token or (")") in token or ("{") in token or ("}") in token:
        return True
    else:
        return False
    
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
    
