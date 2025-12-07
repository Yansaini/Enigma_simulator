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