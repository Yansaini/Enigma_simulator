
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

def mover_rotores(posiciones_actuales, rotor):
    # Rotor1 (derecha) avanza 1 posicion
    posiciones_actuales[0] = (posiciones_actuales[0] + 1) % 26
    # Si punto_avance es Z, no mueve a los otros rotores
    if rotor[0][1] == "Z": 
        return posiciones_actuales
    # Si rotor1 llega a su punto de avance, se mueve rotor2
    if chr(posiciones_actuales[0] + 65) == rotor[0][1]:
        posiciones_actuales[1] = (posiciones_actuales[1] + 1) % 26
        # Si rotor2 llega a su punto de avance, se mueve rotor3
        if chr(posiciones_actuales[1] + 65) == rotor[1][1]:
            posiciones_actuales[2] = (posiciones_actuales[2] + 1) % 26
    return posiciones_actuales


#this funcion clean the text bfore encrypting it
def limpiar_texto(texto):
    texto = texto.upper() # convert everything in uppercase
    resultado = ""
    for ch in texto:
        if "A" <= ch <= "Z": #only keep letter from A to Z
            resultado += ch
    return resultado


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
            #anadir para cifrar
            mensaje = input("Escribe tu mensaje que quieres cifrar: ")
            mensaje = limpiar_texto(mensaje) #
            print("mensaje cifrado: ", mensaje)
            a = 1
        elif opcion == "2":
            #anadir para descifrar
            a=2
        elif opcion == "3":
            #anadir para editar rotores
            a=3
        elif opcion == "4": 
            print("Gracias por sus servicios.")
            break
        else:
            print("Opcion invalida, por favor, vuelva a introducir.")

main()