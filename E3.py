import sqlite3

conexion = sqlite3.connect('MasterDB.db')

cursor = conexion.cursor()

# Obtener el ID del registro a modificar desde la entrada del usuario
registro_id = input("Introduce el código de barras del producto vendido: ")

# Obtener el nuevo valor para el campo del registro
uni = input("Introduce la cantidad de unidades en stock: ")

# Modificar el campo del registro en la base de datos
sql = "UPDATE Productos SET Unidades=? WHERE id=?"
valores = (uni, registro_id)
cursor.execute(sql, valores)

# Guardar los cambios
conexion.commit()

# Cerrar la conexión a la base de datos
conexion.close()

