# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:30:36 2024

@author: gpotel
"""


import numpy as np
import random as rd
from tools import *


def creationIVs():
    IV = []
    for i in range(6):
        IV.append(rd.randint(0,31))
    return IV







#Je définis EV = 85 parce que le max est 510 donc je répartis 85 par stats, inutile de faire une liste où j'écris 6 fois 85
#Je définis nature au cas où, cf https://www.pokebip.com/page/general/statistiques
#Pour les dégats : https://www.pokebip.com/page/jeuxvideo/guide_tactique_strategie_pokemon/formules_mathematiques
#Pour les captures : https://www.pokebip.com/page/jeuxvideo/rbvj/chances_capture
#Pour les attaque : https://www.pokepedia.fr/Liste_des_capacit%C3%A9s#OA
class Pokemon():
    def __init__(self, nom, level = 50, EV = 85, nature = 1):
        self.nom = nom
        self.IV = creationIVs()
        self.EV = EV
        self.nature = nature
        self.type1 = liste_stats_array[Nom_Indices_Pokemon[self.nom]][1]
        self.type2 = liste_stats_array[Nom_Indices_Pokemon[self.nom]][2]
        self.stats = liste_stats_array[Nom_Indices_Pokemon[self.nom]][3]
        pointsdevie =  (((self.IV[0] + 2 * int(self.stats[0]) + (np.floor(EV/4))) * (level/100)) + level + 10)
        self.pointsdevie = pointsdevie
        self.attack =       (((self.IV[1] + 2 * int(self.stats[1]) + (np.floor(EV / 4))) * (level/ 100)) + 5) * self.nature
        self.defense =      (((self.IV[2] + 2 * int(self.stats[2]) + (np.floor(EV / 4))) * (level/ 100)) + 5) * self.nature
        self.attackSpe =    (((self.IV[3] + 2 * int(self.stats[3]) + (np.floor(EV / 4))) * (level/ 100)) + 5) * self.nature
        self.defenseSpe =   (((self.IV[4] + 2 * int(self.stats[4]) + (np.floor(EV / 4))) * (level/ 100)) + 5) * self.nature
        self.speed =        (((self.IV[5] + 2 * int(self.stats[5]) + (np.floor(EV / 4))) * (level/ 100)) + 5) * self.nature
        self.pointsdevieTOT = pointsdevie
        self.attaqueneutre = 40   #Puissance, pas les dégats
        self.attaquetype1 = 80
        if self.type2 != 'None':
            self.attaquetype2 = 80
        
        
    def subir_degats(self, degats):
        #degats négatifs = heal
        self.pointsdevie = self.pointsdevie - degats

class Combat(Pokemon):
    def __init__(self, equipe1, equipe2):
        self.equipe1 = equipe1
        self.mainpokemon1 = equipe1[0]
        self.equipe2 = equipe2
        self.mainpokemon2 = equipe2[0]

        
    def changement_pokemon(self, changeur):
        self.mainpokemon = changeur
        
    def pokemon_KO_ami(self):
        pkmndispo = []
        for i in range(len(self.equipe1)):
            if self.equipe1[i].pointsdevie != 0:
                pkmndispo.append(self.equipe1[i].nom)
        if pkmndispo == []:
            print("Vous n'avez plus de Pokémon en état de se battre. Vous êtes nul !")
        elif self.mainpokemon1.pointsdevie == 0:
            print("Votre pokémon n'est plus en état de se battre.")
            print("Choisissez un pokémon parmi vos pokemons disponibles : ")
            booleen = False
            while booleen == False:
                print(pkmndispo)
                choix = input('Nom du pokémon choisi : ')
                if choix == 'stop':
                    booleen = True
                for i in range(len(self.equipe1)):
                    if str(self.equipe1[i].nom) == choix:
                        self.mainpokemon1 = self.equipe1[i]
                        booleen = True

    def pokemon_KO_ennemi(self):
        pkmndispo = []
        for i in range(len(self.equipe2)):
            if self.equipe2[i].pointsdevie != 0:
                pkmndispo.append(self.equipe2[i].nom)
        if self.mainpokemon2.pointsdevie == 0:
            if len(pkmndispo) != 0:
                for i in range(len(self.equipe2)):
                    if self.equipe2[i].nom == pkmndispo[0]:
                        self.mainpokemon2 = self.equipe2[i]
                        break
            else:
                return('Finito')
                
    def attaque(self):
        

        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    equipecool = Combat((Pokemon('Charmander'), Pokemon('Squirtle'), Pokemon('Mewtwo')), (Pokemon('Caterpie'), Pokemon('Kakuna'), Pokemon('Articuno')))
    
    
    
    # # Test pokemon_KO_ami :
    # equipecool.equipe1[0].pointsdevie = 0
    # equipecool.pokemon_KO_ami()
    # print('Nouveau mainpokemon :', equipecool.mainpokemon1.nom)
    
    
    
    # # Test pokemon_KO_ennemi :
    # equipecool.mainpokemon2.pointsdevie = 0
    # equipecool.pokemon_KO_ennemi()
    # print('Nouveau mainpokemon :', equipecool.mainpokemon2.nom)
    # equipecool.mainpokemon2.pointsdevie = 0
    # equipecool.pokemon_KO_ennemi()
    # print('Nouveau mainpokemon :', equipecool.mainpokemon2.nom)
    # equipecool.mainpokemon2.pointsdevie = 0
    # equipecool.pokemon_KO_ennemi()