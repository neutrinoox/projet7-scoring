# Projet 7 Scoring

## Télécharger le notebook et l'ouvrir dans Google Colab

### Où trouver le terminal ?

Avant de lancer la commande `./scripts/package_notebook.sh`, ouvre la fenêtre où tu peux taper du texte :

- **Dans VS Code** : clique sur le menu **View ▸ Terminal** (ou **Affichage ▸ Terminal**). Un onglet « Terminal » apparaît en bas de la fenêtre ; clique dedans pour commencer à écrire.
- **Dans JupyterLab** : en haut à gauche, clique sur le bouton **+ Launcher**, puis sur l’icône **Terminal** dans la section « Other ». Une fenêtre noire s’ouvre dans un nouvel onglet ; c’est l’endroit où tu tapes les commandes.
- **Sur Windows sans ces outils** : appuie sur **Win + R**, tape `cmd` puis valide pour ouvrir l’invite de commandes (ou cherche « PowerShell » dans le menu Démarrer). Navigue ensuite jusqu’au dossier du projet avant de lancer la commande.
- **Sur macOS ou Linux** : ouvre l’application **Terminal** (recherche-la dans Spotlight ou dans la liste des applications), puis va dans le dossier du projet.

Une fois le terminal affiché, clique à l’intérieur pour t’assurer que le curseur clignote : tu peux maintenant taper les commandes décrites ci-dessous.

### Mode « ultra débutant » : récupérer le fichier sur ton ordinateur

1. **Prépare le fichier.**
   - Clique sur la fenêtre du Terminal (la zone noire où tu tapes des commandes).
   - Tape exactement :

     ```bash
     ./scripts/package_notebook.sh
     ```

     puis appuie sur **Entrée**. Patiente quelques secondes : un message « `Archive générée : …/dist/V_Maxime_2_notebook_modélisation_092025.zip` » va s’afficher. Ce fichier `.zip` est comme un sac qui contient le notebook.

2. **Récupère ce sac sur ton ordinateur.**
   - Si tu utilises VS Code ou JupyterLab : dans le panneau de gauche, ouvre le dossier `dist`, fais un clic droit sur `V_Maxime_2_notebook_modélisation_092025.zip` puis choisis **Download** ou **Télécharger**.
   - Si tu es dans un autre outil (par exemple un terminal distant), utilise la commande `scp` ou l’outil de transfert de fichiers proposé par ta plateforme pour rapatrier le fichier `dist/V_Maxime_2_notebook_modélisation_092025.zip`.

3. **Ouvre le sac.**
   - Double-clique sur le fichier `.zip` depuis ton ordinateur puis clique sur « Extraire » pour obtenir le fichier `V_Maxime_2_notebook_modélisation_092025.ipynb`.

4. **Ouvre le notebook dans Colab.**
   - Va sur [Google Colab](https://colab.research.google.com/).
   - Clique sur **File ▸ Upload notebook** (ou **Fichier ▸ Importer un notebook**).
   - Choisis le fichier `.ipynb` que tu viens d’extraire et valide. Colab va s’ouvrir avec exactement le notebook que tu viens de récupérer.

### Mode avancé : ouvrir directement depuis GitHub

1. Pousse le dépôt sur GitHub (ou assure-toi qu’il y est déjà).
2. Dans Google Colab, clique sur **File ▸ Open notebook ▸ GitHub**.
3. Recherche le dépôt GitHub, sélectionne la branche voulue puis choisis `V_Maxime_2_notebook_modélisation_092025.ipynb`.
4. Colab ouvrira directement le notebook sans téléchargement manuel, ce qui te permet de l’exécuter en ligne.

> Astuce : pour partager un lien direct, utilise l’URL `https://colab.research.google.com/github/<utilisateur>/<dépôt>/blob/<branche>/V_Maxime_2_notebook_modélisation_092025.ipynb` en remplaçant les éléments entre chevrons par tes valeurs.
