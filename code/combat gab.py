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
        
    def afficher_nom(Pokemon):
        return Pokemon.nom
        
    def subir_degats(self, degats):
        #degats négatifs = heal
        self.pointsdevie = self.pointsdevie - degats

class Equipe(Pokemon):
    def __init__(self,equipe):
        self.equipe = equipe
        self.mainpokemon = equipe[0]
        self.noms = [self.equipe[i].nom for i in range(len(self.equipe))]
        
    def changement_pokemon(self, changeur):
        self.mainpokemon = changeur
        
    def pokemon_KO(self):
        self.mainpokemon.pointsdevie = 0
        print('Votre pokémon', self.mainpokemon.nom,'est KO')
        print('Changez de pokémon !')
        print('Vos pokémons disponibles :', self.noms)
        numero = input('Quel pokemon voulez-vous envoyer au combat ? ')
        for i in range(len(self.equipe)):
            if self.equipe[i].nom == input:
                self.mainpokemon = self.equipe[i]
        
    
equipetropcool = Equipe((Pokemon('Charmander'), Pokemon('Eevee'), Pokemon('Zapdos')))