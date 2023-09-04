import controller 

print("=================================================")
print("Welcome, remember that before running the code ")
print("you should place the txt file you want to verify in the 'Data' folder of this proyect \n \n")
print("=================================================")
filename = input("What is the name of the file you want to verify? \n================================================= \n")
try:
   data = controller.load_data(filename)
   print("File loaded properly")
   print("Verifying the code........ \n\n")
   verifier = controller.verify(data)
   print(f"The code has correct syntax? \n {verifier}")
   print(verifier)
   print("Thanks for using the program")
    
except:
   print("Exploto :p")
    





