from database import conectar
from DB_info import ver_tabla_estudiantes

def main():
    conexion = conectar()

    if conexion:
        print("Conexión exitosa")
        conexion.close()

    ver_tabla_estudiantes()

if __name__ == "__main__":
    main()