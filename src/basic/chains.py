import re

def count_words(text):
    # Convertimos el texto a minúsculas para hacer el conteo insensible a mayúsculas/minúsculas
    text = text.lower()
    
    # Usamos una expresión regular para extraer solo las palabras (eliminando signos de puntuación)
    words = re.findall(r'\b\w+\b', text)
    
    # Creamos un diccionario para contar las ocurrencias de cada palabra
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    
    return count

# Tambien se puede ajustar el codigo usando directamente la clase Counter del módulo collections
