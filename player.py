from color import *
from config import *
import pygame

class Player(pygame.sprite.Sprite):

########## INIT PROCESS ##########

    def __init__(self):
        ## Call the parent class (Sprite) constructor
        super().__init__()

        self.conf = Config()

        ## Import textures
        self.bunny_stand = pygame.image.load("PNG/Players/bunny1_stand.png").convert()

        ## Resize images
        self.bunny_stand = pygame.transform.scale(self.bunny_stand, [int(self.bunny_stand.get_width()*self.conf.factor), int(self.bunny_stand.get_height()*self.conf.factor)])

        ## Set texture background to transparent
        self.bunny_stand.set_colorkey(Color.BLACK)
       
        ## Set texture
        self.image = self.bunny_stand

        ## Set mask
        self.mask = pygame.mask.from_surface(self.image)
       
        self.entity_type = "player"

        ## Get sprite position
        self.rect = self.image.get_rect()

        ## Get sprite width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        ## Set player default position
        self.rect.y = 1080 - 32 - 94 - self.height
        self.rect.x = 32

