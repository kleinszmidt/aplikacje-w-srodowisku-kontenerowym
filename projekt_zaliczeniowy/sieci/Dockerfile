# Wybieramy obraz bazowy
FROM python:3.9-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki aplikacji do kontenera
COPY . /app

# Instalujemy wymagane biblioteki
RUN pip install --no-cache-dir -r requirements.txt

# Uruchamiamy aplikację
CMD ["python", "app.py"]
