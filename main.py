import csv

with open('cargacad.csv') as csv_pca:
    reader = csv.reader(csv_pca, delimiter=";")
    for row in reader:

        id_asignatura = row[3]
        aula = row[7]
        hrdeci = float(row[9])
        duracion = int(row[10])
        tipodato = type(hrdeci)
        #Hora de inicio
        Conversion = hrdeci * 24
        horas = int(Conversion)
        minutos = int((Conversion * 60) % 60)
        if minutos == 0:
            minutos = "00"
        Hora_inicio = str(horas) + ':' + str(minutos)
        #Hora Final
        ConversionFinalp1 = hrdeci+(0.03125*duracion)
        ConversionFinalp2 = ConversionFinalp1 * 24
        horasf = int(ConversionFinalp2)
        minutosf = int((ConversionFinalp2 * 60) % 60)
        if minutosf == 0:
            minutosf = "00"
        Hora_fin = str(horasf) + ':' + str(minutosf)

        #Hora_inicio2 = str(int(math.floor(Conversion))) + ':' + str(int((Conversion % (math.floor(Conversion))) * 60)) + ':' + str(int(((Conversion % (math.floor(Conversion))) * 60) % math.floor(((Conversion % (math.floor(Conversion))) * 60)) * 60))
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
                'fecha_inicio': 'Julio 23, 2022 '+Hora_inicio+':00 PM',
                'fecha_fin': 'Julio 23, 2022 '+Hora_fin+':00 PM',
                'descripcion': 'HOLA',
                'recurrencia': 'Semanal',
                'fecha_fin_evento': 'Julio 31, 2022 05:00:00 PM',
                'color': '11',
                'idEvent': ''
            }
        }
        print(Json_GCF)
