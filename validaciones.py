def validar_rango(dato:int, minimo:int, maximo:int)->int:  
        validar = dato
        while validar < minimo or validar > maximo:
            validar = pedir_int(f"ERROR, ingrese un valor dentro del rango ({minimo} - {maximo}): ")
        return validar

def validar_minimo(dato:int, minimo:int)->int: 
        validar = dato
        while validar <= minimo:
            validar = pedir_int(f"ERROR, el valor ingresado no puede ser menor a {minimo}): ")
        return validar

def pedir_int(mensaje:str)->int:
    ingreso = input(mensaje)
    while detectar_casteable(ingreso) == False:
        ingreso = input("ERROR, ingrese una opcion valida: ")
    return int(ingreso)

def validar_str_lista(string:str, opciones_validas:list):
    valido = False
    valor = string
    while valido == False:
        for i in range(len(opciones_validas)):
            if valor == opciones_validas[i]:
                valido = True                
        if valido == False: 
            valor = input("ERROR, Ingrese una opcion valida: ")

    return valor

def validar_str_exacto(string:str, comparacion:str, mensaje:str)->str:
    valor = string
    while valor == comparacion:
        valor = input(mensaje)
    return valor
          

def detectar_casteable(string:str)->bool:
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]
    casteable = True

    if string == "":
        casteable = False
    else:        
        for i in range(len(string)):
            if string[i] in numeros:
                pass
            else:
                casteable = False
                break
           
    return casteable

def validar_dato_json(lista, dato):
    for item in lista:
        for subitem in item.values():
            if subitem == dato:
                return item

def validar_key_json(lista, dato):
    for item in lista:
        for subitem in item:
            if subitem == dato:
                return item
            
def validar_key_dict(diccionario, dato):
    for item in diccionario:
        if item == dato:
            return diccionario
