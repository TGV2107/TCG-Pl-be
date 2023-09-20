#importation des utilitaires:

import pygame

from Class.Button import *

#importation des classes:


def affichage_main(screen):

    rects = []

    # bouton goToColleciton

    goToCollection = Button("test",pygame.font.SysFont("Comic Sans MS", 10, bold=True),(255,255,255),(100,50),(300,300),pygame.image.load("Assets/img/bouton_collection.png"))
    goToCollection.Blit(screen)
    rects.append(("main_goTo_Collection",goToCollection.rect))

    #return
    return rects