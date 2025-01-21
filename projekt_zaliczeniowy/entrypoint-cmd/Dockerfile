# Użyj oficjalnego obrazu Pythona
FROM python:3.9-slim

# Skopiuj plik Pythonowy do obrazu
COPY script.py /app/script.py

# Ustaw katalog roboczy
WORKDIR /app

# Domyślna komenda przy użyciu ENTRYPOINT
ENTRYPOINT ["python3", "script.py"]
