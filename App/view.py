import controller 

print("Bienvenido, recuerde que antes de empezar con las pruebas ")
print("debe colocar el archivo txt que desea verificar en la carpeta 'Data' de este proyecto \n")
filename = input("Cúal es el nombre del archivo que desea verificar: \n")
try:
    data = controller.load_data(filename)
    print("Verifying the code........")
    verifier = controller.verify(data)
    print(verifier)
    print("Thanks for using the program")
    
except:
    print("Could not read the file properly")
    





