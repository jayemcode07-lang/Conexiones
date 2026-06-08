from database import conectar

def main():
    conexiones = conectar()
    if conexiones:
        conexiones.close()
        print("Conexión Cerrada")

if __name__ == "__main__":
    main()
