import os
import requests
import firebase_admin
from firebase_admin import credentials, db
import shutil

def download_service_account_key(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return save_path
    else:
        raise Exception(f"Failed to download service account key from {url}")
    

def initialize_firebase(service_account_url, database_url, upload_folder = '/tmp'):
    os.makedirs(upload_folder, exist_ok=True)
    service_account_path = os.path.join(upload_folder,'service-account.json')

    try:
        download_service_account_key(service_account_url, service_account_path)
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': database_url
        })
        return db.reference('/')
    except Exception as e:
        print(e)
        exit(1)

# define your service account URL and Firebase Realtime Database URL

# Define the path to your configuration file

# SERVICE_ACCOUNT_FILE = './service-account.json'

# Load the configuration from JSON file
# SERVICE_ACCOUNT_URL = os.path.abspath(SERVICE_ACCOUNT_FILE)
SERVICE_ACCOUNT_URL = "https://firebasestorage.googleapis.com/v0/b/grijeshalgo.appspot.com/o/serviceAccountKey%2Fservice-account.json?alt=media&token=2d16508e-edc4-46b6-9b7c-517417591b0c"
DATABASE_URL = 'https://grijeshalgo-default-rtdb.firebaseio.com/'

# firebase initialize
firebase_ref = initialize_firebase(SERVICE_ACCOUNT_URL,DATABASE_URL)

# firbase configuration details for REST API
apiKey = "AIzaSyB4ZjNOrCl4HaH0MTFgW8s5xHVZz6JBemQ"
authDomain = "grijeshalgo.firebaseapp.com"
databaseURL = "https://grijeshalgo-default-rtdb.firebaseio.com"
projectId = "grijeshalgo"
storageBucket = "grijeshalgo.appspot.com"
messagingSenderId = "395128672277"
appId = "1:395128672277:web:ddd9e025c47f3024c9be1c"
measurementId = "G-FMBV3VZDB9"





