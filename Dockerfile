# Gebruik een officiële Python 3.8 runtime als basisimage
FROM python:3.8-slim

# Stel de werkdirectory in
WORKDIR /app

# Kopieer de vereisten en installeer afhankelijkheden
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de rest van de applicatie
COPY . .

# Definieer het commando om de applicatie uit te voeren
CMD ["python", "main.py"]
