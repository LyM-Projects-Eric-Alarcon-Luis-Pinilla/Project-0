"""
Funciones que van a entrar: 
name = v 
jump()
walk()
Walk() pero con direccion
walk ()pero con putnros cardinales (norete sur este etc)
leap()
leap ()
leap()
turn
turnto
drop
get
grab
letgo
nop
facing
can
"""

def verify_command(command:list,parameters:list) -> bool:
    pass
    

regular_command_data = {
    "jump":{"Quantity":2 ,"Types": [int,int]},
    "turn":{"Quantity":1 , "Types": [str]},
    "turnto":{"Quantity":1 , "Types": [str]},
    "drop":{"Quantity":1 , "Types": [int]},
    "get":{"Quantity":1 , "Types": [int]},
    "grab":{"Quantity":1 , "Types": [int]},
    "letgo": {"Quantity":1 , "Types": [int]},
    #"nop":{"Quantity":0 , "Types": [None]},
    "facing": {"Quantity":1 , "Types": [str]},
    "can":{"Quantity":1 , "Types": [str]}
    #"not": {"Quantity":1 , "Types": [bool]}
    }

special_command_data = {
    "walk":{"Quantity"},
    "leap": {}


}

allowed_D = ["front", "right", "left","back"]
allowed_O= ["north", "south", "west", "east"]



def commandSyntaxChecker(sublist:list)->bool:


    if sublist[0] == "walk" or sublist[0]== "leap":
        return checkSpecialCommand(sublist)
    else:
        return checkRegularCommand(sublist)





def  checkRegularCommand(sublist:list)->bool:

    """
    Function: checks if the syntax of the function declaration is correct
    Args: A sublist with the tokenized elements of the command
    Return: True/False if the syntax is correct. 
    """
    
    #Checks if the structure of the task starts with kw followed by ( and ends in )
    if sublist[0] not in regular_command_data.keys() or sublist[1]!= "(" or sublist[-1]!= ")":
            return False


    criteriaParameter = regular_command_data[sublist[0]]
    parameters = []
    structure = True
    while structure:

        #Makes a sub-sub list with the parameters so I can check them
            parameters = sublist[2:-1]
            #This function checks that the parameters are correctly indexed.
            if parameterVerifier(parameters, criteriaParameter) !=True:
                structure = False
            else: 
                print("Hola")
                return True
                

    return structure

def checkSpecialCommand(sublist:list)->bool:

    """ Aquí se usa un criterio especial para walk y leap"""


    return 0

def parameterVerifier(paramtoVerify:list, criteria:dict)->bool:
    """
    This function sets a set of rules for all the parameters for the simple commands and checks if they check out
    Args: Parameter to verifu(list) it is a token list with the components inside a parameter instantation
    return : True or false if the parameter lists are well defined. 
    """

    estructParam = True
    while estructParam:
        #This function checks if the parameters are correctly separated by commas
        commas=isSeparatedbyComma(paramtoVerify)
        if commas != True:
            
            return False
        
        num_parameters = correctNumberParameters(paramtoVerify, criteria)
        if  num_parameters!=True:
            
            return False
        
        if correctTypeParamsRegular(paramtoVerify, criteria) != True:
            estructParam = False

        return True
    
    return estructParam





def isSeparatedbyComma(paramtoVerify:list)->bool: 
    #Checks if the first and last elements are ","
    if paramtoVerify[0] == "," or paramtoVerify[-1] == ",":
        return False

    else: 
        num_commas = paramtoVerify.count(",")
        num_Notcommas = sum(1 for token in paramtoVerify if token != ",")
        if num_Notcommas- num_commas ==1:
            return True
        
        return True

def correctNumberParameters(paramtoVerify:list, criteria:dict)->bool:
    

    only_param = [parameter for parameter in paramtoVerify if parameter != ","]
    if len(only_param) == criteria["Quantity"]:
        return True
    
    else:
        return False
    


def correctTypeParamsRegular(paramtoVerify: list, criteria: dict)->bool:
    """This will check if the parameters entered into the  function are coherent to the ones 
    specified on the language for functoins other than walk or leap"""
    
    only_parameters = [parameter for parameter in paramtoVerify if parameter != ","]
    criteria_types = criteria["Types"]

    fixed_parameters = []

    for p in only_parameters:
        try:
            p_int = int(p)
            fixed_parameters.append(p_int)
        
        except ValueError:
            fixed_parameters.append(p)



    for c in range(0,len(fixed_parameters)):
        if type(fixed_parameters[c])!= criteria_types[c]:
            return False
        else:
            if type(fixed_parameters[c]) == str: 
                if fixed_parameters not in allowed_D or fixed_parameters not in allowed_O: 
                    return False

    return True

##############################
##############################

""""prueba = ["drop","(","x",")"]"""
"print(commandSyntaxChecker(prueba))"












