from flask import Flask, render_template_string
import psycopg2

app = Flask(__name__)

def verileri_getir():
    try:
        # Docker'daki veritabanımıza bağlanıp verileri çekiyoruz
        baglanti = psycopg2.connect(
            host="host.docker.internal",
            database="postgres",
            user="postgres",
            password="gizlisifre",
            port="5432"
        )
        imlec = baglanti.cursor()
        # Verileri en yeniden en eskiye doğru sıralayarak alıyoruz
        imlec.execute("SELECT * FROM is_listesi ORDER BY zaman DESC;")
        kayitlar = imlec.fetchall()
        
        imlec.close()
        baglanti.close()
        return kayitlar
    except Exception as e:
        return str(e)

@app.route('/')
def ana_sayfa():
    veriler = verileri_getir()
    
    # Veritabanı bağlantısı koparsa hata mesajı göster
    if isinstance(veriler, str):
        return f"<h1>Hata Oluştu!</h1><p>{veriler}</p>"

    # Basit ve Şık Bir Kontrol Paneli (Dashboard) Tasarımı
    html_sablonu = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Kontrol Paneli</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
            h1 { color: #2c3e50; text-align: center; }
            table { width: 80%; margin: 0 auto; border-collapse: collapse; background-color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            th, td { padding: 15px; border-bottom: 1px solid #ddd; text-align: left; }
            th { background-color: #2980b9; color: white; }
            tr:hover { background-color: #f5f5f5; }
        </style>
    </head>
    <body>
        <h1>🚀 M4 Uzay Gemisi: DevOps Kontrol Paneli</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Zaman (Timestamp)</th>
                <th>İşlem Mesajı (Log)</th>
            </tr>
            {% for kayit in veriler %}
            <tr>
                <td>{{ kayit[0] }}</td>
                <td>{{ kayit[1] }}</td>
                <td>{{ kayit[2] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html_sablonu, veriler=veriler)

if __name__ == '__main__':
    # Web sunucusunu 5001 portunda başlatıyoruz
    app.run(host='0.0.0.0', port=5001)
