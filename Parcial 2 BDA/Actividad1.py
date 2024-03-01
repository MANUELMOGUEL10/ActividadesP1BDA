import mysql.connector
import json

# Conectar a la base de datos
conn = mysql.connector.connect(
    host="mysql-opset.alwaysdata.net",
    user="opset_us",
    password="Holamundo",
    database="opset_us"
)

# Variable de consulta a la base de datos
cursor = conn.cursor()

# Cargar datos desde el archivo JSON
with open('diccionario_maya.json','r',encoding='utf-8') as file:
  diccionario_data = json.load(file)

for palabra in diccionario_data:
  maya = palabra['Maya']
  espanol = palabra['Español']
  insert_query = "INSERT INTO diccionario_json (maya,espanol) VALUES(%s,%s)"
  cursor.execute(insert_query, (maya,espanol))

conn.commit()
cursor.close()
conn.close()
