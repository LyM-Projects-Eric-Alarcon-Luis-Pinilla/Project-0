import keyword as ke

def is_def_value(token:str)->bool:
    
    """_summary_

    Returns:
        verify (bool): True if the token can be the name of a variable or funcition
    """
    
    verify = True
    
    if ke.iskeyword(token) or not(token.isalnum()) or token[0].isnumeric():
        verify = False
    
    return verify

def is_value(token:str)->bool:
    """_summary_

    Args:
        token (str): any token

    Returns:
        verify (bool): True if the token is a number in str format. 
    """

    return token.isnumeric()

def is_value_parameter(token:str)->bool:
    
    verify = True
    
    if ke.iskeyword(token):
        verify = False
        
    return verify