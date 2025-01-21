import time
import psycopg2
from psycopg2 import OperationalError

# Funkcja do łączenia się z bazą danych
def create_connection():
    try:
        connection = psycopg2.connect(
            host="db-container",  # Nazwa kontenera bazy danych
            port="5432",          # Standardowy port PostgreSQL
            database="mydb",      # Nazwa bazy danych
            user="myuser",        # Użytkownik
            password="mypassword" # Hasło
        )
        return connection
    except OperationalError as e:
        print(f"Nie udało się połączyć: {e}")
        return None

# Pętla główna aplikacji
while True:
    connection = create_connection()
    if connection:
        print("Połączono z bazą danych!")
        connection.close()
    else:
        print("Błąd połączenia z bazą danych!")
    time.sleep(5)  # Czekaj 5 sekund przed kolejną próbą
