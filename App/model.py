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


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


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


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


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
