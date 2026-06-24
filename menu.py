from validaciones import *
from funciones import *
import json

def menu ():
    datos = []
    menu = True
    while menu == True:
        print("""
    --------------- MENU ---------------
        
    1) Importar la lista de personajes
    2) Listar los personajes de alguna raza
    3) Modificar un personaje
    4) Eliminar un personaje
    5) Ordenar la lista
    6) Ver el personaje con mas tecnicas
    7) Ver el heroe con menor cantidad de transformaciones
    8) Guardar y salir
        
    ------------------------------------
    """)
        
        eleccion = pedir_int("Elija la opcion deseada: ")

        match validar_rango(eleccion, 1, 8):
            case 1:
                with open('dragon_ball.json', 'r', ) as archivo:
                    datos = json.load(archivo)
            case 2:
                if datos == []:
                    print("Ninguna lista de personajes fue cargada")
                else:
                    raza = input("Ingrese la raza por la que desea filtrar: ")
                    mostrar_json(filtrar_json(datos, "raza", raza))
            case 3:
                nombre = input("Ingrese el nombre del personaje a modificar: ")
                if type(validar_dato_json(datos, nombre)) == dict:
                    personaje = validar_dato_json(datos, nombre)
                    caracteristica = input("Ingrese la caracteristica a modificar: ").lower()
                    if type(validar_key_json(datos, caracteristica)) == dict:
                        nuevo_valor = input("Ingrese el nuevo valor: ")
                        if detectar_casteable(nuevo_valor) == True:
                            personaje[caracteristica] = int(nuevo_valor)
                        else:
                            personaje[caracteristica] = nuevo_valor
                    else:
                        print(f'la caracteristica "{caracteristica}" '
                              'no se encontró en el personaje "{nombre}"')
                else:
                    print(f'el personaje "{nombre}" no se encontró en la lista')

            case 4:
                nombre = input("Ingrese el nombre del personaje a eliminar: ")
                eliminar_json(datos, "nombre", nombre)
            case 5:
                copia_lista = copiar_json(datos)
                key = validar_str_lista(
                    input("Ingrese el dato por el que desea filtrar:"
                    " (nombre, raza o edad): "),
                    ["nombre", "edad", "raza"])
                mostrar_json(ordenar_json(copia_lista, key))
            case 6:
                ver_maximo(datos, "tecnicas")
            case 7:
                ver_minimo(datos, "transformaciones")
            case 8:
                with open("dragon_ball.json", "w") as archivo:
                    json.dump(datos, archivo, indent=4)
                print("Sesion finalizada")
                menu = False

menu()