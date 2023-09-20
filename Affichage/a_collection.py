#importation des utilitaires:

import csv
import math
import os

import pygame

from Class.Button import *
from Class.Card import *
from Class.CardRect import *

#importation des classes:


#fonction d'affichage de la page de collection:

def affichage_collection(screen, OwnedCards, page_collection, isLooking, looked_card):
    
    rects = []
    rectCards = []
    posx, posy = 180, 180
    
    #récupération des IP cartes à afficher
    Ip = page_collection*10
    max_Ip = Ip+10
    if max_Ip > len(OwnedCards)-1:
        max_Ip = len(OwnedCards)-1
                        
    for Ncarte in range (Ip, max_Ip): #affichage de chaque carte et enregistrement
        
        #affichage des cartes
        carte = OwnedCards[Ncarte]
        carteRect = CardRect(carte, (posx, posy),(94.5,132), pygame.image.load("Assets/img/Cartes/"+carte.Name+".png"))
                
        carteRect.Blit(screen)

        #ajout de la carte à la liste des cartes affichées
        rectCards.append((carteRect.rect,carte))
        
        #incrémentation des coordonnées
        posx = posx + 180
                    
        if posx == 1080:
                        
            posx = 180
            posy = 360
    
    looked_card_rect = None

    if isLooking == True: #affichage carte cliquée
        
        #affichage de la carte

        looked_card_rect = CardRect(looked_card, (303.75, 30.0),(472.5, 660), pygame.image.load("Assets/img/Cartes/"+looked_card.Name+".png"))    
        looked_card_rect.Blit(screen)
        rects.append(("collection_looked_card",looked_card_rect.rect))
                
    #affichage bouton page suivante
    
    buttonNextPage = Button("->", pygame.font.SysFont("Comic Sans MS", 10, bold=True), (255,255,255), (100,50), (900,600), pygame.image.load("Assets/img/bouton_collection.png"))
    buttonNextPage.Blit(screen)
    rects.append(("collection_buttonNextPage",buttonNextPage.rect))
            
    #affichage bouton page précédente
    
    buttonPreviousPage = Button("<-", pygame.font.SysFont("Comic Sans MS", 10, bold=True), (255,255,255), (100,50), (800,600), pygame.image.load("Assets/img/bouton_collection.png"))
    buttonPreviousPage.Blit(screen)
    rects.append(("collection_buttonPreviousPage",buttonPreviousPage.rect))

    #récupération des decks
    
    wayDecks = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Data"),"Decks.csv")
    
    with open(wayDecks) as file:
        
        r = csv.reader(file)
        
        Decks = {}
        
        for row in r:
            
            Deck_cards = []
            
            wayDecks = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Data"),str(row[0] + ".csv"))
            
            with open(wayDecks) as deck:
                
                r2 = csv.reader(deck)
                
                for card in r2:
                    
                    IP, Name, Type, Cost, Health, Attack, Rarity, Class = card
                    IP, Cost, Health, Attack = int(IP), int(Cost), int(Health), int(Attack)
                    Deck_cards.append(Card(IP, Name, Type, Cost, Health, Attack, Rarity, Class))
                
            Decks[row[0]] = Deck_cards
        
    #affichage des decks
    
    posx, posy = 10, 60
    
    Decks_name = list(Decks.keys())
    
    for deck_name in Decks_name:
        
        font = pygame.font.SysFont("Comic Sans MS", 30, bold=True)
        
        txt_deck = font.render(deck_name,False,(255,255,255))
        
        screen.blit(txt_deck, (posx,posy))
        
        posy = posy + 50
    
    #bouton ajout de deck

    buttonAddDeck = Button("Add deck", pygame.font.SysFont("Comic Sans MS", 10, bold=True), (255,255,255), (100,50), (0,0), pygame.image.load("Assets/img/bouton_collection.png"))
    buttonAddDeck.Blit(screen)
    rects.append(("collection_buttonAddDeck",buttonAddDeck.rect))
    
    #return
    return rectCards, rects