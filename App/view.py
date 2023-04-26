"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
from DISClib.ADT import orderedmap as om

import matplotlib.pyplot as plt
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def filtrar_dic_con_por_llaves(dic, lista_de_columnas_aMostrar):
    dic_filt ={}
    for llave in lista_de_columnas_aMostrar:
        dic_filt[llave]=dic[llave]

    return dic_filt

def filtrar_lista_dics_por_columnas(lista_dics,lista_columnas):
    lista_filt = []
    
    tamanio_lista = len(lista_dics)
    i = 0
    
    while i<tamanio_lista:
        dic_filt_dado = filtrar_dic_con_por_llaves(lista_dics[i],lista_columnas)
        lista_filt.append(dic_filt_dado)
        i+=1
    return lista_filt

def new_controller():
    """
        Se crea una instancia del controlador
    """
    control =controller.new_controller()
    return control

    pass


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Reportar todos los accidentes dado un rango de fechas")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Reportar los 5 accidentes más recientes dada una gravedad y un rango de fechas")
    print("6- Ejecutar Requerimiento 5")
    print("7- Mostrar los N accidentes ocurridos dentro de una zona específica para un mes y un año")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")

def menu_nombre_archivo():
    print("Que porcentage de datos ")
    print("1-1%")
    print("2-5%")
    print("3-10%")
    print("4-20%")
    print("5-30%")
    print("6-50%")
    print("7-80%")
    print("8-100%")

def menu_archivo():
    menu_nombre_archivo()
    porcentaje = input('Seleccione una opción para continuar\n')
    try:
        if int(porcentaje) == 2:
            
            size ='datos_siniestralidad-5pct.csv'
            return size
        elif int(porcentaje) == 3:
            size = 'datos_siniestralidad-10pct.csv'
            return size
        elif int(porcentaje) == 4:
            size = 'datos_siniestralidad-20pct.csv'
            return size
        elif int(porcentaje) == 5:
            size = 'datos_siniestralidad-30pct.csv'
            return size
        elif int(porcentaje) == 6:
            size = 'datos_siniestralidad-50pct.csv'
            return size
        elif int(porcentaje) == 1:
            size = 'datos_siniestralidad-small.csv'
            return size
        elif int(porcentaje) == 7:
            size = 'datos_siniestralidad-80pct.csv'
            return size
        elif int(porcentaje) == 8:
            size = 'datos_siniestralidad-large.csv'
            return size
    except ValueError:
            print(" una opción válida.\n")
            traceback.print_exc()

def print_3_primeros_3últimos(control):

    array_gen = control['model']['siniestros']
    l = lt.size(array_gen)
    i=0
    lista_impr =[]
    lista_impr.append(lt.getElement(array_gen,1))
    lista_impr.append(lt.getElement(array_gen,2))
    lista_impr.append(lt.getElement(array_gen,3))
    lista_impr.append(lt.getElement(array_gen,l-2))
    lista_impr.append(lt.getElement(array_gen,l-1))
    lista_impr.append(lt.getElement(array_gen,l))
    
    lista_filt = filtrar_lista_dics_por_columnas(lista_impr,['CODIGO_ACCIDENTE','FECHA_HORA_ACC','LOCALIDAD','DIRECCION','GRAVEDAD','CLASE_ACC',
                                                             'LATITUD','LONGITUD'])
    tabulate_respuesta = tabulate(lista_filt, headers='keys', maxcolwidths =[10]*9, maxheadercolwidths=[10]*9)
    print('Los 3 primeros y 3 últimos siniestros cargados son: ')
    print(tabulate_respuesta)

