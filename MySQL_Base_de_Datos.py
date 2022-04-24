from asyncio.windows_events import NULL
from locale import locale_encoding_alias
import mysql.connector


conexion1 = mysql.connector.connect(
    user='user',
    password='password',
    host='localhost',
    database='mysqldatabase',
    auth_plugin='mysql_native_password'
    )

cursor1 = conexion1.cursor()

#cursor1.execute("orden")  Ejecuta la orden como si fuera un SQL Script

def showInformation(information):
    cursor1.execute(f"show {information}")
    for elem in cursor1:
        print(f"{elem[0]}")

def insertaRow(tabla, columnas, valores):
    sql=f"insert into {tabla} ({columnas}) values ({valores})"
    cursor1.execute(sql)
    conexion1.commit()

def showRows(tabla, columnas):
    cursor1.execute(f"select {columnas} from {tabla}")
    for fila in cursor1:
        print(fila)

def modifyRow(tabla, columnaActualizar, condicion):
    cursor1.execute(f"update {tabla} set {columnaActualizar} where {condicion}")
    conexion1.commit()

def deleteRow(tabla, condicion):
    cursor1.execute(f"delete from {tabla} where {condicion}")
    conexion1.commit()


# #Muestra las bases de datos existente
# showInformation("databases")

# #Muestra las tablas existente en (todas?) las bases de datos
# showInformation("tables")

# #Inserta una linea en una tabla
# nombreTabla = 'Pruebas'
# nombreTodasColumnas = 'Nombre, Apellido, Email, Telefono'
# JuanraDatos = '"Juanra", "Sesma", "juanra@sesma.com", 12345"' 
# RaulDatos = '"Raul", "Correro", "raul@correro.com", 54321'
# GonzaloDatos = '"Gonzalo","Estrada", "gonzalo@estrada.com", NULL'
# insertaRow(nombreTabla, nombreTodasColumnas , JuanraDatos)
# insertaRow(nombreTabla, nombreTodasColumnas , RaulDatos)
# insertaRow(nombreTabla, nombreTodasColumnas , GonzaloDatos)

# #Trae todas las rows de una tabla
# showRows(nombreTabla, nombreTodasColumnas)

# #Modifica una row de una tabla
# condicionModify = 'Nombre="Raul"'
# updatedColumn = 'Apellido="Correro 2"'
# modifyRow(nombreTabla, updatedColumn, condicionModify)

# #region Elimina una row de una tabla
# condicionDelete = 'Nombre="Juanra"'
# deleteRow(nombreTabla, condicionDelete)



conexion1.close() 