import firebase_admin
from firebase_admin import credentials, firestore

# Path ke file kredensial
cred_path = '../serviceAccountKey.json'
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Menginisialisasi Firestore
db = firestore.client()