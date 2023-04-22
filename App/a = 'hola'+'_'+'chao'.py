from datetime import datetime

a = 'hola'+'_'+'chao'
print(a)
print(type(a))

fecha = '2022/09/21 15:14:00+00'
fecha_1 = fecha.replace('/','').replace(':','').replace(' ','').replace('+','')

print(fecha_1)
a= '10:24:00'

a = a.split(':')[0]

print(a)
dic_horas={}

i =0
while i<24:
    dic_horas[i]=0
    i+=1

print(dic_horas)
b =list(dic_horas)

print(type(b))