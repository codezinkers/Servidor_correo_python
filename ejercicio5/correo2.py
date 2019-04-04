# encoding: utf-8
# import time
# import mysql.connector
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# ----------------variable comun--------------------
fichero='usuarios.csv'
ficheroTXT=open('file.txt').read()
resultado=[]
nombre= ""
mail= ""

# ---------conversion del csv  a un array-----------
def fichero_csv():
    with open(fichero) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        row1=next(reader)
        # cada fila es una lista
        for row in reader:
            # resultado.append(row)
            resultado.append(row)
        return resultado
fichero_csv()

# ALEX: el envio se esta enviando mediante hotmail, para poder enviarlos por 1onos hay que cambiar el smtp.ionos.com con su puerto
# correspondiente 465 o 587, tambien se puede adjuntar archivos.
def enviar_mail(nombre, mail):
    # Iniciamos los parámetros del script
    remitente = 'practicasdevacademy@hotmail.com'
    destinatarios = [mail]
    asunto = 'BIENVENIDO A DEV ACADEMY'
    # cuerpo = 'Hola '+nombre+' Bienvenido a devAcademy'
    # despues de la lectura del archivo  se realiza un replace del nombre(tiene que llamarse igual en el file.txt y en el codigo) y se le pasa el nombre
    cuerpo = ficheroTXT.replace("XXXXNOMBREXXXX", nombre)
    # print(cuerpo)
    # ruta_adjunto = 'file.txt'
    # nombre_adjunto = 'file.txt'

    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()

    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto

    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Abrimos el archivo que vamos a adjuntar
    # archivo_adjunto = open(ruta_adjunto, 'rb')

    # Creamos un objeto MIME base
    # adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    # adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    # encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    # adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    # mensaje.attach(adjunto_MIME)

    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.live.com', 25)

    # Ciframos la conexión
    sesion_smtp.starttls()

    # Iniciamos sesión en el servidor
    sesion_smtp.login('practicasdevacademy@hotmail.com','Alex2019!')

    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()

    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatarios, texto)

    # Cerramos la conexión
    sesion_smtp.quit()

# ALEX: funcion que no nos recorre el array de resultado que contiene los datos del csvfile y llama a una funcion que se encarga de enviar los mensajes.
#  despues de cada llamada a una nuncion se reliza un delay de 60" para evitar el bloquedo de la cuenta como spam
def enviar2():
    contador=0
    for i in range(len(resultado)):
        enviar_mail(resultado[i][0],resultado[i][1])
        print('se han enviado  un mensaje a',resultado[i][1])
        contador+=1
        # time.sleep(60)
    print('se han enviado',contador,"mensajes")
enviar2()
