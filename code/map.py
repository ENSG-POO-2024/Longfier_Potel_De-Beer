import joueur
from tools import *
from combat_gab import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random as rd
import numpy as np



class Carte(QWidget):
    def __init__(self):
        super().__init__()

        self.coord = [rd.randint(1000,3000), rd.randint(1000,3000)]
        self.coord = tableau_travail[1]
        self.cam_size = 14
        self.pixel_number = 64
        self.taille_map = int(np.max(tableau_travail)) + 1


        #Création de la fenêtre principale
        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('Pokemon mais en plus gèze')

        #Changement de l'icone de l'app
        self.icone = QIcon('ressources/pokeball_icone.png')
        self.setWindowIcon(self.icone)

        #Initialisation du fond
        self.state = 'start_screen'
        self.background = QPixmap('ressources/Background.png').scaledToHeight(self.height())

        '''
        # Initialisation du layout
        self.temp = QHBoxLayout()
        self.label_temp = QLabel('oui')
        self.temp.addWidget(self.label_temp)


        self.layout_verti = QVBoxLayout(self)
        self.layout_verti.addLayout(self.temp)

        print(self.layout_verti.itemAt(0))
        '''
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

                    print(self.global_map[x_cam, y_cam])
                    if self.global_map[x_cam, y_cam] == 'Tree' and self.global_map[x_cam, y_cam - 1] == '0.0':
                        painter.drawPixmap(x_draw, y_draw, QPixmap(mapToSprite['Tree']))



                    elif self.global_map[x_cam, y_cam] in Nom_Indices_Pokemon.keys() :
                        print('POKEMON')
                        painter.drawPixmap(x_draw, y_draw, QPixmap(mapToSprite['Tall_grass']))






    def startScreen(self):

        #Initialisation du bouton
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
        player = joueur.Joueur([self.coord], equipe)
        self.start_button.hide()
        self.global_map = creaMap()
        self.state = 'game_screen'
        self.update()





if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = Carte()
    widget.show()
    sys.exit(app.exec_())


'''
# Effacez le contenu précédent du layout_verti uniquement si nécessaire
            if self.layout_verti.count() > 0:
                for i in reversed(range(self.layout_verti.count())):
                    layout_to_remove = self.layout_verti.itemAt(i)
                    for j in reversed(range(layout_to_remove.count())):
                        widget = layout_to_remove.itemAt(j).widget()
                        layout_to_remove.removeWidget(widget)
                        widget.setParent(None)
                    self.layout_verti.removeItem(layout_to_remove)

            for i in range(x_min, x_max):
                layout_horiz = QHBoxLayout()
                for j in range(y_min, y_max):
                    pixmap = self.dessinPixmap(self.global_map[i, j])
                    if pixmap:
                        label = QLabel()
                        label.setPixmap(pixmap)
                        layout_horiz.addWidget(label)
                self.layout_verti.addLayout(layout_horiz)

        def dessinPixmap(self,valeur):

            if valeur == '0.0' :
                print('pixmap')
                pixmap = QPixmap(64,64)
                pixmap.fill(QColor(166,247,64))
                texture = QPixmap( mapToSprite['0'])
                painter = QPainter(pixmap)
                painter.drawPixmap(0,0,texture)
                painter.end()

                return pixmap
                
            else :
                return None
'''