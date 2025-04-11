# 0 1 1 2 3 5 8 13 21 34 55 89, ...

def fibonacci_iterative(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    # Variables para almacenar los dos últimos números de Fibonacci
    previous, current = 1, 1
    
    # Calcular iterativamente hasta el n-ésimo número
    for _ in range(3, n + 1):
        next_value = previous + current
        previous = current
        current = next_value
    
    return current