import os
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

archivo_cliente = 'client_secret.json'
scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']
api_service = 'youtube'
api_version = 'v3'

def auth_service():
    flow = InstalledAppFlow.from_client_secrets_file(archivo_cliente,scopes)
    credenciales = flow.run_console()
    return build(api_service, api_version,credentials=credenciales)

if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = auth_service()
    result = service.channels().list('snippet,contentDetails,statistics').execute()
    print(result)


