import csv
import uuid
import sys
import os

# Menambahkan jalur folder Config ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Config')))

from firebase_config import db

def load_csv_to_firestore(csv_file_path, collection_name, primary_key_fields):
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        batch = db.batch()

        for row in csv_reader:
            # Membuat primary key berdasarkan kolom yang ditentukan
            primary_key = "_".join([row[field] for field in primary_key_fields])
            doc_id = primary_key if len(primary_key.split('_')) % 2 == 0 else str(uuid.uuid4())

            # Cek apakah dokumen dengan ID yang sama sudah ada
            doc_ref = db.collection(collection_name).document(doc_id)
            doc_snapshot = doc_ref.get()

            if doc_snapshot.exists:
                print(f"Dokumen dengan ID {doc_id} sudah ada di koleksi {collection_name}")
            else:
                batch.set(doc_ref, row)
                print(f"Dokumen dengan ID {doc_id} ditambahkan ke koleksi {collection_name}")

        batch.commit()
        print(f"Data dari {csv_file_path} dimuat ke koleksi Firestore {collection_name}")