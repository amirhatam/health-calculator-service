FROM python:3.12-slim

WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le dossier 'src' et son contenu dans le répertoire de travail
COPY src/ /app/src/

# Exposer le port 5000
EXPOSE 5000

# Modifie la commande pour que Gunicorn utilise le bon chemin pour 'app.py'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "src.app:app"]
