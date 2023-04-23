"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from datetime import datetime
import math 
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {"siniestros": None,
                "dateIndex": None,
                }

    data_structs["siniestros"] = lt.newList("ARRAY_LIST")
    data_structs["dateIndex"] = om.newMap(omaptype="RBT",
                                      comparefunction=compareDates)

    return data_structs



# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["siniestros"], data)
    updateDateIndex(data_structs["dateIndex"], data)

    return data_structs


# Funciones para creacion de datos

def new_data(formulario,cod_acc, fecha, hora,anio,mes,dia, direccion, gravedad, clase_acc, localidad,municipio,fecha_hora,latitud,longitud):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {}
    data['CODIGO_ACCIDENTE']=cod_acc
    data['FECHA_HORA_ACC']= fecha_hora
    data['LOCALIDAD']= localidad
    data['DIRECCION']= direccion
    data['GRAVEDAD']= gravedad
    data['CLASE_ACC']= clase_acc
    data['LATITUD']=latitud
    data['LONGITUD']=longitud

    return data


def updateDateIndex(map, siniestro):
    """
    Se toma la fecha del siniestro y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de siniestros.
   
    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea.
    """
    occurreddate = siniestro["FECHA_HORA_ACC"]
    #date_arbol = datetime.strptime(occurreddate, "%Y/%m/%d %H:%M+%S")
    date_arbol = occurreddate.replace('/','').replace(':','').replace(' ','').replace('+','')
    entry = om.get(map, date_arbol)
    if entry is None:
        datentry = newDataEntry(siniestro)
        om.put(map, date_arbol, datentry)
    else:
        datentry = me.getValue(entry)

    ###añade el elemento al nodo
    addDateIndex(datentry, siniestro)
    return map

def addDateIndex(datentry, siniestro):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry["lista_accidentes"]
    lt.addLast(lst, siniestro)

    return datentry
def newDataEntry(siniestro):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {"fecha": None, "lista_accidentes": None}
    entry['fecha'] = siniestro['FECHA_HORA_ACC']

    entry["lista_accidentes"] = lt.newList("SINGLE_LINKED", compareDates)

    return entry
# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass

def fecha_hora_inicial(fecha):
    valor_fecha = fecha.replace('/','').replace(':','').replace(' ','').replace('+','')
    "vuelve la fecha a la manera que se organizo el dic"
    size = len(valor_fecha)
    "el tamañio de ese string "
    ideal_size = 16
    "los que debe tener por si no se le agrega la hora o algo asi"
    ceros = ideal_size -size
    "cuando faltan para estar completos"
    respuesta = valor_fecha + "0"*ceros 
    "sumarle los ceros necesarios al valor "
    return respuesta

def fecha_hora_final(fecha):
    valor_fecha = fecha.replace('/','').replace(':','').replace(' ','').replace('+','')
    "vuelve la fecha a la manera que se organizo el dic"
    size = len(valor_fecha)
    "el tamañio de ese string "
    ideal_size = 12
    "los que debe tener por si no se le agrega la hora o algo asi"
    ceros = ideal_size -size
    "cuando faltan para estar completos"
    respuesta = valor_fecha + "2359"+ "0"*ceros 
    "sumarle los ceros necesarios al valor "
    return respuesta

def devolver_value(mapa, key):
    llave_valor = mp.get(mapa, key)
    valor = me.getValue(llave_valor)
    return valor 
def organizar_rango_fechas_mas_reciente(data_structs,fecha1, fecha2):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    
    valor_fecha1 = fecha_hora_inicial(fecha1)
    
    valor_fecha2 = fecha_hora_final(fecha2)
    "se convierte la fecha dada a tipo de llave"

    llaves = om.values(data_structs["model"]["dateIndex"],valor_fecha1, valor_fecha2)
    "se sacan los que esten en el rango dado"
    respuesta = lt.newList()
    tamanio = lt.size(llaves)
    i =1
    while i <= tamanio:
        pos = lt.getElement(llaves,i)
        "se saca el valor acorde en la lista"
        dato = pos["lista_accidentes"]
        "se deja solo la lista de accidentes "

        valor = lt.getElement(dato,1)
        "solo tendra un dato "
        lt.addFirst(respuesta,valor)
        i+=1

    return respuesta
def req1(data_structs,fecha1, fecha2):
    respuesta = organizar_rango_fechas_mas_reciente(data_structs,fecha1, fecha2)
    return respuesta

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs,fecha1,fecha2,gravedad):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    lista_fechas = organizar_rango_fechas_mas_reciente(data_structs,fecha1,fecha2)
    tamanio = lt.size(lista_fechas)
    i = 1
    respuesta = lt.newList("ARRAY_LIST")
    while i<= tamanio:
        "verificar si la gravedad que esta es la que quiero, si es asi la agrego a una lista "
        especifico = lt.getElement(lista_fechas,i)
        if especifico["GRAVEDAD"] == gravedad:
            lt.addLast(respuesta,especifico)
        i+=1

    size = lt.size(respuesta)
    "tamanio de cuantos cumplen los requisitos para imprimir"
    final = lt.newList("ARRAY_LIST")
    a=1
    if size >=5:
        "solo para imprimir los 5 "
        while a <= 5:
            valor = lt.getElement(respuesta,a)
            lt.addLast(final,valor)
            a+=1
        return final,size
    else:
        return respuesta, size
    
    




