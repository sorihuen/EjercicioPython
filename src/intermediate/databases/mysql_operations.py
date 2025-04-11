# src/database/mysql_operations.py

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "proyecto_db")
}


def create_connection():
    """Crea y devuelve una conexión a la base de datos."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("Conexión exitosa a la base de datos.")
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def execute_query(connection, query, params=None):
    """Ejecuta una consulta con una conexión ya abierta."""
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params if params else ())

        if query.strip().upper().startswith("CALL"):
            results = []
            result_set = cursor.fetchall()
            if result_set:
                results.extend(result_set)

            while cursor.nextset():
                more_results = cursor.fetchall()
                if more_results:
                    results.extend(more_results)

            return results
        else:
            return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        raise
    finally:
        cursor.close()


def call_procedure(connection, procedure_name, params=None):
    """Llama a un procedimiento almacenado usando una conexión existente."""
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.callproc(procedure_name, params or ())

        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())

        connection.commit()
        print(f"Procedimiento '{procedure_name}' ejecutado correctamente.")
        return results
    except Error as e:
        print(f"Error al llamar al procedimiento '{procedure_name}': {e}")
        return None
    finally:
        cursor.close()
