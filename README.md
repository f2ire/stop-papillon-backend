# StopPapillon Backend

Backend API REST pour l’application **StopPapillon**, conçue pour aider à rester focus en bloquant les distractions ("papillonnage").

---

## Fonctionnalités principales

- Gestion des utilisateurs (authentification simple)
- Gestion des sessions de focus (type Pomodoro amélioré)
- Stockage et suivi des sessions et distractions
- Système de collection de papillons débloqués
- API REST sécurisée et propre

---

## Stack technique

- Python 3.11+
- Django 4.x
- Django REST Framework
- PostgreSQL
- python-decouple pour la gestion des variables d’environnement
- dj-database-url pour la configuration facile de la base de données

---

## Installation & Setup

### Prérequis

- Python 3.11+
- PostgreSQL
- `virtualenv` recommandé

### Étapes

1. Cloner le repo :

```bash
git clone https://github.com/ton-utilisateur/stop-papillon-backend.git
cd stop-papillon-backend
