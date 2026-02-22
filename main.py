import psycopg2
import datetime
import os
import requests # <-- İNTERNETE SESLENMEK İÇİN YENİ EKLENEN KÜTÜPHANE

# VIP Kimlik Bilgilerimiz (Güvenlik uyarımızı unutma, bu tokenları daha sonra değiştireceğiz!)
TELEGRAM_TOKEN = "8384452056:AAFhW3_eyVyAj186mF6VVG9RjIWZ2JNxqys"
CHAT_ID = "7356374196"

def telegram_mesaj_gonder(mesaj):
    """Telegram'ın sunucusuna HTTP GET isteği gönderen özel haberci fonksiyonumuz."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    parametreler = {
        "chat_id": CHAT_ID,
        "text": mesaj
    }
    try:
        # requests.get ile URL'ye gidip paketi teslim ediyoruz.
        requests.get(url, params=parametreler)
    except Exception as e:
        print("Telegram'a mesaj gönderilirken bir sorun oluştu:", e)

def veritabani_isleri():
    try:
        # Jenkins ortamında mıyız, yoksa lokalde mi?
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

        # Tablo yoksa oluştur
        imlec.execute("CREATE TABLE IF NOT EXISTS is_listesi (id SERIAL PRIMARY KEY, zaman TIMESTAMP, is_adi VARCHAR(100));")

        # Veriyi Ekle
        zaman = datetime.datetime.now()
        islem_mesaji = "OTOMASYON: Ellerimi klavyeden cektim, Jenkins otopilotta calisiyor!"
        imlec.execute("INSERT INTO is_listesi (zaman, is_adi) VALUES (%s, %s)", (zaman, islem_mesaji))

        baglanti.commit()
        
        # BAŞARI DURUMU: Hem terminale yaz hem Telegram'a gönder!
        basari_bildirimi = f"✅ JENKINS BİLDİRİMİ: Veritabanına '{islem_mesaji}' başarıyla eklendi."
        print(basari_bildirimi)
        telegram_mesaj_gonder(basari_bildirimi) # <-- C ŞIKKI: BAŞARIYI BİLDİR!

        imlec.close()
        baglanti.close()

    except Exception as e:
        # HATA DURUMU: Hem terminale yaz hem Telegram'a acil durum gönder!
        hata_bildirimi = f"❌ JENKINS ACİL DURUM: Veritabanı bağlantısı patladı! Detay: {e}"
        print(hata_bildirimi)
        telegram_mesaj_gonder(hata_bildirimi) # <-- C ŞIKKI: HATAYI BİLDİR!
        exit(1) # Jenkins hatayı anlasın diye

if __name__ == "__main__":
    veritabani_isleri()import psycopg2
import datetime
import os
import requests # <-- İNTERNETE SESLENMEK İÇİN YENİ EKLENEN KÜTÜPHANE

# VIP Kimlik Bilgilerimiz (Güvenlik uyarımızı unutma, bu tokenları daha sonra değiştireceğiz!)
TELEGRAM_TOKEN = "8384452056:AAFhW3_eyVyAj186mF6VVG9RjIWZ2JNxqys"
CHAT_ID = "7356374196"

def telegram_mesaj_gonder(mesaj):
    """Telegram'ın sunucusuna HTTP GET isteği gönderen özel haberci fonksiyonumuz."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    parametreler = {
        "chat_id": CHAT_ID,
        "text": mesaj
    }
    try:
        # requests.get ile URL'ye gidip paketi teslim ediyoruz.
        requests.get(url, params=parametreler)
    except Exception as e:
        print("Telegram'a mesaj gönderilirken bir sorun oluştu:", e)

def veritabani_isleri():
    try:
        # Jenkins ortamında mıyız, yoksa lokalde mi?
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

        # Tablo yoksa oluştur
        imlec.execute("CREATE TABLE IF NOT EXISTS is_listesi (id SERIAL PRIMARY KEY, zaman TIMESTAMP, is_adi VARCHAR(100));")

        # Veriyi Ekle
        zaman = datetime.datetime.now()
        islem_mesaji = "OTOMASYON: Ellerimi klavyeden cektim, Jenkins otopilotta calisiyor!"
        imlec.execute("INSERT INTO is_listesi (zaman, is_adi) VALUES (%s, %s)", (zaman, islem_mesaji))

        baglanti.commit()
        
        # BAŞARI DURUMU: Hem terminale yaz hem Telegram'a gönder!
        basari_bildirimi = f"✅ JENKINS BİLDİRİMİ: Veritabanına '{islem_mesaji}' başarıyla eklendi."
        print(basari_bildirimi)
        telegram_mesaj_gonder(basari_bildirimi) # <-- C ŞIKKI: BAŞARIYI BİLDİR!

        imlec.close()
        baglanti.close()

    except Exception as e:
        # HATA DURUMU: Hem terminale yaz hem Telegram'a acil durum gönder!
        hata_bildirimi = f"❌ JENKINS ACİL DURUM: Veritabanı bağlantısı patladı! Detay: {e}"
        print(hata_bildirimi)
        telegram_mesaj_gonder(hata_bildirimi) # <-- C ŞIKKI: HATAYI BİLDİR!
        exit(1) # Jenkins hatayı anlasın diye

if __name__ == "__main__":
    veritabani_isleri()import psycopg2
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
        mesaj = "OTOMASYON: Ellerimi klavyeden cektim, Jenkins otopilotta calisiyor!"
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
