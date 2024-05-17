import joueur
from tools import *
from combat_gab import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random as rd
import numpy as np
import echap_window
import combat_window
import time



class Main_window(QWidget):
    def __init__(self):
        super().__init__()


        self.cam_size = 14
        self.pixel_number = 64
        self.taille_map = int(np.max(tableau_travail)) + 1
        self.coord = [rd.randint(int(self.taille_map/3),int(self.taille_map*2/3)), rd.randint(int(self.taille_map/3),int(self.taille_map*2/3))]
        self.coord = tableau_travail[898]



        #Création de la fenêtre principale
        self.setGeometry(300, 100, 900, 900)
        self.setObjectName('Pokemon mais en plus gèze')

        self.game_over = QLabel(self)
        self.game_over.setGeometry(300, 400, 300, 100)
        self.game_over.setText("Game Over")
        self.game_over.setObjectName("game_over")
        self.setStyleSheet("""
            QLabel#game_over{
                font-size: 50px;
                font-weight: bold;
            }
            """)
        self.game_over.hide()


        #Changement de l'icone de l'app
        self.icon = QIcon('ressources/pokeball_icone.png')
        self.setWindowIcon(self.icon)

        #Initialisation du fond
        self.state = 'start_screen'
        self.time = 'flow'
        self.background = QPixmap('ressources/Background.png').scaledToHeight(self.height())

        # Creation de fenêtres annexes
        self.Ui_combat_window = QMainWindow()
        self.Ui_combat = combat_window.Ui_combat_window()
        self.Ui_combat.setupUi(self.Ui_combat_window)

        self.Ui_combat.run_button.clicked.connect(self.close_combat)


        self.Ui_echap_window = QMainWindow()
        self.Ui_echap = echap_window.Ui_echap_window()
        self.Ui_echap.setupUi(self.Ui_echap_window)

        self.Ui_echap.resume_button.clicked.connect(self.close_echap)
        self.Ui_echap.quit_button.clicked.connect(QApplication.quit)

        #Initialisation de certaines données pour eviter les erreurs
        self.player = joueur.Joueur(self.coord, [],None)
        self.global_map = []
        self.combat = None



        #Démarrage
        self.startScreen()

    def paintEvent(self, event):
        if self.state == 'start_screen':

            painter = QPainter(self)
            painter.drawPixmap(-275, 0, self.background)

        else:
            #Caméra bord droite / bas
            x_min_cam = min(self.coord[0] - self.cam_size // 2, self.taille_map - self.cam_size )
            y_min_cam = min(self.coord[1] - self.cam_size // 2, self.taille_map - self.cam_size )

            #Caméra bord gauche / haut
            x_min_cam = max(x_min_cam, 0)
            y_min_cam = max(y_min_cam, 0)

            #Initialisation des indice pour le dessin
            x_min_draw = (self.width() - self.cam_size * self.pixel_number) // 2
            y_min_draw = (self.height() - self.cam_size * self.pixel_number) // 2

            #Initialisation du dessin
            painter = QPainter(self)
            painter.setPen(QColor(0, 0, 0))

            #Début du dessin
            for i in range (self.cam_size):
                for j in range(self.cam_size):
                    #Création des indices
                    x_draw = x_min_draw + i * self.pixel_number
                    y_draw = y_min_draw + j * self.pixel_number

                    #Affichage de l'herbe (sol par défaut)
                    painter.drawPixmap(x_draw, y_draw, QPixmap(mapToSprite['0']))





            #Superposition des autres éléments
            for i in range(self.cam_size):
                for j in range(self.cam_size):
                    # Création des indices
                    x_draw = x_min_draw + i * self.pixel_number
                    y_draw = y_min_draw + j * self.pixel_number

                    #Coordonnées sur la carte
                    x_cam = x_min_cam + i
                    y_cam = y_min_cam + j



                    if x_min_draw + (self.cam_size//2) * self.pixel_number == x_draw and y_min_draw + (self.cam_size//2) * self.pixel_number == y_draw :
                        painter.drawPixmap(x_min_draw + (self.cam_size // 2) * self.pixel_number,
                                           y_min_draw + (self.cam_size // 2) * self.pixel_number - 34,
                                           QPixmap(mapToSprite['Homme_face']))
                        print(self.global_map[x_cam,y_cam])
                    bloc = self.global_map[x_cam, y_cam]

                    if bloc in Nom_Indices_Pokemon.keys():
                        if liste_stats_array[Nom_Indices_Pokemon[bloc],-1] == 'False':
                            painter.drawPixmap(x_draw, y_draw + 11, QPixmap(mapToSprite['Tall_grass']))
                        else:
                            if bloc == 'Mew' :
                                painter.drawPixmap(x_draw + 13,y_draw,QPixmap(mapToSprite[bloc]))
                            elif bloc == 'Moltres' :
                                painter.drawPixmap(x_draw - 40, y_draw - 7, QPixmap(mapToSprite[bloc]))
                            elif bloc == 'Articuno':
                                painter.drawPixmap(x_draw - 27, y_draw, QPixmap(mapToSprite[bloc]))
                            elif bloc == 'Zapdos':
                                painter.drawPixmap(x_draw - 9, y_draw - 20, QPixmap(mapToSprite[bloc]))
                            else :
                                painter.drawPixmap(x_draw + 10, y_draw, QPixmap(mapToSprite[bloc]))


                    if bloc == 'Tree':
                        painter.drawPixmap(x_draw, y_draw, QPixmap(mapToSprite['Tree']))




    def startScreen(self):

        #Initialisation du bouton
        self.state == 'start_screen'
        self.start_button = QPushButton(text='Start game', parent=self)
        self.start_button.setGeometry(350, 530, 200, 100)
        self.start_button.show()
        self.start_button.clicked.connect(self.start_game)
        self.start_button.setStyleSheet(
            "QPushButton {"
            "color: black;"
            "background-color: transparent;"
            "font-size: 24px;"
            "font-weight: bold"
            "}"
        )

    def start_game(self):
        equipe = [Pokemon('Bulbasaur'), Pokemon('Charmander'), Pokemon('Squirtle')]
        self.start_button.hide()
        self.global_map = creaMap()
        self.player.map = self.global_map
        self.player.equipe = equipe
        self.state = 'game_screen'
        self.update()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.open_echap()


        if self.state == 'game_screen' and self.time == 'flow':
            if event.key() == Qt.Key_Q :
                self.player.depl(np.array([-1,0]))
            if event.key() == Qt.Key_D:
                self.player.depl(np.array([1,0]))
            if event.key() == Qt.Key_Z:
                self.player.depl(np.array([0,-1]))
            if event.key() == Qt.Key_S:
                self.player.depl(np.array([0,1]))
            self.coord = self.player.coord
            self.update()
            self.check_poke()


    def check_poke(self):
        bloc = self.global_map[self.coord[0], self.coord[1]]
        if bloc in Nom_Indices_Pokemon.keys():
            if rd.random() < Rarete_Pokemon[bloc] :
                self.open_combat([Pokemon(bloc)])
        pass

    def close_echap(self):
        self.time = 'flow'
        self.Ui_echap_window.hide()


    def open_echap(self):
        self.time = 'paused'
        self.Ui_echap_window.show()

    def open_combat(self,equipe_ennemie):
        self.time = 'pause'
        self.Ui_combat_window.show()
        self.combat = Combat(self.player.equipe,equipe_ennemie)
        print(Type(self.combat))

        self.Ui_combat.poke_switch_1.setText(self.player.equipe[0].nom)
        self.Ui_combat.poke_switch_2.setText(self.player.equipe[1].nom)
        self.Ui_combat.poke_switch_3.setText(self.player.equipe[2].nom)

        #Début avec 3 pokémons
        if len(self.player.equipe) >= 4:
            print(self.player.equipe[3].nom)
            self.Ui_combat.poke_switch_4.setText(self.player.equipe[3].nom)
        if len(self.player.equipe) >= 5:
            self.Ui_combat.poke_switch_5.setText(self.player.equipe[4].nom)
        if len(self.player.equipe) ==6:
            self.Ui_combat.poke_switch_6.setText(self.player.equipe[5].nom)

        self.switch_poke_affichage()

        self.Ui_combat.poke_switch_1.pressed.connect(self.switch_poke_1)
        self.Ui_combat.poke_switch_2.pressed.connect(self.switch_poke_2)
        self.Ui_combat.poke_switch_3.pressed.connect(self.switch_poke_3)
        self.Ui_combat.poke_switch_4.pressed.connect(self.switch_poke_4)
        self.Ui_combat.poke_switch_5.pressed.connect(self.switch_poke_5)
        self.Ui_combat.poke_switch_6.pressed.connect(self.switch_poke_6)

        self.Ui_combat.att_normal_button.pressed.connect(self.attaque_normale)
        self.Ui_combat.att_spe1_button.pressed.connect(self.attaque_spe1)
        self.Ui_combat.att_spe2_button.pressed.connect(self.attaque_spe2)


    def switch_poke_1(self):
        if self.player.equipe[0].pointsdevie > 0 :
            self.combat.changement_pokemon(self.player.equipe[0])
            self.Ui_combat.retour_pressed()

            self.switch_poke_affichage()

    def switch_poke_2(self):
        if self.player.equipe[1].pointsdevie > 0:
            self.combat.changement_pokemon(self.player.equipe[1])
            self.Ui_combat.retour_pressed()

            self.switch_poke_affichage()

    def switch_poke_3(self):
        if self.player.equipe[2].pointsdevie > 0:
            self.combat.changement_pokemon(self.player.equipe[2])
            self.Ui_combat.retour_pressed()

            self.switch_poke_affichage()

    def switch_poke_4(self):
        if len(self.player.equipe) >= 4:
            if self.player.equipe[3].pointsdevie > 0:
                self.combat.changement_pokemon(self.player.equipe[3])
                self.Ui_combat.retour_pressed()

                self.switch_poke_affichage()

    def switch_poke_5(self):
        if len(self.player.equipe) >= 5:
            if self.player.equipe[4].pointsdevie > 0:
                self.combat.changement_pokemon(self.player.equipe[4])
                self.Ui_combat.retour_pressed()

                self.switch_poke_affichage()

    def switch_poke_6(self):
        if len(self.player.equipe) >= 6:
            if self.player.equipe[5].pointsdevie > 0:
                self.combat.changement_pokemon(self.player.equipe[5])
                self.Ui_combat.retour_pressed()

                self.switch_poke_affichage()

    def switch_poke_affichage(self):
        self.Ui_combat.att_spe1_button.setText(self.combat.mainpokemon1.type1.upper())

        if self.combat.mainpokemon1.type2 != 'None':
            self.Ui_combat.att_spe2_button.setText(self.combat.mainpokemon1.type2.upper())
            self.Ui_combat.spe2 = 'True'

        else:
            self.Ui_combat.spe2 = 'False'

        self.pokemon1 = 'ressources/Pokemon_Combat/' + self.combat.mainpokemon1.nom.lower() + "_Dos.png"
        self.pokemon2 = 'ressources/Pokemon_Combat/' + self.combat.mainpokemon2.nom.lower() + '_Face.png'
        self.Ui_combat.pokemon1_label.setStyleSheet(
            "QLabel {"
            "background-image: url(" + self.pokemon1 + ");"
            "background-repeat: no-repeat"
            "}"
        )

        self.Ui_combat.pokemon2_label.setStyleSheet(
            "QLabel {"
            "background-image: url(" + self.pokemon2 + ");"
                                                       "background-repeat: no-repeat"
                                                       "}"
        )



    def attaque_normale(self):
        resultat = self.combat.attaque_alliee('normale')
        if resultat == 'Finito' :
            self.close_combat()
        self.attaque_recue()

    def attaque_spe1(self):
        resultat = self.combat.attaque_alliee('type1')
        if resultat == 'Finito' :
            self.close_combat()
        self.attaque_recue()

    def attaque_spe2(self):
        resultat = self.combat.attaque_alliee('type2')
        if resultat == 'Finito' :
            self.close_combat()
        self.attaque_recue()
    def attaque_recue(self):
        resultat = self.combat.attaque_ennemie()
        if resultat == "perdu" :
            self.close_combat()
            self.game_over.show()
            self.game_over.raise_()
            self.state = 'start_screen'
            self.update()
            self.start_button.show()


        elif resultat == 'poke ko' :
            self.Ui_combat.poke_ko()

    def close_combat(self):
        #Regeneration des pv des pokemons
        for i in self.player.equipe :
            i.pointsdevie = i.pointsdevieTOT
        self.player.equipe = self.combat.equipe1

        self.Ui_combat.retour_pressed()
        self.time = 'flow'
        self.Ui_combat_window.hide()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = Main_window()
    widget.show()
    sys.exit(app.exec_())

