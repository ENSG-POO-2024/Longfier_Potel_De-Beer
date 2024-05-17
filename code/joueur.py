from math import sqrt
import numpy as np
from tools import *

dict_types = {'Steel' : 0, 'Fighting' : 1, 'Dragon' : 2, 'Water' : 3, 'Electric' : 4, 'Fire' : 5, 'Fairy' : 6, 'Ice' : 7, 'Bug' : 8, 
             'Normal' : 9, 'Grass' : 10, 'Poison' : 11, 'Psychic' : 12, 'Rock' : 13, 'Ground' : 14, 'Ghost' : 15, 'Dark' : 16, 
             'Flying' : 17}

table_affin = np.array(([0.5, 1, 1, 0.5, 0.5, 0.5, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
                       [2, 1, 1, 1, 1, 1, 0.5, 2, 0.5, 2, 1, 0.5, 0.5, 2, 1, 0, 2, 0.5],
                       [0.5, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 2, 2, 1, 1, 1],
                       [1, 1, 0.5, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 0, 1, 1, 2],
                       [2, 1, 0.5, 0.5, 1, 0.5, 1, 2, 2, 1, 2, 1, 1, 0.5, 1, 1, 1, 1],
                       [0.5, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 2, 1],
                       [0.5, 1, 2, 0.5, 1, 0.5, 1, 0.5, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2],
                       [0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 2, 0.5, 2, 1, 1, 0.5, 2, 0.5],
                       [0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 0, 1, 1],
                       [0.5, 1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 1, 0.5, 0.5, 1, 2, 2, 1, 1, 0.5],
                       [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 0.5, 0.5, 1, 1],
                       [0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0, 1],
                       [0.5, 0.5, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 0.5, 1, 1, 2],
                       [2, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 2, 0.5, 1],
                       [1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 2, 0.5, 1],
                       [0.5, 2, 1, 1, 0.5, 1, 1, 1, 2, 1, 2, 1, 1, 0.5, 1, 1, 1, 1]))

def dist(p1, p2):
    """
    Calcul de la distance euclidienne
    """
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
class PokemonSauvage:
    #Nous n'utilisons pas cette classe au final
    def __init__(self, coord, typ, nb_vies, déf, att, sauv):
        self.coord = coord
        self.typ = typ #liste des types
        self.nb_vies = nb_vies
        self.déf = déf
        self.att = att
        self.sauv = sauv
        self.cache = True
    
    def decouv_pok(self, joueur, d_decouv):
        self.cache = (dist(self.coord, joueur.coord) >= d_decouv)
        

class Joueur:
    def __init__(self, coord, equipe, map):
        self.coord = coord
        self.equipe = equipe
        self.map = map
        self.pc = []
        
    def depl(self, direct):
        """
        Gestion du déplacement du joueur

        """
        new_coord = self.coord + direct
        if self.map[new_coord[0],new_coord[1] - 1] != 'Tree':
            self.coord[0] += direct[0]
            self.coord[1] += direct[1]
        
    def change_equipe(self,equipe):
        self.equipe = equipe

    def changement_equipe_pc(self):
        """
        Gestion de l'envoi ou de la récupération d'un pokemon dans le PC
        (On n'a pas eu le temps de l'implémenter au final)

        """
        pass

if __name__ == '__main__' :
    pass