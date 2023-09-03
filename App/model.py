import regex as re 


def verify_code(text:str)->bool:  
    """Main Function

    Args:
        text (string): the code in form of text

    Returns:
        _boolean: True/False 
    """
    tokenizer = tokenize(text)
    
    return True

def tokenize(text:str)->list:
    
    raw_list = re.split("\s",text)
    tokenized_list = []
    
    for token in raw_list:
        
        if token!= "":
            if has_separator(token):
                pass
                
            else:
                tokenized_list.append(token)
        
        
        pass

    return True

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