def req_5(data_structs,anio,mes,localidad):
    """
    Función que soluciona el requerimiento 5
    """
    arbol_fechas = data_structs['dateIndex']

    lim_inf = int(anio+mes)*10**10
    lim_sup = (int(anio+mes)+1)*10**10
    
    lista_10 = []
    ##rango en single_linked
    rango_siniestros = om.values_array(arbol_fechas,lim_inf,lim_sup)



    
    ###iterar rango hasta obtener los 10 más recientes de la localidad

    len_rango = lt.size(rango_siniestros)
    i=0
    
    while i<=len_rango:
            
            len_10 =len(lista_10)

            if len_10 ==10:
                break
            lista_nodo = lt.getElement(rango_siniestros,len_rango-i)['lista_accidentes']
            len_lista_nodo = lt.size(lista_nodo)
            j=1

            while j<=len_lista_nodo:
                accidente = lt.getElement(lista_nodo,j)

                if accidente['LOCALIDAD']==localidad:
                    lista_10.append(accidente)

                len_10 = len(lista_10)
                
                if len_10==10:
                    break

                j+=1

            i+=1

    

  
    return lista_10
  
  
  
    pass



def funcion_distancias_lat_long(latitud1,longitud1,latitud2,longitud2):
    r = 6371
    c = math.pi/180
    d =r*2*math.asin(math.sqrt(math.sin(c*(latitud1-latitud2)/2)**2 + math.cos(c*latitud1) * math.cos(c*latitud2)*math.sin(c*(longitud1-longitud2)/2)**2))

    return d

def req_6(data_structs,anio,mes,latitud,longitud,radio,n_actividades):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    codificacion = anio + mes + "0"*10
    if mes == "12":
        anio = int(anio) + 1
        mes = int(mes) - 11
        codificacion_siguiente_mes = str(anio) +"0" + str(mes) + "0"*10
        "calculo el siguiente mes dependiendo si es diciembre "
    
    else:
        mes = int(mes) + 1
        codificacion_siguiente_mes = str(anio) + "0" + str(mes) + "0"*10
        "el valor que se le dara al mes indicado "

    lista_intervalo_valores = om.values(data_structs["model"]["dateIndex"],codificacion,codificacion_siguiente_mes)
    "lista del intervalo "

    tamanio = lt.size(lista_intervalo_valores)
    i = 1
    heap = mpq.newMinPQ(cmpfunction=compareradio)
    mapa = mp.newMap()
    "no se que colocar para el heap "
    while i <=tamanio:
        exacto = lt.getElement(lista_intervalo_valores,i)
        pos = lt.getElement(exacto["lista_accidentes"],1)
        distancia = funcion_distancias_lat_long(float(latitud), float(longitud), float(pos["LATITUD"]), float(pos["LONGITUD"]))
        "se saca la distancia en la que esta "
        if distancia <= int(radio):
            mpq.insert(heap,distancia)
            mp.put(mapa,distancia,pos)
            "si es verdad se agrega a un heap "
            "Mapa con llave la distancia y respuesta lo que quiero dar "
        i+=1

    

    respuesta = lt.newList("ARRAY_LIST")
    a = 1
    while a <= int(n_actividades):
        "voy agregando poco a poco a una nueva lista para que al final solo muestre las que deseo "
        min = mpq.min(heap)
        dic = devolver_value(mapa,min)
        lt.addLast(respuesta,dic)
        
        mpq.delMin(heap)
        a +=1 
    
    return respuesta 





#### Funciones req 7


#Crea diccionario con llave hora y valor numero de accidentes
def data_frame_accidentes_por_hora(data_structs,anio,mes):

    arbol_fechas = data_structs['dateIndex']

    lim_inf = int(anio+mes)*10**10
    lim_sup = (int(anio+mes)+1)*10**10
    

    ##rango en single_linked
    rango_siniestros = om.values_array(arbol_fechas,lim_inf,lim_sup)

    #print(rango_siniestros)
    #crear dic
    dic_horas={}

    i =0
    while i<24:
        dic_horas[i]=0
        i+=1
    rango_siniestros_iterable = lt.iterator(rango_siniestros)
    for entry in rango_siniestros_iterable:
        lista_accidentes = entry['lista_accidentes']

        lista_acc_iterable = lt.iterator(lista_accidentes)

        for accidente in lista_acc_iterable:
            #print(accidente)
            hora_acc = int(accidente['HORA_OCURRENCIA_ACC'].split(':')[0])
            #print(hora_acc)

            dic_horas[hora_acc]+=1
    
    return dic_horas


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass


def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (int(date1) == int(date2)):
        return 0
    elif (int(date1) > int(date2)):
        return 1
    else:
        return -1
    
def compareradio(radio1, radio2):
    """
    Compara dos fechas
    """
    
    if (int(radio1) > int(radio2)):
        return True
    else:
        return False
