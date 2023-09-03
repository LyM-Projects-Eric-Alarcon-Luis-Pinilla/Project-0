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
        pass

    return True
        
