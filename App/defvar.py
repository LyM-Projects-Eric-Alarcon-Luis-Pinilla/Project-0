import keyword as ke


def check(block:list)->bool:
    
    verify = True
    
    if block[0] != "defvar":
        verify = False
    if ke.iskeyword(block[1]) or block[1].isnumeric():
        verify = False
    if not (block[2].isnumeric()):
        verify = False
    
    return verify
