import pandas as pd

archivo=input("Ingrese nombre archivo .xlsx a convertir: ")

evaluar= archivo.endswith(".xlsx")

if evaluar == True:
    print("El archivo es .xlsx")
    read_file = pd.read_excel(archivo) # lee el archivo excel
    read_file.to_csv(archivo,  
                  index = None, 
                  header=True) 
    
    df = pd.DataFrame(pd.read_csv(archivo)) 
  
    df
else:
    print("El archivo no es .xlsx")

     
