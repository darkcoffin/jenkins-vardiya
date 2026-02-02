import psycopg2
import datetime
import os

def veritabani_isleri():
    try:
        # Jenkins ortaminda miyiz, yoksa lokalde mi?
        # Jenkins'te 'veritabani', lokalde 'localhost' kullanilir.
        # Simdilik direkt Jenkins ayarini yapiyoruz:
        db_host = "veritabani" 
        
        print(f"Baglanti deneniyor: {db_host}...")
        
        baglanti = psycopg2.connect(
            host=db_host,
            database="postgres",
            user="postgres",
            password="gizlisifre",
            port="5432"
        )

        imlec = baglanti.cursor()

        # Tablo yoksa olustur
        imlec.execute("CREATE TABLE IF NOT EXISTS is_listesi (id SERIAL PRIMARY KEY, zaman TIMESTAMP, is_adi VARCHAR(100));")

        # Veriyi Ekle
        zaman = datetime.datetime.now()
        mesaj = "GITHUB-V2: Kod Buluttan Geldi!"
        imlec.execute("INSERT INTO is_listesi (zaman, is_adi) VALUES (%s, %s)", (zaman, mesaj))

        baglanti.commit()
        print(f"✅ BASARILI: '{mesaj}' kaydi eklendi.")

        imlec.close()
        baglanti.close()

    except Exception as e:
        print("❌ HATA OLUSTU:", e)
        exit(1) # Jenkins hatayi anlasin diye

if __name__ == "__main__":
    veritabani_isleri()
