FROM python:3.12-slim

WORKDIR /app

# Copie le fichier requirements.txt à la racine
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie tous les fichiers de l'application à la racine
COPY . .

EXPOSE 5000

# Point d'entrée pour Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
