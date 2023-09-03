import regex as re 
import keywords as key


def verify_code(text:str)->bool:  
    """Main Function

    Args:
        text (string): the code in form of text

    Returns:
        _boolean: True/False 
    """
    tokenizer = tokenize(text)
    print(tokenizer)
    print("\nFinished tokenizing the txt..... \n\n")
    list_of_components = create_blocks(tokenizer)
    
    return True

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
                    if has_separator(small_token):
                        tokenized_list.append(small_token)
                        if len(sub_token) != 0:
                            tokenized_list.append(sub_token)
                            sub_token = ""   
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
    
def block_def_var(i,tokenizer):
    
    sublist = []
    new_i = i+3
    
    for pos in range(i,new_i):
        sublist.append(tokenizer[pos])
    
    
    
    return sublist,new_i

def block_commandProc(i,tokenizer):
    
    sublist = []
    counter_close = 1
    new_i = i+1
    
    while i < len(tokenizer):
        token = tokenizer[i]
        if token:
            pass
        
        
    
    return 0,i

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
    
