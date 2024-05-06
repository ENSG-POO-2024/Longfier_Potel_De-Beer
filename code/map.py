import joueur
import tools
from combat_gab import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QPixmap,QIcon




class Carte(QWidget) :
    def __init__(self):
        super().__init__()




        #Création de la fenêtre principale
        self.setGeometry(300, 100, 900, 900)
        self.setWindowTitle('Pokemon mais en plus gèze')

        #Changement de l'icone de l'app
        self.icone = QIcon('ressources/pokeball_icone.png')
        self.setWindowIcon(self.icone)

        #Initialisation du fond
        self.state = 'start_screen'
        self.background = QPixmap('ressources/Background.png').scaledToHeight(self.height())


        self.startScreen()


    def paintEvent(self, event):
        if self.state == 'start_screen' :
            painter = QPainter(self)
            painter.drawPixmap(-275, 0, self.background)

        else :
            self.paintMap()


    def startScreen(self):

        #Initialisation du bouton
        self.start_button = QPushButton(text = 'Start game', parent = self)
        self.start_button.setGeometry(350,530,200,100)
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
        equipe = [Pokemon('Bulbasaur'),Pokemon('Charmander'),Pokemon('Squirtle')]
        player = joueur.Joueur(500,equipe)




    def paintMap(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Carte()
    widget.show()
    sys.exit(app.exec_())