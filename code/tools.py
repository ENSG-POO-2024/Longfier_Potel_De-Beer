# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:57:19 2024

@author: gpotel
"""

import numpy as np
import csv
import ast
import matplotlib.pyplot as plt

#np.loadtxt('D:\Downloads\pokemon_coordinates.csv', skiprows = 1)

with open('D:\Downloads\pokemon_coordinates.csv', 'r') as f:
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
tableau_travail[:,0] = np.ceil(tableau_travail[:,0] * 1000)
tableau_travail[:,1] = np.ceil(tableau_travail[:,1] * 1000)


with open('D:\Downloads\pokemon_first_gen.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
data_stats_array = np.array(data)









if __name__ == '__main__':
    pass
#    #Travail sur le tableau pokemon_coordinates
#    plt.figure('Affichage pkmn')
#    plt.plot(data_array[1:,1].astype(float),data_array[1:,2].astype(float), '+')
#    plt.title('Répartition Pokemon')
#    
#    plt.figure('Affichage pkmn * 1000')
#    plt.plot(tableau_travail[:,0],tableau_travail[:,1], '+')
#    plt.title('Répartition Pokemon * 1000')