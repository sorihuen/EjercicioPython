from intermediate.databases.mysql_operations import execute_query

resultado = execute_query("SELECT * FROM Equipos")
for equipo in resultado:
    print(equipo)
