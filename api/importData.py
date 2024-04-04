import pandas as pd
from  .models import Tab_aux  
def importer_donnees_de_excel(chemin_fichier_excel):
    # Lecture du fichier Excel
    data = pd.read_excel(chemin_fichier_excel)

    # Parcours des lignes du fichier Excel
    for index, row in data.iterrows():
        # Création d'une instance de Tab_aux pour chaque ligne
        tab_aux_instance = Tab_aux(
            code=row['CODE'],  # Utilisez les noms de colonnes du fichier Excel
            libelle=row['LIBELLE black']
            # Vous pouvez ajouter d'autres champs si nécessaire
        )
        # Sauvegarde de l'instance dans la base de données
        tab_aux_instance.save()

    print("Données importées avec succès.")

# Utilisation de la fonction pour importer les données
  
chemin_fichier_excel = "C:\\Users\\PC\\Downloads\\TAB_AUX (1).xlsx"  # Utilisez des doubles barres obliques ou une barre oblique
importer_donnees_de_excel(chemin_fichier_excel)