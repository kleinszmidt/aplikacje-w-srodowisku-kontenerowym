# Bazowy obraz
FROM alpine:3.18

# Ustaw katalog roboczy
WORKDIR /app

# Instaluj zależności aplikacji (przykład - dostosuj do swojej aplikacji)
RUN apk add --no-cache python3 curl

# Dodaj użytkownika o nazwie 'appuser' bez hasła
RUN adduser -D -u 1000 appuser

# Zmień właściciela katalogu roboczego na 'appuser'
RUN chown appuser /app

# Przełącz na użytkownika 'appuser'
USER appuser

# Kopiuj pliki aplikacji
COPY . /app

# Uruchom aplikację (przykładowy wpis)
CMD ["python3", "app.py"]
