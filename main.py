import connect as cnn

db_connection = cnn.DB()

while True:
    print("""
    1) Insertar
    2) Listar
    3) Actualizar
    4) Elimininar
    5) Buscar
    6) Salir
    """)

    try:
        opcion = int(input("Accion a realizar: \n"))
        if opcion = 1:
            pass
    except:
        print('Error')