FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Menjalankan migrasi database saat container dijalankan
CMD ["sh", "-c", "flask db upgrade && flask run --host=0.0.0.0"]
