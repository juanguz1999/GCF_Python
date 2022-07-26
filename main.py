import csv
import math

with open('cargacad.csv') as csv_pca:
    reader = csv.reader(csv_pca, delimiter=";")
    for row in reader:

        id_asignatura = row[3]
        aula = row[7]
        hrdeci = row[9]
        prueba = type(float(hrdeci))
        prueba2 = float(hrdeci)*24
        horas = int(prueba2)
        Hora_inicio = str(horas) + ':'
        #Hora_inicio = str(int(math.floor(prueba2))) + ':' + str(int((prueba2%(math.floor(prueba2)))*60)) + ':' + str(int(((prueba2%(math.floor(prueba2)))*60) % math.floor(((prueba2%(math.floor(prueba2)))*60))*60))
        Json_GCF = {
            'Llave_evento': {
                'id_grupo': '',
                'id_docente': '',
                'email_docente': 'docente@pca.edu.co',
                'id_asignatura': id_asignatura,
                'id_jornada': 'D'
            },
            'Datos_evento': {
                'calendar_id': 'pruebas1@pca.edu.co',
                'nombre_evento': 'Prueba Final',
                'asistentes': 'pruebas1@pca.edu.co,juan.guzmanm@pca.edu.co',
                'lugar': aula,
                #'fecha_inicio': 'Julio 23, 2022 '+Hora_inicio+' PM',
                'fecha_fin': "Julio 23, 2022 05:00:00 PM",
                'descripcion': 'HOLA',
                'recurrencia': 'Semanal',
                'fecha_fin_evento': 'Julio 31, 2022 05:00:00 PM',
                'color': '11',
                'idEvent': ''
            }
        }
        print(Hora_inicio)
