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
        IP, Name, Type, Cost, Health, Attack, Rarity, Class = row
        IP, Cost, Health, Attack = int(IP), int(Cost), int(Health), int(Attack)
        Cards.append(Card(IP, Name, Type, Cost, Health, Attack, Rarity, Class))

with open("Data/Collection.csv") as file:
    
    r = csv.reader(file)
    
    OwnedCards = []
    for row in r:
        IP, Name, Type, Cost, Health, Attack, Rarity, Class = row
        IP, Cost, Health, Attack = int(IP), int(Cost), int(Health), int(Attack)
        OwnedCards.append(Card(IP, Name, Type, Cost, Health, Attack, Rarity, Class))

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
    
    pygame.display.flip()
    screen.fill(game.getBackground())
    
    #affichage de chaque page
    
    if game.getScreen() == "main": #affichage de main

        main_goToCollection_rect = affichage_main(screen)
    
        """
        paramètres : screen
        return : goToCollection.rect
        """
    
    elif game.getScreen() == "collection": #affichage de la collection
            
        rectCards, looked_card_rect, collection_buttonNextPage_rect, collection_buttonPreviousPage_rect, collection_buttonAddDeck_rect = affichage_collection(screen, OwnedCards, page_collection, isLooking, looked_card)
            
        """
        paramètres : screen, Owned Cards, page_collection, isLooking, looked_card
        return : rectCards, looked_card_rect, buttonNextPage.rect, buttonPreviousPage.rect, buttonAddDeck.rect
        """
    #détection des événements                          
    for event in pygame.event.get():
        
        #événement de fermeture de la page pygame
        if event.type == pygame.QUIT:
            
            running = False
            pygame.quit()
        
        #événement si souris cliquée
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
                
            if game.getScreen() == "main": #événements de la page main
                
                if main_goToCollection_rect.collidepoint(event.pos):
                
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
                        
                    #Boutons next et previous page :
                        
                    if collection_buttonNextPage_rect.collidepoint(event.pos):
                            
                        Npages = ((len(OwnedCards)-1)/10) -1
                            
                        if (len(OwnedCards)-1)%10 == 0:
                                
                            Npages = Npages + 1
                            
                        if page_collection < Npages:
                                
                            page_collection = page_collection + 1
                            
                    elif collection_buttonPreviousPage_rect.collidepoint(event.pos):
                            
                        if page_collection > 0:
                                
                            page_collection = page_collection - 1
                        
                    #Bouton add deck :
                        
                    elif collection_buttonAddDeck_rect.collidepoint(event.pos):
                            
                        print("add deck")
                    
                #Fin du zoom:
                elif (isLooking == True) and (not looked_card_rect.rect.collidepoint(event.pos)):
                        
                    isLooking = False
    
    #FPS
    time.sleep(0.05)