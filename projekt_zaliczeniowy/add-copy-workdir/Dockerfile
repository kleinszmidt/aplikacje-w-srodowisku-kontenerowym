# Używamy obrazu bazowego
FROM python:3.9-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy plik example.txt do katalogu roboczego
COPY example.txt .

# Dodajemy plik another_example.txt do katalogu roboczego
ADD files/another_example.txt .

# Ustawiamy polecenie uruchamiane w kontenerze
CMD ["ls", "-l"]
