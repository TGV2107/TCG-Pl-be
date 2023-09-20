#importation des utilitaires:

import pygame

#importation des classes:

from Class.Button import *

def affichage_main(screen):

    # bouton goToColleciton

    goToCollection = Button("test",pygame.font.SysFont("Comic Sans MS", 10, bold=True),(255,255,255),(100,50),(300,300),pygame.image.load("Assets/img/bouton_collection.png"))
    goToCollection.Blit(screen)

    #return
    return goToCollection.rect