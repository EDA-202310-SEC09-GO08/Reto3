from datetime import datetime

a = 'hola'+'_'+'chao'
print(a)
print(type(a))

fecha = '2022/09/21 15:14:00+00'
fecha_1 = fecha.replace('/','').replace(':','').replace(' ','').replace('+','')

print(fecha_1)