# Health Calculator Microservice with CI/CD Pipeline on Azure

## Objectif

Le but de ce projet est de développer un microservice en Python qui calcule des indicateurs de santé tels que l'IMC (BMI) et le BMR (Basal Metabolic Rate) via une API REST. Le microservice sera conteneurisé à l'aide de Docker, géré avec un fichier Makefile, et déployé sur Azure en utilisant GitHub Actions pour le pipeline CI/CD.

## Calculs Mathématiques pour les Indicateurs de Santé

### 1. Indice de Masse Corporelle (IMC) - BMI
Formule :  
\[ \text{BMI} = \frac{\text{poids (kg)}}{\left(\text{taille (m)}\right)^2} \]

### 2. Taux Métabolique de Base (BMR) - Harris-Benedict

#### Pour les hommes :
\[ \text{BMR} = 88.362 + (13.397 \times \text{poids (kg)}) + (4.799 \times \text{taille (cm)}) - (5.677 \times \text{âge (années)}) \]

#### Pour les femmes :
\[ \text{BMR} = 447.593 + (9.247 \times \text{poids (kg)}) + (3.098 \times \text{taille (cm)}) - (4.330 \times \text{âge (années)}) \]

## Exigences du Projet

### 1. Microservice Python

- Développer une API Flask avec les points de terminaison suivants :
  - `/bmi` : Calcule l'IMC en utilisant la taille (mètres) et le poids (kg).
  - `/bmr` : Calcule le BMR en utilisant la taille (cm), le poids (kg), l'âge et le sexe.

### 2. Conteneurisation avec Docker

- Créer un `Dockerfile` pour conteneuriser l'application.

### 3. Orchestration avec Makefile

- Automatiser l'installation, les tests, l'exécution et la construction avec des commandes `make` :
  - `make init`
  - `make run`
  - `make test`
  - `make build`

### 4. Gestion des Dépendances

- Gérer les dépendances dans le fichier `requirements.txt`.

### 5. Tests

- Rédiger des tests unitaires pour valider les calculs d'IMC et de BMR et les points de terminaison de l'API.

### 6. Pipeline CI/CD avec GitHub Actions

- Mettre en place un pipeline pour automatiser les tests et le déploiement lors de chaque poussée de code.

### 7. Déploiement sur Azure

- Utiliser Azure App Service pour héberger le microservice conteneurisé.

## Tester l'Application Web

Une fois l'application déployée, vous pouvez tester les API exposées par votre application. Voici un exemple de commande `curl` pour tester l'API BMI :

```bash
curl -X POST http://my-app-flask.azurewebsites.net/bmi \
  -H "Content-Type: application/json" \
  -d '{"height": 1.75, "weight": 70}'
```

```bash
curl -X POST http://my-app-flask.azurewebsites.net/bmr \
  -H "Content-Type: application/json" \
  -d '{"height": 1.75, "weight": 70, "age": 30, "gender": "male"}'
```