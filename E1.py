import sqlite3
database = sqlite3.connect("MasterDB.db")#Conecta con la base de datos de productos 
print("Introduzca el código de barras")
codigo = input()
print("Introduzca el nombre")
nombre = input()
print("Introduzca el peso")
peso = input()
print("Introduzca el precio")
precio = input()
print("Introduzca las unidades")
uni = input()
register1 = (codigo,nombre,peso,precio,uni)
cursor = database.cursor()
cursor.execute("INSERT INTO Productos VALUES(?,?,?,?,?)", register1)#Introduce los datos en la base de datos
database.commit()#Guarda los cambios
database.close()#Cierra la conexión