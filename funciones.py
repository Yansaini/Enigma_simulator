def leer_rueda(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as f:
            lineas = f.readlines()
        conexiones = lineas[0].strip().upper() 
        punto_avance = "Z"  
        if len(lineas) > 1:
            punto_avance = lineas[1].strip().upper()
        return conexiones, punto_avance
    except FileNotFoundError:
        print(f"Error: Archivo {nombre_archivo} no encontrado")
        # Mapeo
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Z"