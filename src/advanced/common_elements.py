def find_common_elements(list1, list2):
    # Convertir las listas a conjuntos para operaciones más eficientes
    # Complejidad: O(n) para list1 y O(m) para list2, donde n y m son las longitudes de las listas
    set1 = set(list1)
    set2 = set(list2)

    # Encontrar la intersección de los conjuntos
    # Complejidad: O(min(n, m)) porque Python itera sobre el conjunto más pequeño y verifica la pertenencia en el conjunto más grande (operación O(1))
    common_elements = set1.intersection(set2)

    # Convertir el resultado de vuelta a una lista
    # Complejidad: O(k) donde k es el número de elementos comunes (k ≤ min(n, m))
    return list(common_elements)

# Complejidad total: O(n + m + min(n, m)) que se simplifica a O(n + m)
# Esta solución es mucho más eficiente que un enfoque de fuerza bruta con bucles anidados que tendría una complejidad de O(n*m)



def sort_people(people):
    # Utilizamos sorted() con una función lambda como clave
    # La lambda ordena primero por edad (índice 1) y luego por nombre (índice 0)
    # La función sorted tiene una complejidad de O(n log n)
    return sorted(people, key=lambda person: (person[1], person[0]))


class Stack:
    def __init__(self):
        # Inicializar la pila como una lista vacía
        self.items = []

    def push(self, item):
        # Agregar un elemento al final de la lista (top de la pila)
        self.items.append(item)

    def pop(self):
        # Quitar y devolver el último elemento si la pila no está vacía
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Opcional: lanzar excepción si prefieres

    def is_empty(self):
        # Verificar si la pila está vacía
        return len(self.items) == 0

    def peek(self):
        # Devolver el elemento en la cima sin quitarlo
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        # Devolver la cantidad de elementos en la pila
        return len(self.items)


class Node:
    def __init__(self, value):
        # Cada nodo tiene un valor y una referencia al siguiente nodo
        self.value = value
        self.next = None

def has_cycle(head):
    # Usamos dos punteros para detectar el ciclo
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # Avanza uno
        fast = fast.next.next     # Avanza dos

        if slow == fast:
            # Si se encuentran, hay un ciclo
            return True

    # Si llegamos al final sin que se encuentren, no hay ciclo
    return False



def find_sublist_with_target_sum(nums, target):
    # Inicializamos dos punteros para definir la ventana: inicio y fin
    start = 0
    current_sum = 0

    # Iteramos con el puntero 'end' por toda la lista
    for end in range(len(nums)):
        current_sum += nums[end]  # Agregamos el valor al total

        # Si la suma actual supera el objetivo, reducimos desde el inicio
        while current_sum > target and start <= end:
            current_sum -= nums[start]
            start += 1

        # Si encontramos una sublista con suma exacta al target
        if current_sum == target:
            return nums[start:end + 1]

    # Si no se encuentra ninguna sublista con suma igual al target
    return None
