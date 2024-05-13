"Autores: Axel Castañeda Sánchez 010145666
"         Diego Sánchez Mendoza 340401995
"Descripción: El programa despliega un menu de opciónes y
"en base a realiza los comandos pertinentes.
import os
import subprocess

def ejecuta_comando(comando):
    subprocess.run(comando, shell=True)

def menu():
    print("1. Muestre los contenidos del directorio actual")
    print("2. Crea un archivo locura.py con gedit")
    print("3. Muestra los contenidos del archivo menu.py'")
    print("4. Muestra las primera lineas del archivo menu.py'")
    print("5. Cambia el permiso a menu.py")
    print("6  Encuentra menu.py")
    print("7. Muestra el directorio actual ")
    print("8. Salir ")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            ejecuta_comando("ls")
        elif opcion == '2':
            ejecuta_comando("gedit locura.py")   
        elif opcion == '3':
            ejecuta_comando("cat menu.py")
        elif opcion == '4':
            ejecuta_comando("head menu.py")
        elif opcion == '5':
            ejecuta_comando("chmod 777 menu.py")
        elif opcion == '6':
            ejecuta_comando ("find menu.py")
        elif opcion =='7':
            ejecuta_comando("pwd")
        elif opcion == '8':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida. ")

if __name__ == "__main__":
    main()
