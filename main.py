#importations utilitaires:

import csv
import math
import os
import time

import pygame

from Affichage.a_collection import *
from Affichage.a_main import *
from Class.Button import *
from Class.Card import *
from Class.CardRect import *
from Class.Game import *

#importation des classes:


#importation des affichages:


#récupération des cartes :

with open("Data/Cards.csv") as file:

    r = csv.reader(file)

    Cards = []
    for row in r:
        ID, Name, Type, Cost, Health, Attack, Rarity, Class = row
        ID, Cost, Health, Attack = int(ID), int(Cost), int(Health), int(Attack)
        Cards.append(Card(ID, Name, Type, Cost, Health, Attack, Rarity, Class))

with open("Data/Collection.csv") as file:
    
    r = csv.reader(file)
    
    OwnedCards = []
    for row in r:
        ID, Name, Type, Cost, Health, Attack, Rarity, Class = row
        ID, Cost, Health, Attack = int(ID), int(Cost), int(Health), int(Attack)
        OwnedCards.append(Card(ID, Name, Type, Cost, Health, Attack, Rarity, Class))

#initialisation :

game = Game() #instance du statut du joueur

page_collection = None #Numéro de la page de collection affichée
isLooking = False #Booléen, si regarde une carte dans la collection
looked_card = None #instance de Card() pour la carte regardée
deck_looked = False #Booléen, si deck sélectionné

#création du pygame :

pygame.font.init()
pygame.init()

screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Plèbe War")

running = True

#boucle d'actualisation
while running:
    
    rectList = [] #liste des rects présent sur la page

    pygame.display.flip()
    screen.fill(game.getBackground())
    
    #affichage de chaque page
    
    if game.getScreen() == "main": #affichage de main

        rectList = affichage_main(screen)


    
    elif game.getScreen() == "collection": #affichage de la collection
            
        rectCards, rectList = affichage_collection(screen, OwnedCards, page_collection, isLooking, looked_card)


    #détection des événements
    for event in pygame.event.get():
        
        #événement de fermeture de la page pygame
        if event.type == pygame.QUIT:
            
            running = False
            pygame.quit()
        
        #événement si souris cliquée
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            #recherche de l'élément cliqué
            rectName = None
            for val in rectList:

                name, rect = val

                if rect.collidepoint(event.pos):

                    rectName = name

            #événements des pages

            if game.getScreen() == "main": #événements de la page main
                
                if rectName == "main_goTo_Collection": #bouton go to collection -> envoie vers la page de collection
                
                    game.Screen = "collection"
                    page_collection = 0
            
            elif game.getScreen() == "collection": #événements de la page collection
                    
                if isLooking == False:
                        
                    #Zoom sur une carte :
                    for rectCard in rectCards:
                        
                        rect, card = rectCard
                        
                        if rect.collidepoint(event.pos):
                                
                            looked_card = card
                            looked_rect = rect
                            isLooking = True

                        
                    #Boutons next et previous page -> ajoute ou retire 1 au numéro de la page de la collection
                        
                    if rectName == "collection_buttonNextPage":
                            
                        Npages = ((len(OwnedCards)-1)/10) -1
                            
                        if (len(OwnedCards)-1)%10 == 0:
                                
                            Npages = Npages + 1
                            
                        if page_collection < Npages:
                                
                            page_collection = page_collection + 1
                            
                    elif rectName == "collection_buttonPreviousPage":
                            
                        if page_collection > 0:
                                
                            page_collection = page_collection - 1
                        
                    #Bouton add deck -> permet d'ajouter un deck nommé "Nouveau deck"      NON FONCTIONNEL
                        
                    elif rectName == "collection_buttonAddDeck":
                            
                        print("add deck")
                    
                #Fin du zoom -> si autre chose que la carte zommé est cliqué -> la carte est enlevé
                elif (isLooking == True) and (not rectName == "collection_looked_card"):
                        
                    isLooking = False
    
    #FPS
    time.sleep(0.05)