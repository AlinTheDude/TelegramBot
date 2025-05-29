# Immagine base
FROM python:3.10-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file
COPY . .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Avvia il bot
CMD ["python", "bot.py"]
