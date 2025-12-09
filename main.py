
def leer_rueda(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as f:
            lineas = f.readlines()
        conexiones = lineas[0].strip().upper() # Como cambia cada letra
        punto_avance = "Z"   # Valor por defecto
        if len(lineas) > 1:
            punto_avance = lineas[1].strip().upper()
        return conexiones, punto_avance
    except FileNotFoundError:
        print(f"Error: Archivo {nombre_archivo} no encontrado")
        # Si no hay archivo, cada letra se transforma en ella misma (mapeo)
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Z"


def cifrar_letra(letra, mapeo, posicion):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #1. Mirar que numero es la letra (A=0, B=1, etc)
    indice = (abecedario.index(letra) + posicion) % 26
    #2. Cifrar usando el mapeo de la rueda
    letra_cifrada = mapeo[indice]
    #3. Convertir de vuelta a posicion normal
    indice_salida = (abecedario.index(letra_cifrada) - posicion) % 26
    return abecedario[indice_salida]

<<<<<<< HEAD
<<<<<<< HEAD
=======
def descifrar_letra(letra, mapeo, posicion):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indice = (abecedario.index(letra) + posicion) % 26
    # Esto hace el mapeo inverso (es decir, si A->E, entonces E->A)
    inverso = [""] * 26
    for i in range(26):
        inverso[abecedario.index(mapeo[i])] = abecedario[i]
    mapeo_inverso = "".join(inverso)  # Para convertir la lista a string
    letra_cifrada = mapeo_inverso[indice]
    indice_salida = (abecedario.index(letra_cifrada) - posicion) % 26
    return abecedario[indice_salida]

#Menu principal :)

def main():
    while True:
        print("--- MAQUINA ENIGMA ---\n---------------------")
        print("1. Cifrar mensaje.")
        print("2. Descifrar mensaje.")
        print("3. Editar rotores")
        print("4. Salir.")

        opcion = input("> ")
        if opcion == "1":
<<<<<<< HEAD
            # para cifrar
            mensaje = input("Escribe tu mensaje que quieres cifrar: ")
            mensaje = limpiar_texto(mensaje) #
            print("Mensaje Limpio: ", mensaje)
            # rotor posicions
            pos1 = 0
            pos2 = 0
            pos3 =0
            print("Posiciones inicuales:", pos1,pos2,pos3)

            rotor1_mapeo, rotor1_avance = leer_rueda("rotor1.txt")
            rotor2_mapeo, rotor2_avance = leer_rueda("rotor2.txt")
            rotor3_mapeo, rotor3_avance = leer_rueda("rotor3.txt")

            resultado = ""

            for letra in mensaje:
                resultado += letra 

            print("Mensaje cifrado: ",resultado)
            
=======
            #anadir para cifrar
            mensaje = input("Escribe tu mensaje que quieres cifrar: ")
            mensaje = limpiar_texto(mensaje) #
            print("Mensaje Limpio: ", mensaje)
            a = 1
        elif opcion == "2":
            #anadir para descifrar
            a=2
        elif opcion == "3":
            #anadir para editar rotores
            editar_rotores()
            a=3
        elif opcion == "4":
            print("Gracias por sus servicios.")
            break
        else:
            print("Opcion invalida, por favor, vuelva a introducir.")

main()