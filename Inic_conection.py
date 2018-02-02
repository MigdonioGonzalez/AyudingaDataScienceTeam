import httplib2
import sys
from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

#Se requiere que el archivo cliente_secret.json, expecificar ruta de ser necesario
archivo_cliente = 'client_secret.json'
scope = ['https://www.googleapis.com/auth/youtube.readonly']
service = 'youtube'
ver = 'v3'

#Funcion para crear un servicio de youtube
def autenficar():

    #Extrae los archivos secretos
    flow = flow_from_clientsecrets(archivo_cliente, scope=scope)
    almacenamiento = Storage('%s-oauth2.json' % sys.argv[0])
    credenciales = almacenamiento.get()

    #Verifica si hay algun archivo previo con credenciales
    if credenciales is None or credenciales.invalid:
        band = argparser.parse_args()
        credenciales = run_flow(flow, almacenamiento, band)

    #returna un servicio de youtube
    return build(service, ver, http=credenciales.authorize(httplib2.Http()))


#En caso de añadir a otro archivo, eliminar el siguiente if
if __name__ == '__main__':
    yt = autenficar()
