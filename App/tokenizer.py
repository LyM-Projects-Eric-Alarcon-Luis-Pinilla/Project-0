import regex as re

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
                    elif small_token == ",":
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