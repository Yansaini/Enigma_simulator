
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


#this funcion clean the text bfore encrypting it
def limpiar_texto(texto):
    texto = texto.upper() # convert everything in uppercase
    resultado = ""
    for ch in texto:
        if "A" <= ch <= "Z": #only keep letter from A to Z
            resultado += ch
    return resultado


#submenu functions of option 3.1
def ver_rotor():
    print("Que rotor quieres ver? (1, 2, 3)")
    rotor_num = input("> ")
    if rotor_num == "1":
        archivo = "rotor1.txt"
    elif rotor_num == "2":
        archivo = "rotor2.txt"
    elif rotor_num == "3":
        archivo = "rotor3.txt"
    else:
        print("Numero de rotor invalido")
        return
    #we load rotor infor the mapping and advamces
    mapeo, avance = leer_rueda(archivo)
    #rotor info
    print("\nRotor selleccionado: ", archivo)
    print("Mapeo: ", mapeo)
    print("Punto de avance: ", avance)
    print("")


#submenu of option 3
def editar_rotores():
    while True:
        print("--- EDITAR ROTORES ---\n---------------------")
        print("1. Ver rotor")
        print("2. Cambiar posicion inicial")
        print("3. Cambiar mapeo del rootor")
        print("4. Volver")
        #falta editar las funciones
        sub_opcion = input("> ")
        if sub_opcion == "1":
            ver_rotor()
        elif sub_opcion == "2":
            print("Función para cambiar posicion inicial")
        elif sub_opcion == "3":
            print("Función para cambiar mapeo del rotor")
        elif sub_opcion == "4":
            break
        else:
            print("Opcion inavalida, intentalo de nuevo")
       

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