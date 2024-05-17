# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:57:19 2024

@author: gpotel
"""

import numpy as np
import csv
import ast
import matplotlib.pyplot as plt
import random as rd

#np.loadtxt('../data/pokemon_coordinates.csv', skiprows = 1)

'''
J'ai isolé les coordonnées en X et en Y pour que ce soit + facile
Dans tableau_travail, les coordonnées sont multipliées par 35 et arrondies à l'unité
'''

with open('../data/pokemon_coordinates.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
data_array = np.array(data)

colonne_list = []
for i in range(data_array.shape[0]):
    colonne_list.append(data_array[i,1].split(','))
    if i == 0 :
        pass
    else:
        colonne_list[i][0] = float(colonne_list[i][0][1:-1])
        colonne_list[i][1] = float(colonne_list[i][1][:-1])

colonne_zeros = np.zeros((data_array.shape[0],1))
data_array = np.concatenate((data_array, colonne_zeros),1)
data_array[1:,1:] = np.array(colonne_list[1:])

data_array[0,0] = 'Pokemon'
data_array[0,1] = 'Coordonnees en X'
data_array[0,2] = 'Coordonnees en Y'


tableau_travail = data_array[1:,1:].astype(float)
tableau_travail[:,0] = np.ceil(tableau_travail[:,0] * 35)
tableau_travail[:,1] = np.ceil(tableau_travail[:,1] * 35)
tableau_travail = tableau_travail.astype(int)


'''
J'ai importé le tableau des stats, il est utilisable tel quel, mais je me garde la
possibilité de le modifier + tard si nécessaire
'''

with open('../data\pokemon_first_gen.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
data_stats_array = np.array(data)
data_stats_array[data_stats_array == ''] = None  #Affecte le type 2 None quand il n'y en a pas

liste_stats = [] # np.zeros((data_stats_array.shape[0],2))
for i in range(data_stats_array.shape[0]):
    stats = ()
    # for j in range(6):
        # stats.append(float(data_stats_array[i,5+j]))
    stats = data_stats_array[:,5:11].tolist()
    liste_stats.append([str(data_stats_array[i,1]), str(data_stats_array[i,2]), str(data_stats_array[i,3]), tuple(stats[i]), str(data_stats_array[i,-1])])
    liste_stats_array = np.array( liste_stats , dtype = object )
liste_stats_array[-1,-1] = 'True'


#On utilise un dictionnaire pour associer le nom des pokemons à leur numéro, cela permet de coder avec les noms
Nom_Indices_Pokemon = {'Bulbasaur' : 1, 'Ivysaur' : 2, 'Venusaur' : 3, 'Charmander' : 4, 'Charmeleon' : 5, 'Charizard' : 6,
                       'Squirtle' : 7, 'Wartortle' : 8, 'Blastoise' : 9, 'Caterpie' : 10, 'Metapod' : 11, 'Butterfree' : 12,
                       'Weedle' : 13, 'Kakuna' : 14, 'Beedrill' : 15, 'Pidgey' : 16, 'Pidgeotto' : 17, 'Pidgeot' : 18,
                       'Rattata' : 19, 'Raticate' : 20, 'Spearow' : 21, 'Fearow' : 22, 'Ekans' : 23, 'Arbok' : 24,
                       'Pikachu' : 25, 'Raichu' : 26, 'Sandshrew' : 27, 'Sandslash' : 28, 'Nidoranâ™€' : 29, 'Nidorina' : 30,
                       'Nidoqueen' : 31, 'Nidoranâ™‚' : 32, 'Nidorino' : 33, 'Nidoking' : 34, 'Clefairy' : 35, 'Clefable' : 36,
                       'Vulpix' : 37, 'Ninetales' : 38, 'Jigglypuff' : 39, 'Wigglytuff' : 40, 'Zubat' : 41, 'Golbat' : 42,
                       'Oddish' : 43, 'Gloom' : 44, 'Vileplume' : 45, 'Paras' : 46, 'Parasect' : 47, 'Venonat' : 48,
                       'Venomoth' : 49, 'Diglett' : 50, 'Dugtrio' : 51, 'Meowth' : 52, 'Persian' : 53, 'Psyduck' : 54,
                       'Golduck' : 55, 'Mankey' : 56, 'Primeape' : 57, 'Growlithe' : 58, 'Arcanine' : 59, 'Poliwag' : 60,
                       'Poliwhirl' : 61, 'Poliwrath' : 62, 'Abra' : 63, 'Kadabra' : 64, 'Alakazam' : 65, 'Machop' : 66,
                       'Machoke' : 67, 'Machamp' : 68, 'Bellsprout' : 69, 'Weepinbell' : 70, 'Victreebel' : 71, 'Tentacool' :  72,
                       'Tentacruel' : 73, 'Geodude' : 74, 'Graveler' : 75, 'Golem' : 76, 'Ponyta' : 77, 'Rapidash' : 78,
                       'Slowpoke' : 79, 'Slowbro' : 80, 'Magnemite' : 81, 'Magneton' : 82, "Farfetch'd" : 83, 'Doduo' : 84,
                       'Dodrio' : 85, 'Seel' : 86, 'Dewgong' : 87, 'Grimer' : 88, 'Muk' : 89, 'Shellder' : 90,
                       'Cloyster' : 91, 'Gastly' : 92, 'Haunter' : 93, 'Gengar' : 94, 'Onix' : 95, 'Drowzee' : 96,
                       'Hypno' : 97, 'Krabby' : 98, 'Kingler' : 99, 'Voltorb' : 100, 'Electrode' : 101, 'Exeggcute' : 102,
                       'Exeggutor' : 103, 'Cubone' : 104, 'Marowak' : 105, 'Hitmonlee' : 106, 'Hitmonchan' : 107, 'Lickitung' : 108,
                       'Koffing' : 109, 'Weezing' : 110, 'Rhyhorn' : 111, 'Rhydon' : 112, 'Chansey' : 113, 'Tangela' : 114,
                       'Kangaskhan' : 115, 'Horsea' : 116, 'Seadra' : 117, 'Goldeen' : 118, 'Seaking' : 119, 'Staryu' : 120,
                       'Starmie' : 121, 'Mr. Mime' : 122, 'Scyther' : 123, 'Jynx' : 124, 'Electabuzz' : 125, 'Magmar' : 126,
                       'Pinsir' : 127, 'Tauros' : 128, 'Magikarp' : 129, 'Gyarados' : 130, 'Lapras' : 131, 'Ditto' : 132,
                       'Eevee' : 133, 'Vaporeon' : 134, 'Jolteon' : 135, 'Flareon' : 136, 'Porygon' : 137, 'Omanyte' : 138,
                       'Omastar' : 139, 'Kabuto' : 140, 'Kabutops' : 141, 'Aerodactyl' : 142, 'Snorlax' : 143, 'Articuno' : 144,
                       'Zapdos' : 145, 'Moltres' : 146, 'Dratini' : 147, 'Dragonair' : 148, 'Dragonite' : 149, 'Mewtwo' : 150,
                       'Mew' : 151}
legendary = []

for i in range(1,len(data_array)) :
    if liste_stats_array[Nom_Indices_Pokemon[data_array[i, 0]], -1] == 'True' :
        legendary += [[liste_stats_array[Nom_Indices_Pokemon[data_array[i,0]],0],tableau_travail[i-1,0], tableau_travail[i-1,1]]]
legendary = np.array(legendary, dtype = object)

def creaMap() :
    # Creation de la map
    taille_map = int(np.max(tableau_travail)) + 1

    # 0 : Bloc de deplacement libre (herbe)
    # Nom de bloc 'dur' : bloc sans déplacement
    # Nom de pokemon : hautes herbes où spawn le pokémon
    map = np.zeros([taille_map, taille_map]).astype(str)

    for i in range(len(tableau_travail)):

        # Génération de hautes herbes aléatoires pour les pokémons non légendaires
        if liste_stats_array[Nom_Indices_Pokemon[data_array[i + 1, 0]], -1] == 'False' :
            for j in range(8):
                if tableau_travail[i, 0] + j < taille_map:
                    for k in range(8):
                        if tableau_travail[i, 1] + k < taille_map:
                            if rd.random() < 0.5:

                                map[tableau_travail[i, 0] + j, tableau_travail[i, 1] + k] = data_array[i + 1, 0]
        if liste_stats_array[Nom_Indices_Pokemon[data_array[i + 1, 0]], -1] == 'False':
            map[tableau_travail[i, 0], tableau_travail[i, 1]] = data_array[i + 1, 0]

    for i in legendary :
        map[i[1],i[2]] = i[0]


    #Génération de blocs durs
    for i in range(taille_map):
        for j in range(taille_map - 1):
            if rd.random() < 0.08 and map[i,j + 1] == '0.0':
                map[i,j] = 'Tree'



    return map



Taux_rencontre = {'Common' : 0.87, 'Uncommon' : 1/8, 'Rare' : 1/600, 'Very Rare' : 1/600, 'Extremely Rare' : 1/5000, 'Legendary' : 1, 'Special' : 1/4000, 'Starter' : 1/10000}

'''
Pour les taux de rareté : https://pokemon-planet.fandom.com/wiki/Encounter_Rate
Pour les raretés : https://pokemon-planet.fandom.com/wiki/Pokedex
J'ai adapté certaines raretés : je suis souvent parti de la rareté du pokémon initial, puis j'ai augmenté d'un stade la rareté par évolution.
Pour les Pokémons initiaux, j'ai conservé presque toutes les raretés du site, sauf pour certains "Very Rare" que j'ai redescendu en "Rare".
Globalement, j'ai essayé de prendre en compte les raretés des Pokémons, mais aussi le fait que dans les vrais jeux, les Pokémons sont répartis par zones tandis qu'ici
ils apparaissent partout (nous n'avons pas le temps de définir des zones)
'''

Rarete_Pokemon = {'Bulbasaur' : Taux_rencontre['Starter'], 'Ivysaur' : Taux_rencontre['Starter'], 'Venusaur' : Taux_rencontre['Starter'], 'Charmander' : Taux_rencontre['Starter'], 'Charmeleon' : Taux_rencontre['Starter'], 'Charizard' : Taux_rencontre['Starter'],
                  'Squirtle' : Taux_rencontre['Starter'], 'Wartortle' : Taux_rencontre['Starter'], 'Blastoise' : Taux_rencontre['Starter'], 'Caterpie' : Taux_rencontre['Common'], 'Metapod' : Taux_rencontre['Uncommon'], 'butterfree' : Taux_rencontre['Rare'],
                  'Weedle' : Taux_rencontre['Common'], 'Kakuna' : Taux_rencontre['Uncommon'], 'Beedrill' : Taux_rencontre['Rare'], 'Pidgey' : Taux_rencontre['Common'], 'Pidgeotto' : Taux_rencontre['Uncommon'], 'Pidgeot' : Taux_rencontre['Rare'],
                  'Rattata' : Taux_rencontre['Common'], 'Raticate' : Taux_rencontre['Uncommon'], 'Spearow' : Taux_rencontre['Common'], 'Fearow' : Taux_rencontre['Uncommon'], 'Ekans' : Taux_rencontre['Common'], 'Arbok' : Taux_rencontre['Rare'],
                  'Pikachu' : Taux_rencontre['Very Rare'], 'Raichu' : Taux_rencontre['Extremely Rare'], 'Sandshrew' : Taux_rencontre['Common'], 'Sandslash' : Taux_rencontre['Uncommon'], 'Nidoranâ™€' : Taux_rencontre['Common'], 'Nidorina' : Taux_rencontre['Uncommon'],
                  'Nidoqueen' : Taux_rencontre['Rare'], 'Nidoranâ™‚' : Taux_rencontre['Common'], 'Nidorino' : Taux_rencontre['Uncommon'], 'Nidoking' : Taux_rencontre['Rare'], 'Clefairy' : Taux_rencontre['Rare'], 'Clefable' : Taux_rencontre['Very Rare'],
                  'Vulpix' : Taux_rencontre['Very Rare'], 'Ninetales' : Taux_rencontre['Extremely Rare'], 'Jigglypuff' : Taux_rencontre['Very Rare'], 'Wigglytuff' : Taux_rencontre['Extremely Rare'], 'Zubat' : Taux_rencontre['Common'], 'Golbat' : Taux_rencontre['Uncommon'],
                  'Oddish' : Taux_rencontre['Common'], 'Gloom' : Taux_rencontre['Uncommon'], 'Vileplume' : Taux_rencontre['Rare'], 'Paras' : Taux_rencontre['Common'], 'Parasect' : Taux_rencontre['Uncommon'], 'Venonat' : Taux_rencontre['Rare'],
                  'Venomoth' : Taux_rencontre['Very Rare'], 'Diglett' : Taux_rencontre['Common'], 'Dugtrio' : Taux_rencontre['Uncommon'], 'Meowth' : Taux_rencontre['Uncommon'], 'Persian' : Taux_rencontre['Rare'], 'Psyduck' : Taux_rencontre['Very Rare'],
                  'Golduck' : Taux_rencontre['Extremely Rare'], 'Mankey' : Taux_rencontre['Rare'], 'Primeape' : Taux_rencontre['Very Rare'], 'Growlithe' : Taux_rencontre['Very Rare'], 'Arcanine' : Taux_rencontre['Extremely Rare'], 'Poliwag' : Taux_rencontre['Uncommon'],
                  'Poliwhirl' : Taux_rencontre['Rare'], 'Poliwrath' : Taux_rencontre['Very Rare'], 'Abra' : Taux_rencontre['Rare'], 'Kadabra' : Taux_rencontre['Very Rare'], 'Alakazam' : Taux_rencontre['Extremely Rare'], 'Machop' : Taux_rencontre['Uncommon'],
                  'Machoke' : Taux_rencontre['Rare'], 'Machamp' : Taux_rencontre['Extremely Rare'], 'Bellsprout' : Taux_rencontre['Common'], 'Weepinbell' : Taux_rencontre['Uncommon'], 'Victreebel' : Taux_rencontre['Rare'], 'Tentacool' :  Taux_rencontre['Common'],
                  'Tentacruel' : Taux_rencontre['Uncommon'], 'Geodude' : Taux_rencontre['Common'], 'Graveler' : Taux_rencontre['Uncommon'], 'Golem' : Taux_rencontre['Rare'], 'Ponyta' : Taux_rencontre['Very Rare'], 'Rapidash' : Taux_rencontre['Extremely Rare'],
                  'Slowpoke' : Taux_rencontre['Very Rare'], 'Slowbro' : Taux_rencontre['Extremely Rare'], 'Magnemite' : Taux_rencontre['Rare'], 'Magneton' : Taux_rencontre['Very Rare'], "Farfetch'd" : Taux_rencontre['Extremely Rare'], 'Doduo' : Taux_rencontre['Rare'],
                  'Dodrio' : Taux_rencontre['Very Rare'], 'Seel' : Taux_rencontre['Rare'], 'Dewdong' : Taux_rencontre['Very Rare'], 'Grimer' : Taux_rencontre['Rare'], 'Muk' : Taux_rencontre['Very Rare'], 'Shellder' : Taux_rencontre['Rare'],
                  'Cloyster' : Taux_rencontre['Very Rare'], 'Gastly' : Taux_rencontre['Common'], 'Haunter' : Taux_rencontre['Uncommon'], 'Gengar' : Taux_rencontre['Very Rare'], 'Onix' : Taux_rencontre['Extremely Rare'], 'Drowzee' : Taux_rencontre['Rare'],
                  'Hypno' : Taux_rencontre['Very Rare'], 'Krabby' : Taux_rencontre['Uncommon'], 'Kingler' : Taux_rencontre['Rare'], 'Voltorb' : Taux_rencontre['Common'], 'Electrode' : Taux_rencontre['Common'], 'Exeggcute' : Taux_rencontre['Very Rare'],
                  'Exeggutor' : Taux_rencontre['Extremely Rare'], 'Cubone' : Taux_rencontre['Very Rare'], 'Marowak' : Taux_rencontre['Extremely Rare'], 'Hitmonlee' : Taux_rencontre['Special'], 'Hitmonchan' : Taux_rencontre['Special'], 'Lickitung' : Taux_rencontre['Special'],
                  'Koffing' : Taux_rencontre['Rare'], 'Weezing' : Taux_rencontre['Very Rare'], 'Rhyhorn' : Taux_rencontre['Extremely Rare'], 'Rhydon' : Taux_rencontre['Extremely Rare'], 'Chansey' : Taux_rencontre['Very Rare'], 'Tangela' : Taux_rencontre['Very Rare'],
                  'Kangaskhan' : Taux_rencontre['Extremely Rare'], 'Horsea' : Taux_rencontre['Rare'], 'Seadra' : Taux_rencontre['Very Rare'], 'Goldeen' : Taux_rencontre['Uncommon'], 'Seaking' : Taux_rencontre['Rare'], 'Staryu' : Taux_rencontre['Very Rare'],
                  'Starmie' : Taux_rencontre['Extremely Rare'], 'Mr. Mime' : Taux_rencontre['Special'], 'Scyther' : Taux_rencontre['Extremely Rare'], 'Jynx' : Taux_rencontre['Special'], 'Electabuzz' : Taux_rencontre['Extremely Rare'], 'Magmar' : Taux_rencontre['Very Rare'],
                  'Pinsir' : Taux_rencontre['Extremely Rare'], 'Tauros' : Taux_rencontre['Very Rare'], 'Magikarp' : Taux_rencontre['Common'], 'Gyarados' : Taux_rencontre['Very Rare'], 'Lapras' : Taux_rencontre['Special'], 'Ditto' : Taux_rencontre['Very Rare'],
                  'Eevee' : Taux_rencontre['Special'], 'Vaporeon' : Taux_rencontre['Special'], 'Jolteon' : Taux_rencontre['Special'], 'Flareon' : Taux_rencontre['Special'], 'Porygon' : Taux_rencontre['Special'], 'Omanyte' : Taux_rencontre['Special'],
                  'Omastar' : Taux_rencontre['Special'], 'Kabuto' : Taux_rencontre['Special'], 'Kabutops' : Taux_rencontre['Special'], 'Aerodactyl' : Taux_rencontre['Special'], 'Snorlax' : Taux_rencontre['Extremely Rare'], 'Articuno' : Taux_rencontre['Legendary'],
                  'Zapdos' : Taux_rencontre['Legendary'], 'Moltres' : Taux_rencontre['Legendary'], 'Dratini' : Taux_rencontre['Extremely Rare'], 'Dragonair' : Taux_rencontre['Extremely Rare'], 'Dragonite' : Taux_rencontre['Extremely Rare'], 'Mewtwo' : Taux_rencontre['Legendary'],
                  'Mew' : Taux_rencontre['Legendary']}



#On a implémenté la capture de pokemons, et donc les taux de capture officiels des différents pokemons
Taux_Capture_Pokemon = {'Bulbasaur' : 45, 'Ivysaur' : 45, 'Venusaur' : 45, 'Charmander' : 45, 'Charmeleon' : 45, 'Charizard' : 45,
                       'Squirtle' : 45, 'Wartortle' : 45, 'Blastoise' : 45, 'Caterpie' : 255, 'Metapod' : 120, 'butterfree' : 45,
                       'Weedle' : 255, 'Kakuna' : 120, 'Beedrill' : 45, 'Pidgey' : 255, 'Pidgeotto' : 120, 'Pidgeot' : 45,
                       'Rattata' : 255, 'Raticate' : 127, 'Spearow' : 255, 'Fearow' : 90, 'Ekans' : 255, 'Arbok' : 90,
                       'Pikachu' : 190, 'Raichu' : 75, 'Sandshrew' : 255, 'Sandslash' : 90, 'Nidoranâ™€' : 235, 'Nidorina' : 120,
                       'Nidoqueen' : 45, 'Nidoranâ™,' : 255, 'Nidorino' : 120, 'Nidoking' : 45, 'Clefairy' : 150, 'Clefable' : 25,
                       'Vulpix' : 190, 'Ninetales' : 75, 'Jigglypuff' : 170, 'Wigglytuff' : 50, 'Zubat' : 255, 'Golbat' : 90,
                       'Oddish' : 255, 'Gloom' : 120, 'Vileplume' : 45, 'Paras' : 190, 'Parasect' : 75, 'Venonat' : 190,
                       'Venomoth' : 75, 'Diglett' : 255, 'Dugtrio' : 50, 'Meowth' : 255, 'Persian' : 90, 'Psyduck' : 190,
                       'Golduck' : 75, 'Mankey' : 190, 'Primeape' : 75, 'Growlithe' : 190, 'Arcanine' : 75, 'Poliwag' : 255,
                       'Poliwhirl' : 120, 'Poliwrath' : 45, 'Abra' : 200, 'Kadabra' : 100, 'Alakazam' : 50, 'Machop' : 180,
                       'Machoke' : 90, 'Machamp' : 45, 'Bellsprout' : 255, 'Weepinbell' : 120, 'Victreebel' : 45, 'Tentacool' :  190,
                       'Tentacruel' : 60, 'Geodude' : 255, 'Graveler' : 120, 'Golem' : 45, 'Ponyta' : 190, 'Rapidash' : 60,
                       'Slowpoke' : 190, 'Slowbro' : 75, 'Magnemite' : 190, 'Magneton' : 60, "Farfetch'd" : 45, 'Doduo' : 190,
                       'Dodrio' : 45, 'Seel' : 190, 'Dewdong' : 75, 'Grimer' : 190, 'Muk' : 75, 'Shellder' : 190,
                       'Cloyster' : 60, 'Gastly' : 190, 'Haunter' : 90, 'Gengar' : 45, 'Onix' : 45, 'Drowzee' : 190,
                       'Hypno' : 75, 'Krabby' : 225, 'Kingler' : 60, 'Voltorb' : 190, 'Electrode' : 60, 'Exeggcute' : 90,
                       'Exeggutor' : 45, 'Cubone' : 190, 'Marowak' : 75, 'Hitmonlee' : 45, 'Hitmonchan' : 45, 'Lickitung' : 45,
                       'Koffing' : 190, 'Weezing' : 60, 'Rhyhorn' : 120, 'Rhydon' : 60, 'Chansey' : 30, 'Tangela' : 45,
                       'Kangaskhan' : 45, 'Horsea' : 225, 'Seadra' : 75, 'Goldeen' : 225, 'Seaking' : 60, 'Staryu' : 225,
                       'Starmie' : 60, 'Mr. Mime' : 45, 'Scyther' : 45, 'Jynx' : 45, 'Electabuzz' : 45, 'Magmar' : 45,
                       'Pinsir' : 45, 'Tauros' : 45, 'Magikarp' : 255, 'Gyarados' : 45, 'Lapras' : 45, 'Ditto' : 35,
                       'Eevee' : 45, 'Vaporeon' : 45, 'Jolteon' : 45, 'Flareon' : 45, 'Porygon' : 45, 'Omanyte' : 45,
                       'Omastar' : 45, 'Kabuto' : 45, 'Kabutops' : 45, 'Aerodactyl' : 45, 'Snorlax' : 25, 'Articuno' : 3,
                       'Zapdos' : 3, 'Moltres' : 3, 'Dratini' : 45, 'Dragonair' : 45, 'Dragonite' : 45, 'Mewtwo' : 3,
                       'Mew' : 45}


mapToSprite = {'0' : 'ressources/map/ground_grass.png',
               '0.1': 'ressources/map/ground_other.png',
               'Tree' : 'ressources/map/tree2.png',
               'Tall_grass':'ressources/map/tall_grass_ground_64.png',
               'Homme_face' : 'ressources/map/Perso_masc_face.png',
               'Water' : 'ressources/map/water1.png',
               'Mew' : 'ressources/map/mew.png',
               'Mewtwo' : 'ressources/map/mewtwo.png',
               'Moltres' : 'ressources/map/moltres.png',
               'Articuno' : 'ressources/map/Articuno.png',
               'Zapdos' : 'ressources/map/zapdos.png'
               }



if __name__ == '__main__':
    pass
    #Travail sur le tableau pokemon_coordinates
    # plt.close()
    # plt.figure('Affichage pkmn')
    # plt.plot(tableau_travail[:,0].astype(float),tableau_travail[:,1].astype(float), '+')
    # plt.title('Répartition Pokemon')
    # plt.show()
#
#    plt.figure('Affichage pkmn * 35')
#    plt.plot(tableau_travail[:,0],tableau_travail[:,1], '+')
#    plt.title('Répartition Pokemon * 35')