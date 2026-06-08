from database import conectar

def ver_tabla_estudiantes():
    conexion = conectar()
    cursor = conexion.cursor()

    # Mostrar columnas
    cursor.execute("""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = 'estudiantes'
        ORDER BY ordinal_position
    """)

    print("\n=== CAMPOS DE LA TABLA ESTUDIANTES ===")
    columnas = cursor.fetchall()

    for nombre, tipo in columnas:
        print(f"{nombre} -> {tipo}")

    # Mostrar registros
    cursor.execute("SELECT * FROM estudiantes")

    registros = cursor.fetchall()

    print("\n=== REGISTROS ===")

    if registros:
        for fila in registros:
            print(fila)
    else:
        print("La tabla no tiene registros.")

    cursor.close()
    conexion.close()

