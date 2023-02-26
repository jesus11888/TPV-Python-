import os #Importa una librería para ejecutar a los esclavos


op=1
while op != 4: 
    print('1.Registrar producto\n2.Visualizar producto\n3.Vender producto\n4.Salir')#Enseña las opciones de la TPV
    op = int(input('Ingresa una opción: '))
    
    if op == 1:
        os.system("python3 E1.py")
    elif op == 2:
        os.system("python3 E2.py")
    elif op == 3:
        os.system("python3 E3.py")
    elif op == 4:
        print('Salio...')
    else:
        print('Ingrese una opción valida')      
        