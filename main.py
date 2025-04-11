from src.basic.lists import remove_duplicates_and_sort
from src.basic.chains import count_words
from src.basic.recursion import fibonacci_iterative
from src.intermediate.email_youtube import main_flow
from src.intermediate.databases.mysql_operations import execute_query, create_connection,call_procedure
from src.advanced.common_elements import( 
    find_common_elements, 
    sort_people, 
    Stack, 
    Node, 
    has_cycle, 
    find_sublist_with_target_sum)
from src.intermediate.databases.query import (
    get_top_local_goal_teams,
    get_matches_with_most_goals,
    get_teams_with_home_wins,
    get_player_current_team
)

print("\n########## EJERCICIO 1: MANIPULACIÓN DE LISTAS ##########")

input_list = [8, 2, 7, 2, 4, 10, 5, 8, 7, 3]
result = remove_duplicates_and_sort(input_list)

print("Entrada:", input_list)
print("Resultado:", result)

print("\n##########################################################\n")

text = "Hola mundo, hola Python. Hola a todos."
result = count_words(text)

print("########## EJERCICIO 2: MANEJO DE CADENAS ##########")
print("Entrada:", text)
print("Resultado:", result)


print("\n########## EJERCICIO 3: RECURSIÓN ##########")
n = 6
result = fibonacci_iterative(n)
print(f"El {n}-ésimo número de Fibonacci es:", result)

print("\n########## EJERCICIO 4: EMAIL-YOUTUBE ##########")
print("Starting advanced flow (email + YouTube)...")
main_flow()


print("\n##########  EJERCICIO 5: BASE DE DATOS: MYSQL ##########")

# Crear una única conexión a la base de datos MySQL
connection = create_connection()
if not connection:
    exit()  # Termina si la conexión falla

try:
    # 1.Consulta: Equipos con más goles locales fundados antes del año 2000
    print("Consulta 1 - Equipos con más goles locales fundados antes del 2000:")
    result_1 = execute_query(connection, get_top_local_goal_teams())
    for row in result_1:
        print(row)

    # 2. Consulta: Partidos con más goles
    print("Consulta 2 - Partidos con más goles (mostrar nombres de equipos):")
    result_2 = execute_query(connection, get_matches_with_most_goals())
    for row in result_2:
        print(row)

    # 3. Consulta: Equipos que han ganado partidos como locales
    print("Consulta 3 - Equipos que han ganado siendo locales:")
    result_3 = execute_query(connection, get_teams_with_home_wins())
    for row in result_3:
        print(row)

    print("\n########## PROCEDIMIENTOS ##########")

    # 4.Procedimiento: Registrar un resultado de partido
    print("Procedimiento 2 - RegistrarResultado:")
    # Parametros: id_local=1, id_visitante=2, goles_local=3, goles_visitante=1, fecha='2023-10-10'
    call_procedure(connection, "RegistrarResultado",[2, 3, 2, 2, '2024-03-15'])

    print("Resultado registrado.")

    # 5. Procedimiento: Transferir jugador a otro equipo
    print("Procedimiento 3 - TransferirJugador:")

    # Consulta para mostrar el equipo anterior del jugador
    print("Verificación - Equipo ANTERIOR del jugador:")
    equipo_anterior_result = execute_query(connection, get_player_current_team(1), [1])
    for row in equipo_anterior_result:
        print(row)

    equipo_anterior = equipo_anterior_result[0]["equipo_actual"] if equipo_anterior_result else None
    equipo_anterior_id = equipo_anterior_result[0]["id_equipo"] if equipo_anterior_result else None

    # Buscar un equipo diferente al actual para la transferencia
    query_otro_equipo = """
    SELECT id_equipo FROM Equipos WHERE id_equipo != %s LIMIT 1
    """
    otro_equipo_result = execute_query(connection, query_otro_equipo, [equipo_anterior_id])
    otro_equipo_id = otro_equipo_result[0]["id_equipo"] if otro_equipo_result else 3  # Usar ID 3 como fallback

    # Transferencia del jugador a un equipo diferente
    call_procedure(connection, "TransferirJugador", [1, otro_equipo_id])
    print(f"Transferencia realizada al equipo con ID {otro_equipo_id}.")

    # Verificar si el jugador realmente cambió de equipo
    print("Verificación - Equipo NUEVO del jugador:")
    equipo_nuevo_result = execute_query(connection, get_player_current_team(1), [1])
    for row in equipo_nuevo_result:
        print(row)

    # 6.Procedimiento: Buscar jugadores por posición (ej. "Delantero")
    print("Procedimiento 1 - BuscarJugadoresPorPosicion (Delantero):")
    result_4 = call_procedure(connection, "BuscarJugadoresPorPosicion", ["Delantero"])
    for row in result_4:
        print(row)

finally:
    connection.close()
    print("Conexión cerrada.")


print("\n##########  EJERCICIO 1: AVANZADO ##########")
print("\n LISTAS")

# Datos 
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

# Llamada a la función
resultado = find_common_elements(lista1, lista2)
print("Elementos comunes:", resultado)


print("\n########## EJERCICIO 2: ORDENAR PERSONAS ##########")

people = [("Zoe", 22), ("Anna", 28), ("Liam", 22), ("Mark", 35), ("Eve", 28)]
sorted_people = sort_people(people)

print("Sorted people:", sorted_people)


print("\n########## Ejercico 3: IMPLEMENTACION DE UNA PILA ##########")

stack = Stack()

print("Is empty?", stack.is_empty())  # True

# Apilar elementos
stack.push("first")
stack.push("second")
stack.push("third")

print("Top of stack:", stack.peek())  # third
print("Size:", stack.size())  # 3

# Desapilar elementos
print("Pop:", stack.pop())  # third
print("Pop:", stack.pop())  # second

print("Is empty?", stack.is_empty())  # False

# Último pop
print("Pop:", stack.pop())  # first
print("Is empty?", stack.is_empty())  # True


print("\n##########  EJERCICIO 4: AVANZADO - DETECCIÓN DE CICLOS ##########")

# Crear nodos
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

# Conectar nodos sin ciclo
a.next = b
b.next = c
c.next = d

print("¿Tiene ciclo?:", has_cycle(a))  # False

# Crear un ciclo: D -> B
d.next = b

print("¿Tiene ciclo?:", has_cycle(a))  # True


print("\n##########  EJERCICIO 5: SUBLISTA CON SUMA OBJETIVO ##########")

nums = [4, 2, 7, 1, 9, 3]
target = 10

#nums = [1, 2, 3, 4, 5]
#target = 50  # No hay ninguna combinación consecutiva en [1, 2, 3, 4, 5] que sume 50  es NONE


result = find_sublist_with_target_sum(nums, target)
print("Resultado:", result)  