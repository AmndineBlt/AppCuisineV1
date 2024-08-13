import json
import os

CUR_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CUR_DIR, "database")


# Création de la classe Recette
class Recettes:
    # Initialisation de la recette avec tous les elements
    def __init__(self, nom_recette):
        self.nom_recette = nom_recette
        self.ingredients = []
        self.temps_cuisson = 0
        self.nb_personnes = 0
    
    # Ajouter ingrédients sous forme d'un dictionnaire
    def ajouter_ingredients(self, nom, quantite, unite):
        self.ingredients.append({"nom": nom, "quantite": quantite, "unite": unite})
    
    # Définir un temps de cuisson
    def def_temps_cuisson(self, temps):
        self.temps_cuisson = temps

    # Définir le nombre de personnes
    def def_nb_personnes(self, nb_personnes):
        self.nb_personnes = nb_personnes

    # Sérialisation pour encoder et decoder une recette
    def sauvegarde_recette(self, nom_recette):
        data = {
            "nom_recette": self.nom_recette,
            "ingredients": self.ingredients,
            "tps_cuisson": self.temps_cuisson,
            "nb_personnes": self.nb_personnes
        }

        recette = os.path.join(DATA_DIR, nom_recette)
        with open(recette, "w") as f:
            json.dump(data, f, indent=4)
        
    def afficher_recette(self, nom_recette, nv_nb_personnes):
        recette = os.path.join(DATA_DIR, nom_recette)

        with open(recette, "r") as f:
            data = json.load(f)
            print(f"Recette: {data['nom_recette']}")
            print(f"Pour {nv_nb_personnes} personnes")
            print("ingredients:")
            # Affichier les ingrédients en fonction du nombre de personnes
            for ingredient in data['ingredients']:
                calcule = (nv_nb_personnes * ingredient['quantite'] / data['nb_personnes'])
                print(f"- {ingredient['nom']}: {calcule} {ingredient['unite']}")
            print(f"Temps de cuisson: {data['tps_cuisson']} minutes")
            
            


if __name__ == "__main__":
    recette = Recettes("mousse_au_chocolat")
    recette.ajouter_ingredients("Chocolat noir", 200, "grammes")
    recette.ajouter_ingredients("Sucres vanille", 2, "sachets")
    recette.ajouter_ingredients("Oeufs", 3, "unite")
    recette.def_temps_cuisson(15)
    recette.def_nb_personnes(4)
    recette.sauvegarde_recette("mousse_au_chocolat")
    recette.afficher_recette("mousse_au_chocolat", 4)

"""
    recette = Recettes("tarte_aux_pommes")
    recette.ajouter_ingredients("Pommes", 3, "unite")
    recette.ajouter_ingredients("Compte de pommes", 300, "grammes")
    recette.ajouter_ingredients("Sucre", 3, "cas")
    recette.def_temps_cuisson(45)
    recette.def_nb_personnes(6)
    recette.sauvegarde_recette("tarte_aux_pommes")
    recette.afficher_recette("tarte_aux_pommes")
"""