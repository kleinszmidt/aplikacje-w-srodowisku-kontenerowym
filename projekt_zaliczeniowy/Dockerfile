# Użyj obrazu bazowego z Pythonem
FROM python:3.9-slim

# Utwórz folder roboczy w kontenerze
WORKDIR /app

# Skopiuj folder 'code' z hosta do kontenera
COPY code /app/code

# Ustaw domyślny katalog roboczy na folder z kodem
WORKDIR /app/code

# Domyślny command do uruchamiania Pythona
CMD ["python", "hello.py"]
