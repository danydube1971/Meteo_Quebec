Ce script en Python est une application graphique de bureau pour afficher les prévisions météorologiques pour la ville de Québec. Voici une explication détaillée de ses composants et de son fonctionnement :

![Meteo_Quebec_capture](https://github.com/danydube1971/Meteo_Quebec/assets/74633244/8d1e1ec0-ac4d-4ecc-a201-8f7908cc3ea1)


1. **Importation des modules nécessaires** :
   - `requests` pour effectuer des requêtes HTTP.
   - `datetime` pour manipuler des dates et des heures.
   - `tkinter` et `ttk` pour créer l'interface utilisateur graphique.
   - `tkcalendar` pour intégrer un calendrier dans l'interface.
   - `PIL` (Python Imaging Library) pour manipuler des images.
   - `sys` et `os` pour interagir avec le système d'exploitation.

2. **Fonction `resource_path`** :
   - Sert à trouver le chemin absolu d'une ressource, utile lors de l'utilisation de PyInstaller pour créer un exécutable.

3. **Fonction `fetch_weather`** :
   - Récupère les données météorologiques de l'API OpenWeatherMap pour Québec, en utilisant une clé API spécifique.
   - Affiche un message d'erreur si la requête échoue.
   - Sinon, elle appelle `display_weather` pour afficher les données.

4. **Fonction `get_weather_image`** :
   - Retourne une image représentant les conditions météorologiques basée sur la description (ex: couvert, nuageux, ensoleillé, etc.).
   - Les images doivent être présentes localement dans le dossier de l'application.

5. **Fonction `display_weather`** :
   - Trouve les prévisions les plus proches pour la date sélectionnée dans le calendrier.
   - Affiche les détails de la prévision (température, description, précipitations) et une image correspondante.

6. **Configuration de l'interface graphique (GUI)** :
   - Crée une fenêtre principale avec `tk.Tk()`.
   - Ajoute un calendrier pour sélectionner une date.
   - Ajoute un bouton pour lancer la récupération des données météo.
   - Ajoute des labels pour afficher les informations météorologiques et l'image.

7. **Boucle principale** :
   - `root.mainloop()` démarre l'interface graphique et attend les interactions de l'utilisateur.

### Comment utiliser l'application :

1. Lancez le script Python dans un terminal comme *$ python3 "Meteo_Quebec_GUI.py"*. Cela ouvre l'interface graphique.
2. Sélectionnez une date dans le calendrier.
3. Cliquez sur "Obtenir la météo" pour afficher les prévisions météorologiques pour cette date.
4. Les détails de la météo et une image correspondant à la description de la météo s'afficheront.

### Remarques importantes :
- Assurez-vous que toutes les images mentionnées dans `get_weather_image` sont présentes dans le dossier de l'application.
- La clé API et les coordonnées géographiques sont spécifiques à cet exemple. Vous devrez peut-être les remplacer par vos propres clés et coordonnées.
