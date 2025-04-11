# Prueba Técnica - Python + MySQL

Este proyecto es una abarca tres niveles de ejercicios: **básico**, **intermedio** y **avanzado**, utilizando Python y MySQL. También se integró automatización con N8N y uso de variables de entorno para un entorno más seguro.

---

## 📁 Estructura del Proyecto

```
src/
│
├── basic/             # Ejercicios de nivel básico
│   ├── lists.py       # Manipulación de listas
│   ├── chains.py      # Manejo de cadenas
│   └── recursion.py   # Recursividad (Fibonacci)
│
├── intermediate/      # Automatización e integración con MySQL y N8N
│   └── ...
│
├── advanced/          # Ejercicios de algoritmos y estructuras de datos
│   └── common_elements.py
│
main.py                # Script principal para ejecutar los ejercicios
queries.sql            # Sentencias y procedimientos para MySQL
```

---

## 🧠 Ejercicios

### 🟢 Básico

1. **Manipulación de Listas**  
   Elimina duplicados y ordena una lista de enteros.

2. **Manejo de Cadenas**  
   Cuenta la frecuencia de cada palabra en una cadena.

3. **Recursividad**  
   Calcula el n-ésimo número de la sucesión de Fibonacci usando recursión.

---

### 🟡 Intermedio

- **N8N:**  
  Al recibir un correo, extrae un nombre de canal de YouTube, busca el canal, obtiene suscriptores y número de videos, y responde con esa información al remitente del correo.

- **MySQL:**  
  Diseño de base de datos con tablas `Equipos`, `Jugadores`, `Partidos`. Se realizaron consultas como:
  
  - Top 2 equipos con más goles como local (fundados antes del 2000)
  - Partidos con más goles
  - Equipos ganadores como local  
  Además, se implementaron **procedimientos almacenados** para registrar resultados, transferencias de jugadores, y más.

---

### 🔴 Avanzado

Se desarrollaron ejercicios avanzados enfocados en estructuras de datos y algoritmos:

- Encontrar elementos comunes entre listas
- Ordenar personas por edad y nombre
- Implementación de una pila LIFO
- Detección de ciclos en listas enlazadas
- Sublistas cuya suma sea igual a un número objetivo

---

## 🧪 Cómo ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-repo.git
   cd tu-repo
   ```

2. Crea tu entorno virtual e instálalo:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configura tus variables en un archivo `.env` (ver `.env.example` para guía).

4. Ejecuta el script principal:
   ```bash
   python main.py
   ```

---

## 🔐 Archivo `.env.example`

```env
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
YOUTUBE_API_KEY=your_youtube_api_key

IMAP_SERVER=imap.gmail.com
SMTP_SERVER=smtp.gmail.com

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_db_password
DB_NAME=proyecto_db
```



---

## 👨‍💻 Autor

Desarrollado por [Tu Nombre] para prueba técnica de Python, 2025.

