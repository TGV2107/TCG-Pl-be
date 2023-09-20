import pygame

class Button:
    """Class permettant de créer un bouton"""

    def __init__(self, text : str, font : pygame.font, color : tuple, scale : tuple, pos : tuple, image : pygame.image):
        
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
        
        #design
        self.font = font
        self.color = color
        self.text = text
        self.design = font.render(text, False, color)

        #text rect
        self.textrect = self.design.get_rect()
        self.textrect.x = self.rect.x + self.scaleX//2 - self.textrect.width //2
        self.textrect.y = self.rect.y + self.scaleY//2 - self.textrect.height //2

    def Blit(self, screen):
        
        screen.blit(self.image, self.rect)
        screen.blit(self.design, self.textrect)