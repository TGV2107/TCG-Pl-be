import pygame

from Class.Card import *


class CardRect(Card):
    """Sous class de Card, rajout des rect des attributs de Card"""

    def __init__(self, Carte : Card, pos : tuple, scale : tuple, image : pygame.image):
        
        #super class : Card
        super().__init__(Carte.IP, Carte.Name, Carte.Type, Carte.Cost, Carte.Health, Carte.Attack, Carte.Rarity, Carte.Class)

        #scale
        self.scaleX, self.scaleY = scale

        #image
        image = pygame.transform.scale(image, scale)
        self.image = image

        #rect
        posx,posy = pos
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

        #couleurs des textes de stat
        self.HealthColor = (0,0,0)
        self.AttackColor = (0,0,0)
        self.CostColor = (0,0,0)

    def Blit(self, screen):
        
        #affichage du .png de la carte
        screen.blit(self.image, self.rect)

        font = pygame.font.SysFont("Comic Sans MS", self.scaleY//11, bold=True)

        #affichage de la vie
        txt_healt = font.render(str(self.Health), False, self.HealthColor)
        posxHealth = self.rect.x + (self.scaleX * (9/10))
        posyHealth = self.rect.y + (self.scaleY * (8/9))
        screen.blit(txt_healt, (posxHealth, posyHealth))

        #affichage de l'attaque
        txt_attack = font.render(str(self.Attack), False, self.AttackColor)
        posxAttack = self.rect.x + (self.scaleX * (1/35))
        posyAttack = self.rect.y + (self.scaleY * (8/9))
        screen.blit(txt_attack, (posxAttack, posyAttack))

        #affichage du coût
        txt_cost = font.render(str(self.Cost), False, self.CostColor)
        posxCost = self.rect.x + (self.scaleX * (1/35))
        posyCost = self.rect.y - (self.scaleY * (1/100))
        screen.blit(txt_cost, (posxCost, posyCost))