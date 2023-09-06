import ifconditional as ifc
import procedureblock as proc


def check(block:list,parameters)->bool:
    
    tuple_check_cond = ifc.check_condition(block,parameters,0)
    if tuple_check_cond[0] is False:
        return False
    new_i = tuple_check_cond[1]
    
    if block[-1] == ";":
        verify = proc.check(block[new_i: len(block)-1],parameters)
    else:
        verify = proc.check(block[new_i::],parameters)
    
    return verify


def check_repeat(block:list,parameters:list) -> bool:
    
    if not block[0].isnumeric():
        return False
    if block[1] != "times":
        return False
    if block[-1] == ";":
        verify = proc.check(block[2: len(block)-1],parameters)
    else:
        verify = proc.check(block[2::],parameters)
        
    return verify