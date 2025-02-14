FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .  # Copie tout à la racine, y compris 'src' si nécessaire

EXPOSE 5000

# Modifie la commande pour correspondre à l'emplacement de 'app.py'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
