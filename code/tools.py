# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:57:19 2024

@author: gpotel
"""

import numpy as np
import csv
import ast
import matplotlib.pyplot as plt

#np.loadtxt('../data/pokemon_coordinates.csv', skiprows = 1)

'''
J'ai isolé les coordonnées en X et en Y pour que ce soit + facile
Dans tableau_travail, les coordonnées sont multipliées par 1000 et arrondies à l'unité
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
tableau_travail[:,0] = np.ceil(tableau_travail[:,0] * 100)
tableau_travail[:,1] = np.ceil(tableau_travail[:,1] * 100)
tableau_travail = tableau_travail.astype(int)


"""
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
    stats =data_stats_array[:,5:11].tolist()
    liste_stats.append([str(data_stats_array[i,1]), str(data_stats_array[i,2]), str(data_stats_array[i,3]), stats[i]])
    liste_stats_array = np.array( liste_stats)

Nom_Indices_Pokemon = {'Bulbasaur' : 1, 'Ivysaur' : 2, 'Venusaur' : 3, 'Charmander' : 4, 'Charmeleon' : 5, 'Charizard' : 6,
                       'Squirtle' : 7, 'Wartortle' : 8, 'Blastoise' : 9, 'Caterpie' : 10, 'Metapod' : 11, 'butterfree' : 12,
                       'Weedle' : 13, 'Kakuna' : 14, 'Beedrill' : 15, 'Pidgey' : 16, 'Pidgeotto' : 17, 'Pidgeot' : 18,
                       'Rattata' : 19, 'Raticate' : 20, 'Spearow' : 21, 'Fearow' : 22, 'Ekans' : 23, 'Arbok' : 24,
                       'Pikachu' : 25, 'Raichu' : 26, 'Sandshrew' : 27, 'Sandslash' : 28, 'Nidoranâ™€' : 29, 'Nidorina' : 30,
                       'Nidoqueen' : 31, 'Nidoranâ™,' : 32, 'Nidorino' : 33, 'Nidoking' : 34, 'Clefairy' : 35, 'Clefable' : 36,
                       'Vulpix' : 37, 'Ninetales' : 38, 'Jigglypuff' : 39, 'Wigglytuff' : 40, 'Zubat' : 41, 'Golbat' : 42,
                       'Oddish' : 43, 'Gloom' : 44, 'Vileplume' : 45, 'Paras' : 46, 'Parasect' : 47, 'Venonat' : 48,
                       'Venomoth' : 49, 'Diglett' : 50, 'Dugtrio' : 51, 'Meowth' : 52, 'Persian' : 53, 'Psyduck' : 54,
                       'Golduck' : 55, 'Mankey' : 56, 'Primeape' : 57, 'Growlithe' : 58, 'Arcanine' : 59, 'Poliwag' : 60,
                       'Poliwhirl' : 61, 'Poliwrath' : 62, 'Abra' : 63, 'Kadabra' : 64, 'Alakazam' : 65, 'Machop' : 66,
                       'Machoke' : 67, 'Machamp' : 68, 'Bellsprout' : 69, 'Weepinbell' : 70, 'Victreebel' : 71, 'Tentacool' :  72,
                       'Tentacruel' : 73, 'Geodude' : 74, 'Graveler' : 75, 'Golem' : 76, 'Ponyta' : 77, 'Rapidash' : 78,
                       'Slowpoke' : 79, 'Slowbro' : 80, 'Magnemite' : 81, 'Magneton' : 82, "Farfetch'd" : 83, 'Doduo' : 84,
                       'Dodrio' : 85, 'Seel' : 86, 'Dewdong' : 87, 'Grimer' : 88, 'Muk' : 89, 'Shellder' : 90,
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




"""

if __name__ == '__main__':
    pass
#    #Travail sur le tableau pokemon_coordinates
    plt.close()
    plt.figure('Affichage pkmn')
    plt.plot(tableau_travail[:,0].astype(float),tableau_travail[:,1].astype(float), '+')
    plt.title('Répartition Pokemon')
    plt.show()
#    
#    plt.figure('Affichage pkmn * 1000')
#    plt.plot(tableau_travail[:,0],tableau_travail[:,1], '+')
#    plt.title('Répartition Pokemon * 1000')