import requests
import csv
import datetime

url='http://datos.madrid.es/egob/catalogo/212531-10515086-calidad-aire-tiempo-real.txt'

r=requests.get(url)
respuesta=r.content
horaAnterior = str((datetime.datetime.now() - datetime.timedelta(hours=1)).hour)
lecturaHora = "H" + horaAnterior
comprobacionHora = "V" + horaAnterior
print "Ultima lectura a las " + horaAnterior + "h"
datos = csv.DictReader(respuesta.splitlines(),delimiter=';')
for row in datos:
    if (row['ESTACION'] == "38") & (row['MAGNITUD'] == "8"):
        if row[comprobacionHora] == "V":
            print "Lectura valida"
        else:
            print "Lectura erronea"
        valorLectura = int(row[lecturaHora])
        if (180 < valorLectura < 200):
            estado = "PREAVISO"
        elif (200 < valorLectura < 400):
            estado = "AVISO"
        elif (valorLectura > 400):
            estado = "ALERTA"
        else:
            estado = "NORMAL"
        print "Nivel de N02 en Cuatro Caminos: " + str(valorLectura)
        print "Estado de la estacion: " + estado
