import model

def load_data(filename):
    
    file = open(f"Data/{filename}","r",encoding="utf-8")  
    text = file.read()

    return text

""" 
Verify returns TRUE or FALSE 
"""

def verify(text):
    return model.verify_code(text)
    