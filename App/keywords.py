#Esta funcion es necesaria para asegurarse de que el token esté bien escrito, y para clasificarlos 
#para saber a qué tipo de 

def isKeyWord(token:str)-> bool:
  """
  Function: tells if a token is one of the main commands and should be treated different:
  defVar, defProc, { 
  Args: token to be evaluated
  Returns: True or False 
  """
  token = token.lower
  keys = ["defVar", "defProc", "{"]
  
  if token in keys:
        return True
  
  else: 
      return False



def clasificadorKeyWord (token:str)->int:
    """Main Function
    Recieves a string and will check if it is a KeyWord from the language: defVar, defProc, { 
        (if it is misspelled then it wont process it)
 
    Args:
        token (string): the token to evaluate
    Returns:
        int: type of KeyWord it is 
            1 => defproc, 
            2=>defvar
            3=> {
    """

    token = token.lower()
   
    if token == "defvar":
        return 1
    if token == "defproc":
        return 2
    
    if token == "{":
        return 3

        

    return False









