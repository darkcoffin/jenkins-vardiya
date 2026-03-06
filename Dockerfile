# 1. Hangi işletim sistemini/motoru kullanacağız? (Hafif bir Python seçiyoruz)
FROM python:3.9-slim

# 2. Kutunun içinde kendimize bir çalışma klasörü açıyoruz
WORKDIR /app

# 3. Bizim app.py dosyamızı al, kutunun içine kopyala
COPY app.py .

# 4. Kodun çalışması için gereken kütüphaneleri kutunun içine kur
RUN pip install flask psycopg2-binary

# 5. Kutu çalıştırıldığında hangi komut ateşlensin?
CMD ["python", "app.py"]
