def mostrar_diccionario(diccionario: dict) -> str:
    mensaje = ""
    claves = list(diccionario.keys())
    
    for i in range(0, len(claves), 1):
        clave = claves[i]

        if type(diccionario[clave]) == dict:
            mensaje = mensaje + f"{clave.capitalize()}:\n{mostrar_diccionario(diccionario[clave])}\n"
        elif type(diccionario[clave]) == list:
            mensaje = mensaje + f"{clave.capitalize()}:\n{mostrar_lista(diccionario[clave])}\n"
        else:
            mensaje = mensaje + f"{clave.capitalize()}: {diccionario[clave]}\n"
            
    return mensaje


def mostrar_lista(lista: list) -> str:
    mensaje = ""
    
    for i in range(0, len(lista), 1):
        if type(lista[i]) == dict:
            mensaje = mensaje + f"{mostrar_diccionario(lista[i])}\n"
        elif type(lista[i]) == list:
            mensaje = mensaje + f"{mostrar_lista(lista[i])}\n"
        else:
            mensaje = mensaje + f"{lista[i]}\n"
            
    return mensaje


def mostrar_lista_dict(lista: list):
    mensaje = ""
    
    for i in range(0, len(lista), 1):
        mensaje = mensaje + mostrar_diccionario(lista[i])
        mensaje = mensaje + "-------------------\n"
        
    print(mensaje)

def filtrar_lista(lista:dict, key:str, valor:int|str):
    lista_nueva = []
    encontrado = False
    for item in lista:
        if item[key] == valor:
            lista_nueva.append(item)
            encontrado = True
    if encontrado == False:
        print("No se encontró el dato especificado")

    return lista_nueva

def eliminar_item(lista:list, key:str, valor:str):
    encontrado = False
    for item in lista:
        if item[key] == valor:
            encontrado = True
            print(f"{item[key].capitalize()} eliminado con exito. ")
            lista.remove(item)
            break
    if encontrado == False:
        print(f'No se encontró el dato "{valor}" en la lista')




def ver_maximo_lista(lista:list, key:str):
    valor_max = 0
    lista_maximos = []
    for item in lista:
        contador = 0
        for subitem in item[key]:
            contador += 1
        if contador > valor_max:
            lista_maximos = []
            valor_max = contador
            lista_maximos.append(item)
        elif contador == valor_max:
            lista_maximos.append(item)
    mostrar_lista_dict(lista_maximos)
    
def ver_minimo_lista(lista:list, key:str):
    valor_min = 0
    lista_minimos = []
    flag = True
    for item in lista:
        contador = 0
        for subitem in item[key]:
            contador += 1
        if flag == True:
            valor_min = contador
            lista_minimos.append(item)
            flag = False
        elif contador < valor_min:
            lista_minimos = []
            valor_min = contador
            lista_minimos.append(item)
        elif contador == valor_min:
            lista_minimos.append(item)
    mostrar_lista_dict(lista_minimos)

def ordenar_lista(lista, key):
    for i in range (len(lista)):
        for j in range (len(lista)-1):
            if lista[j][key] > lista[j+1][key]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista
