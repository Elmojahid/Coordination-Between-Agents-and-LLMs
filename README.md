# Système Multi-Agents avec LLM pour la Coordination de Projets

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Description

Ce projet implémente un système multi-agents intelligent utilisant des LLMs (Large Language Models) pour coordonner et gérer des projets de développement logiciel. Chaque agent est spécialisé dans un rôle spécifique et utilise l'IA pour prendre des décisions éclairées.

## 🌟 Caractéristiques

- **Agents Spécialisés** :
  - Project Manager : Gestion et attribution des tâches
  - Developer : Analyse et implémentation
  - Code Reviewer : Revue et qualité du code
  - Architect : Décisions architecturales

- **Interface Web** :
  - Dashboard interactif
  - Suivi en temps réel des tâches
  - Visualisation des revues de code

- **Intégration IA** :
  - Utilisation de Deepseek pour la prise de décision
  - Communication naturelle entre agents
  - Analyse intelligente des tâches

## 🛠️ Technologies

- Python 3.x
- FastAPI
- Vue.js
- Deepseek AI
- TailwindCSS

## 📦 Installation

1. Cloner le repository :
```bash
git clone [URL_DU_REPO]
cd coordination_between_agents_project
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Configuration :
```bash
cp .env.example .env
# Éditer .env et ajouter votre clé API Deepseek
```

## 🚀 Utilisation

1. Démarrer l'interface web :
```bash
python web_interface.py
```

2. Accéder à l'interface :
```
http://localhost:8000
```

3. Pour l'exemple en ligne de commande :
```bash
python example_project.py
```

## 📁 Structure du Projet

```
├── agent.py                # Classe de base des agents
├── specialized_agents.py   # Implémentation des agents spécialisés
├── coordinator.py          # Système de coordination de base
├── project_coordinator.py  # Coordinateur spécifique aux projets
├── web_interface.py       # Interface web FastAPI
├── templates/             # Templates HTML
└── example_project.py     # Exemple d'utilisation
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Ouvrir une issue pour des bugs ou suggestions
- Proposer des pull requests
- Améliorer la documentation

## 👤 Auteur

**El Mustapha EL MOJAHID**

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

⭐️ Si ce projet vous a été utile, n'hésitez pas à lui mettre une étoile sur GitHub !
