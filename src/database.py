import psycopg2
from config import*

def conectar():
    try:
        conexiones = psycopg2.connect(
            host=DB_HOST, 
            database=DB_NAME, 
            user=DB_USER, 
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Conexion exitosa")
        return conexiones
    except Exception as e:
        print(f'Error al conectar: {e}')
        return None
    
