<<<<<<< Updated upstream
=======

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

>>>>>>> Stashed changes
#Menu principal :)

def main():
    while True:
        print("--- MAQUINA ENIGMA ---\n---------------------")
        print("1. Cifrar mensaje.")
        print("2. Descifrar mensaje.")
        print("3. Salir.")

        opcion = input("> ")
        if opcion == "1":
            #anadir para cifrar
            a = 1
        elif opcion == "2":
            #anadir para descifrar
            a=2
        elif opcion == "3": 
            print("Gracias por sus servicios.")
            break
        else:
            print("Opcion invalida, por favor, vuelva a introducir.")

main()