def load_data(control,size):
    """
    Carga los datos
    """
    control =controller.load_data(control,size)
    return control
    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    fecha1 = (input("Por favor ingrese la fecha inicial en formato YY/MM/DD "))
    fecha2 = (input("Por favor ingrese la fecha final en formato YY/MM/DD "))
    respuesta =  controller.req_1(control,fecha1,fecha2)
    size = lt.size(respuesta[0])
    print( " There are " + str(size) + " between " + fecha1 + " and " + fecha2)
   
    heads = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION","GRAVEDAD","CLASE_ACC","LOCALIDAD", "FECHA_HORA_ACC","LATITUD","LONGITUD"]
    res = filtrar_lista_dics_por(respuesta[0],heads)
    print(tabulate(res, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    print("el tiempo " + str(respuesta[1]))

    


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    anio = (input("Por favor ingrese el año que desea estudiar: "))
    mes = (input("Por favor ingrese el mes que desea estudiar (en mayusculas): "))
    hora_i = (input("Por favor ingrese la hora inicial del rango, en formato HH:MM:SS : "))
    hora_f = (input("Por favor ingrese la hora final del rango en formato HH:MM:SS : "))
    respuesta = controller.req_2(control , anio , mes , hora_i , hora_f )
    size= lt.size(respuesta[0])
    print( "Hay " + str(size) + " accidentes para el año " + anio + " para el mes de " + mes + "en el intervalo de horas " + hora_i + " y " + hora_f)
    heads = ["CODIGO_ACCIDENTE", "FECHA_OCURRENCIA_ACC", "DIA_OCURRENCIA_ACC", "LOCALIDAD" , "DIRECCION" , "GRAVEDAD" , "CLASE_ACC" , "LATITUD" , "LONGITUD"]
    res = filtrar_lista_dics_por(respuesta[0] , heads)
    print(tabulate(res , headers= "keys" , tablefmt= "grid" , maxcolwidths= 15, maxheadercolwidths= 15 ))
    print (" el tiempo es " + str(respuesta[1]))
    

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    clase = (input("Por favor ingrese la clase de accidente que desea estudiar: "))
    calle = (input("Por favor ingrese la calle que desea estudiar(todo en mayusculas):  "))
    respuesta = controller.req_3(control , clase , calle)
    heads = ["CODIGO_ACC" , "FECHA_HORA_ACC" , "DIA_OCURRENCIA_ACC" , "LOCALIDAD" , "DIRECCION" , "GRAVEDAD" , "CLASE_ACC" , "LATITUD" , "LONGITUD"]
    res = filtrar_lista_dics_por(respuesta[0][0], heads)
    print("Hay " + str(respuesta[0][1]) + " accidedentes de la clase " + clase + " occuridos a lo largo de la vía " +  calle + " y  los tres mas recientes son: ")
    print(tabulate(res , headers="key" , tablefmt= "grid" , maxcolwidths=15, maxheadercolwidths=15))
    print("El tiempo es " + str(respuesta[1]))
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    fecha1 = (input("Porfavor ingrese la fecha inicial en formato YY/MM/DD "))
    fecha2 = (input("Porfavor ingrese la fecha final en formato YY/MM/DD "))
    gravedad = (input("Porfavor ingrese la gravedad en la que desea investigar "))
    respuesta = controller.req_4(control,fecha1,fecha2,gravedad)
    heads = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION","GRAVEDAD","CLASE_ACC","LOCALIDAD", "FECHA_HORA_ACC","LATITUD","LONGITUD"]
    res = filtrar_lista_dics_por(respuesta[0][0],heads)
    print("There are " + str(respuesta[0][1]) + " de gravedad " + gravedad + " between " + fecha1 + " and " + fecha2)
    print(tabulate(res, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    print("el tiempo " + str(respuesta[1]))



def print_req_5(control):

    anio =(input('Ingrese año: '))
    mes = (input ('Ingrese mes en formato númerico ej 03 para marzo'))
    localidad =(input('ingrese localidad en MAYUSCULAS SIN TILDES: '))

    respuesta = controller.req_5(control,anio,mes,localidad)

    #print(respuesta)
    lista_filt = filtrar_lista_dics_por_columnas(respuesta[0],["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION","GRAVEDAD","CLASE_ACC","LOCALIDAD", "FECHA_HORA_ACC","LATITUD","LONGITUD"])
    print(lista_filt)
    tabulate_respuesta = tabulate(lista_filt, headers='keys', maxcolwidths =[10]*9, maxheadercolwidths=[10]*9)
    print('Los 10 accidentes mas recientes para la fecha dada son: ')
    print(tabulate_respuesta)
    print(respuesta[1])

#
def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    anio = input("Ingrese el año en el que desea buscar la informacion ")
    mes = input("Ingrese el mes en el que desea buscar la informacion en formato de numero, ej:08 ")
    latitud = input("Ingrese la latitud en la que quiere buscar informacion cerca ")
    longitud = input("Ingrese la longitud  en la que quiere buscar informacion cerca ")
    radio = input("Ingrese el radio en el que desea buscar los accidentes en kilometros ")
    n_accidentes = input("Ingrese el numero de accidentes que desea investigar ")
    respuesta = controller.req_6(control, anio, mes, latitud, longitud,radio,n_accidentes)
    heads = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION","GRAVEDAD","CLASE_ACC","LOCALIDAD", "FECHA_HORA_ACC","LATITUD","LONGITUD"]
    res = filtrar_lista_dics_por(respuesta[0],heads)
    print("The " + n_accidentes + " closer to the point (" + latitud + "," + longitud + ") in a radio of " + radio + " km for the year " + anio + " in the month " + mes + "are")
    print(tabulate(res, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    print("el tiempo " + str(respuesta[1]))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    anio =input('Ingrese el año que desea estudiar: ')

    mes = input('Ingrese el mes que desea estudiar (en mayusculas): ')
    #req_72(control,anio,mes)
    # TODO: Manuel, llama aca la función que hagas qye liste los primeros y últimos accidentes por dia
    # TODO: Imprimir el resultado del requerimiento 7
    respuesta = controller.req_7(control , mes , anio)
    heads = ["CODIGO_ACCIDENTE" , "FECHA_HORA_ACC" , "DIA_OCURRENCIA_ACC" , "LOCALIDAD", "DIRECCION" , "GRAVEDAD" , "CLASE_ACC", "LATITUD" , "LONGITUD"]
    res = filtrar_lista_dics_por(respuesta[0] , heads)
    print("Accidentes más temprano y tardios para el mes de " + mes + " de " + anio)
    tamanio = len(res)
    i = 1
    while i <= tamanio:
        imprimir = lt.newList()
        dia = res[i]
        fecha_entera = dia["FECHA_HORA_ACC"]
        fecha = fecha_entera[0:9]
        dia_s = res[i]
        fecha_entera_s = dia["FECHA_HORA_ACC"]
        fecha_s = fecha_entera_s[0:9]
        lt.addLast(imprimir , dia)
        if fecha == fecha_s:
            lt.addLast(imprimir , dia_s)
            print("Accidentes del día " + fecha)
            print(tabulate(imprimir , headers= "keys", tablefmt= "grid" , maxcolwidths= 15, maxheadercolwidths= 15 ))
            i += 2
        else:
            print("Accidentes del día " + fecha)
            print(tabulate(imprimir , headers= "keys", tablefmt= "grid" , maxcolwidths= 15, maxheadercolwidths= 15 ))
            i += 1 
    print("el tiempo " + str(respuesta[1]))


def req_72(control,anio,mes):
    respuesta = controller.req7_2(control,anio,mes)
    respuesta_dic = respuesta[0]

    lista_x = list(respuesta_dic)

    i = 0

    while i<24:
        num = lista_x[i]
        lista_x[i]=str(num)
        i+=1
    ## crea lista y
    #print(type(lista_x[0]))
    lista_y =[]

    i = 0
    while i<24:
        lista_y.append(respuesta_dic[i])
        i+=1
    plt.bar(lista_x,lista_y)
    plt.title('Estadística de accidentes ocurridos en el mes dado por hora')
    plt.xlabel('Hora')
    plt.ylabel('Frecuencia')

    plt.show()
    print(respuesta[1])
def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def filtrar_lista_dics_por(lista_dics,lista_columnas):
    
    lista_filt = []

    tamanio_lista = lt.size(lista_dics)
    i = 1

    while i<=tamanio_lista:
        a = lt.getElement(lista_dics,i)
        dic_filt_dado = filtrar_dic_con_por_llaves(a,lista_columnas)
        lista_filt.append(dic_filt_dado)
        i+=1
    return lista_filt

def filtrar_dic_con_por_llaves(dic, lista_de_columnas_aMostrar):
    dic_filt ={}
    for llave in lista_de_columnas_aMostrar:
        dic_filt[llave]=dic[llave]

    return dic_filt

# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                size = menu_archivo()
                control = new_controller()
                data = load_data(control,size)
                #print(data[1])
                print_3_primeros_3últimos(control)
                #arbol = control['model']['dateIndex']
                #rango = om.values_array(arbol,202204*10**10,202205*10**10)
                #print(rango)
                #min = om.minKey(arbol)
                #print(min)
            elif int(inputs) == 2:

                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
