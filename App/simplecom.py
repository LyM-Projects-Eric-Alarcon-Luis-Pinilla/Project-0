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


allowed_D = ["front", "right", "left","back"]
allowed_O= ["north", "south", "west", "east"]



def commandSyntaxChecker(sublist:list)->bool:


    if sublist[0] == "walk" or sublist[0]== "leap":
        checkSpecialCommand(sublist)
    else:
        checkRegularCommand(sublist)





def checkRegularCommand(sublist:list)->bool:

    """
    Function: checks if the syntax of the function declaration is correct
    Args: A sublist with the tokenized elements of the command
    Return: True/False if the syntax is correct. 
    """
    
    criteriaParameter = {"Quantity":2, "Types": (int,int)}
    parameters = []
    structure = True
    while structure:

        #Checks if the structure of the task starts with kw followed by ( and ends in )
        if sublist[0] != "jump" or sublist[1]!= "(" or sublist[-1]!= ")":
            structure = False
        #Makes a sub-sub list with the parameters so I can check them
        elif sublist[1] == "(":
            parameters = sublist[2:-1]
            #This function checks that the parameters are correctly indexed.
            if parameterVerifier(parameters, criteriaParameter) !=True:
                structure = False
            else: 
                print("hasta aquihemos revisado que abra y cierrre con parentessis y que los parametros estén separados por coma")

            

    return structure

def checkSpecialCommand(sublist:list)->bool:

    """ Aquí se usa un criterio especial para walk y leap"""


    return 0

def parameterVerifier(paramtoVerify:list, criteria:dict)->bool:
    """
    This function sets a set of rules for all the parameters for the simple commands and checks if they check out
    """

    estructParam = True
    while estructParam:
        #This function checks if the parameters are correctly separated by commas
        if isSeparatedbyComma(paramtoVerify) != True:
            estructParam = False
        
        if correctNumberParameters(paramtoVerify, criteria) !=True:
            estructParam = False
        
        if correctTypeParams(paramtoVerify, criteria) != True:
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
    


def correctTypeParams(paramtoVerify: list, criteria: dict)->bool:
    
    only_parameters = [parameter for parameter in paramtoVerify if parameter != ","]
    print(only_parameters)
    
    return 0

##############################
##############################

prueba = ["jump","(","x",",","y",")"]
print(checkRegularCommand(prueba))












