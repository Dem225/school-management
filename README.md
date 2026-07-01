 School Management System

Système de gestion scolaire en ligne de commande, développé en Python avec SQLite comme base de données. L'application permet de gérer les élèves, les enseignants, les matières, les notes et les absences à travers une interface interactive en console, avec des menus dédiés selon le rôle de l'utilisateur (Administrateur, Enseignant, Élève).

 Fonctionnalités

- **Gestion des élèves — ajout, modification, suppression et consultation des dossiers élèves
- **Gestion des enseignants — administration des comptes et informations des professeurs
- **Gestion des matières — création et attribution des matières enseignées
- **Gestion des notes — saisie et suivi des notes par élève et par matière
- **Gestion des absences — enregistrement et suivi de l'assiduité des élèves
- **Authentification par rôle — accès différencié selon le profil (Administrateur / Enseignant / Élève)
- **Génération de matricule — attribution automatique d'identifiants uniques
- **Journalisation (logs) — suivi des actions et des erreurs via un système de logs

## Stack technique

| Composant       | Technologie |
|-----------------|-------------|
| Langage         | Python 3    |
| Base de données | SQLite      |
| Interface       | CLI (ligne de commande) |

 Structure du projet

```
school-management/
├── confige/                     # Menus interactifs selon le rôle
│   ├── Menu.py                  # Menu principal
│   ├── Menu_choix_admin.py      # Menu Administrateur
│   ├── Menu_choix_teacher.py    # Menu Enseignant
│   └── Menu_choix_students.py   # Menu Élève
│
├── database/                    # Connexion et configuration de la base de données
│   └── DB.py
│
├── models/                      # Modèles de données (entités)
│   ├── students_Modeles.py      # Modèle Élève
│   ├── teachers_Modeles.py      # Modèle Enseignant
│   ├── matiere_Modeles.py       # Modèle Matière
│   ├── notes_Modeles.py         # Modèle Notes
│   ├── absences_Modeles.py      # Modèle Absences
│   └── utlisateur_Modeles.py    # Modèle Utilisateur
│
├── services/                    # Logique métier (couche service)
│   ├── services_auth.py         # Authentification
│   ├── service_students.py      # Services liés aux élèves
│   ├── service_teachers.py      # Services liés aux enseignants
│   └── service_user.py          # Services liés aux utilisateurs
│
├── utils/                       # Fonctions utilitaires
│   ├── gere_choix_utilisateur_principale.py
│   ├── gestione_students.py
│   ├── gestione_teacher.py
│   ├── util_Matricule.py        # Génération de matricules
│   └── logger.py                # Système de journalisation
│
├── MANAGER.db                   # Base de données SQLite
├── main.py                      # Point d'entrée de l'application
├── utils_connexion.py           # Gestion de la connexion utilisateur
└── sauvegade.log                # Fichier de logs
```

Architecture

Le projet suit une architecture en couches inspirée du pattern MVC :

- `models/` : représentent les entités de la base de données (Élève, Enseignant, Matière, Notes, Absences, Utilisateur)
- `services/` : contiennent la logique métier et les opérations sur les données (CRUD)
- `confige/` : gèrent l'affichage des menus et la navigation selon le rôle de l'utilisateur
- `database/` : centralise la connexion à la base SQLite
- `utils/` : regroupe les fonctions transverses (génération de matricule, logs, gestion des choix utilisateur)

 Installation

 Prérequis

- Python 3.12 ou supérieur

 Étapes

1. Cloner le dépôt :
```bash
git clone https://github.com/ZEBI-LOBOGNON/school-management.git
cd school-management
```

2. (Optionnel) Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

3. Lancer l'application :
```bash
python main.py
```

> La base de données `MANAGER.db` (SQLite) est créée/utilisée automatiquement, aucune configuration supplémentaire n'est nécessaire.

 Utilisation

Au lancement de `main.py`, l'utilisateur est invité à s'authentifier. Selon son rôle, il accède à un menu spécifique :

- Administrateur** : gestion complète des élèves, enseignants, matières, notes et absences
- Enseignant** : gestion des notes et des absences de ses élèves
- Élève** : consultation de ses notes et de son historique d'absences

 Roadmap

- [ ] Ajout d'une interface graphique (GUI)
- [ ] Export des bulletins de notes en PDF
- [ ] Statistiques et tableaux de bord
- [ ] Migration vers une base de données relationnelle plus robuste (PostgreSQL/MySQL)

 Contribution

Les contributions sont les bienvenues !

1. Forkez le projet
2. Créez votre branche (`git checkout -b feature/ma-fonctionnalite`)
3. Committez vos changements (`git commit -m 'Ajout de ma fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/ma-fonctionnalite`)
5. Ouvrez une Pull Request

 Licence

Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

 Auteur

**ZEBI LOBOGNON**

- GitHub : [@ZEBI-LOBOGNON](https://github.com/ZEBI-LOBOGNON)

---

N'hésitez pas à mettre une étoile si ce projet vous a été utile !
