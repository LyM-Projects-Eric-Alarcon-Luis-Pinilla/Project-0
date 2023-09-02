import regex as re 

filename = "Data/prueba.txt"
file = open(filename,"r",encoding="utf-8")
text = file.read()
raw_tokenizer = re.split("\s",text)

tokenizer = []
separadores = ["(",")","{","}"]

    
        
        
