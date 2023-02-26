import sqlite3
database = sqlite3.connect("MasterDB.db")
cursor = database.cursor()

busqueda = input("Escribe tu búsqueda: ")
if not busqueda:
	print("Búsqueda inválida")
	exit()
 
sentencia = "SELECT * FROM Productos WHERE id LIKE ?;"
 
cursor.execute(sentencia, [ "%{}%".format(busqueda) ])
	
Productos = cursor.fetchall()
print("+{:-<20}+{:-<50}+{:-<10}+{:-<10}+{:-<20}+".format("", "", "", "", ""))
print("|{:^20}|{:^50}|{:^10}|{:^10}|{:^20}|".format("Codigo de barras", "Nombre", "Peso", "Precio", "Unidades"))
print("+{:-<20}+{:-<50}+{:-<10}+{:-<10}+{:-<20}+".format("", "", "", "", ""))
 
 
for id, Nombre, Peso, Precio, Unidades in Productos:
	print("|{:^20}|{:^50}|{:^10}|{:^10}|{:^20}|".format(id, Nombre, Peso, Precio, Unidades))
	
 
print("+{:-<20}+{:-<50}+{:-<10}+{:-<10}+{:-<20}+".format("", "", "", "", ""))