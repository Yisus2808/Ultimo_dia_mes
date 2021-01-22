# Crea una función que te regrese el último día de un mes recibido por valor, se recibe como parámetro mes y año.
import calendar
from datetime import datetime

now = datetime.now()

mes = input("Ingresa el mes: ")
anio = input("Ingresa el anio: ")

mes = int(mes)
anio = int(anio)

# now_anio = now.year
# now_mes = now.month

if mes < 1 or anio < 1 or mes > 12:
    print("INGRESE DATOS CORRECTOS")
    
# elif anio > now_anio or mes > now_mes:
#     print("INGRESE DATOS CORRECTOS")
    
else:
    ultimo_dia = calendar.monthrange(anio, mes)[1]
    print(f"El ultimo dia del mes {mes} en el año {anio} es: ", ultimo_dia)