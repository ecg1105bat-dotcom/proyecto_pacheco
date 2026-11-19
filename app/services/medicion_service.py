#Capa de Servicio 
#En esta parte se debe conectar base de datos
#Por el momento es puro diseño :)

import mysql.connector
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "user": "erick2",
    "password": "123456",
    "database": "invernadero_pacheco"

}

def get_conexion():
    return mysql.connector.connect(**DB_CONFIG)

class MedicionService:
    @staticmethod
    def guardar_lectura(temperatura, humedad, ph):
        conn = get_conexion()
        cursor = conn.cursor()
        ahora = datetime.now()
        cursor.execute(

            "INSERT INTO lecturas (temperatura, humedad, ph, fecha, hora) VALUES (%s, %s, %s, %s, %s)",
            (temperatura, humedad, ph, ahora.date(), ahora.time())

        )
        conn.commit()
        cursor.close()
        conn.close()

        @staticmethod
        def obtener_ultima():
            conn = get_conexion()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM lecturas ORDER BY id DESC LIMIT 1")
            dato = cursor.fetchone()
            cursor.close()
            if not dato:
                return {"temperatura": 0, "humedad": 0, "ph": 0}
            return dato

        @staticmethod
        def obtener_historial():
            conn = get_conexion
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM lecturas ORDER BY id DESC")
            datos = cursor.fetchall()
            cursor.close()
            conn.close()
            return datos



"""
class MedicionService:
    @staticmethod
    def obtener_ultima():
        #TODO: conectar a base de datos
        return {"temperatura": 0, "humedad": 0, "ph": 0}

    @staticmethod
    def obtener_historial():
        #TODO: conectar a base de datos
        return[] 
 """      