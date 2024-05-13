from math import sqrt
import numpy as np
from tools import *

dict_typs = {'Acier' : 1, 'Combat' : 2, 'Dragon' : 3, 'Eau' : 4, 'Electrik' : 5, 'Feu' : 6, 'Fée' : 7, 'Glace' : 8, 'Insecte' : 9, 
             'Normal' : 10, 'Plante' : 11, 'Poison' : 12, 'Psy' : 13, 'Roche' : 14, 'Sol' : 15, 'Spectre' : 16, 'Ténèbre' : 17, 
             'Vol' : 18}

tabl_affin = np.array(([0.5, 1, 1, 0.5, 0.5, 0.5, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
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
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
class PokemonSauvage:
    
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
        
    def depl(self, direct):
        new_coord = self.coord + direct
        if self.map[new_coord[0],new_coord[1] - 1] != 'Tree':
            self.coord[0] += direct[0]
            self.coord[1] += direct[1]
        
    def change_equipe(self,equipe):
        self.equipe = equipe



if __name__ == '__main__' :
    pass