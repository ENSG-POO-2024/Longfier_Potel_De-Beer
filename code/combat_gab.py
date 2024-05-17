# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:30:36 2024

@author: gpotel
"""


import numpy as np
import random as rd
from tools import *
from joueur import *


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
        self.level = level
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
    def __init__(self, player, equipe2):
        self.player = player
        self.equipe1 = player.equipe
        self.mainpokemon1 = player.equipe[0]
        self.equipe2 = equipe2
        self.mainpokemon2 = equipe2[0]

        self.pkmndispo = []
        for i in player.equipe :
            if i.pointsdevie > 0 :
                self.pkmndispo.append(i.nom)



    def changement_pokemon(self, changeur):
        self.mainpokemon1 = changeur



    def pokemon_KO_ami(self):
        for i in range(len(self.equipe1)):
            if self.equipe1[i].pointsdevie > 0:
                self.pkmndispo.append(self.equipe1[i].nom)
        if self.pkmndispo == []:
            return "perdu"

        elif self.mainpokemon1.pointsdevie <= 0:
            return "poke ko"

        else :
            return "continue"



    def pokemon_KO_ennemi(self):
        pkmndispo = []
        for i in range(len(self.equipe2)):
            if self.equipe2[i].pointsdevie > 0:
                pkmndispo.append(self.equipe2[i].nom)
        if self.mainpokemon2.pointsdevie <= 0:
            if len(pkmndispo) == []:
                for i in range(len(self.equipe2)):
                    if self.equipe2[i].nom == pkmndispo[0]:
                        self.mainpokemon2 = self.equipe2[i]
                        break
            else:
                return('Finito')



    def attaque_degats(self,attaque,poke_att,poke_def):
        if attaque == 'normale' :
            puiss = poke_att.attaqueneutre
            typ = 'Normal'

        elif attaque == 'type1' :
            puiss = poke_att.attaquetype1
            typ = poke_att.type1
            
        else :
            puiss = poke_att.attaquetype2
            typ = poke_att.type2

        STAB = 1.5 #Quand un pokémon fait une attaque de son type, il bénéficie des dégats * 1.5. Ici nous n'avons pas de cas où ça n'arrive pas
        
        T = poke_att.speed//2
        rand = rd.randint(0,255)
        if T > rand:
            CoupCrit = (2 * self.mainpokemon1.level + 5) / (self.mainpokemon1.level + 5)
        else:
            CoupCrit = 1
        
        NombreAleatoire = rd.randint(85,100)/100        #Nb random entre 0.85 et 1
        
        EffiSurType1 = table_affin[dict_types[typ],dict_types[poke_def.type1]]
        if poke_def.type2 != 'None':
            EffiSurType2 = table_affin[dict_types[typ],dict_types[poke_def.type2]]
        else:
            EffiSurType2 = 1
        EffiType = EffiSurType1 * EffiSurType2   #Si double faiblesse: EffiType = 4
        
        CM = STAB * CoupCrit * NombreAleatoire * EffiType

        degats = np.floor((np.floor(np.floor(np.floor(poke_att.level * 0.4 + 2) * poke_att.attack * puiss / poke_def.defense) / 50) + 2) * CM)

        if poke_att == self.mainpokemon2 :
            self.mainpokemon1.subir_degats(degats)
        else :
            self.mainpokemon2.subir_degats(degats)



    def attaque_ennemie(self):
        random = rd.random()
        if random < 0.5 :
            if self.mainpokemon2.type2 != 'None' :
                self.attaque_degats('type2', self.mainpokemon2, self.mainpokemon1)
            else :
                self.attaque_degats('normale', self.mainpokemon2, self.mainpokemon1)
        else :
            self.attaque_degats('type1', self.mainpokemon2, self.mainpokemon1)
        return self.pokemon_KO_ami()



    def attaque_alliee(self,attaque):
        self.attaque_degats(attaque, self.mainpokemon1, self.mainpokemon2)
        return self.pokemon_KO_ennemi()
        


    def capture(self, Bball = 1.5):   #On considère que l'on utilise toujours des Super Balls donc Bball = 1.5
        a = (1 - 2/3 * (self.mainpokemon2.pointsdevie / self.mainpokemon2.pointsdevieTOT)) * Taux_Capture_Pokemon[self.mainpokemon2.nom] * Bball  #On ne prend pas en compte Bstatut (car nous n'avons pas implémenté les statuts^^)
        b = 65535 * (a/255)**(1/4)
        print(a)
        print(b)
        if a >= 255:
            if len(self.equipe1) < 6:
                self.equipe1.append(self.mainpokemon2)
            else:
                self.player.pc.append(self.mainpokemon2)
            return 'capture'
        else:
            booleen = True
            for i in range(3):
                if rd.randint(0,65535) > b:
                    booleen = False
            if not booleen:
                return 'rate'
            else:
                if len(self.equipe1) < 6:
                    self.equipe1.append(self.mainpokemon2)
                else:
                     self.player.pc.append(self.mainpokemon2)
                return 'capture'

    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    equipecool = Combat(Joueur((0,0),[Pokemon('Charmander'),Pokemon('Squirtle'),Pokemon('Zapdos')],[]), [Pokemon('Caterpie'), Pokemon('Kakuna'), Pokemon('Articuno')])
    sala = Pokemon('Charmander')

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