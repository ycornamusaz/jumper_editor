from color import *
from config import *
import pygame

class Dalle(pygame.sprite.Sprite) :

    def __init__(self, ground_type) :
        
        super().__init__()

        self.conf = Config()

        self.image_1 = pygame.image.load("PNG/gui/back.png")
         
        ## Import picture
        if ground_type == "grass" or ground_type == 0 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_grass.png").convert()
            self.block_type = "grass"
        elif ground_type == "small_grass" or ground_type == 1 :
            self.image_2= pygame.image.load("PNG/Environment/ground_grass_small.png").convert()
            self.block_type = "small_grass"
        elif ground_type == "broken_grass" or ground_type == 2 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_grass_broken.png").convert()
            self.block_type = "broken_grass"
        elif ground_type == "small_broken_grass" or ground_type == 3 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_grass_small_broken.png").convert()
            self.block_type = "small_broken_grass"
        elif ground_type == "stone" or ground_type == 4 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_stone.png").convert()
            self.block_type = "stone"
        elif ground_type == "small_stone" or ground_type == 5 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_stone_small.png").convert()
            self.block_type = "small_stone"
        elif ground_type == "broken_stone" or ground_type == 6 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_stone_broken.png").convert()
            self.block_type = "broken_stone"
        elif ground_type == "small_broken_stone" or ground_type == 7 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_stone_small_broken.png").convert()
            self.block_type = "small_broken_stone"
        elif ground_type == "cake" or ground_type == 8 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_cake.png").convert()
            self.block_type = "cake"
        elif ground_type == "small_cake" or ground_type == 9 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_cake_small.png").convert()
            self.block_type = "small_cake"
        elif ground_type == "broken_cake" or ground_type == 10 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_cake_broken.png").convert()
            self.block_type = "broken_cake"
        elif ground_type == "small_broken_cake" or ground_type == 11 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_cake_small_broken.png").convert()
            self.block_type = "small_broken_cake"
        elif ground_type == "snow" or ground_type == 12 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_snow.png").convert()
            self.block_type = "snow"
        elif ground_type == "small_snow" or ground_type == 13 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_snow_small.png").convert()
            self.block_type = "small_snow"
        elif ground_type == "broken_snow" or ground_type == 14 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_snow_broken.png").convert()
            self.block_type = "broken_snow"
        elif ground_type == "small_broken_snow" or ground_type == 15 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_snow_small_broken.png").convert()
            self.block_type = "small_broken_snow"
        elif ground_type == "sand" or ground_type == 16 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_sand.png").convert()
            self.block_type = "sand"
        elif ground_type == "small_sand" or ground_type == 17 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_sand_small.png").convert()
            self.block_type = "small_sand"
        elif ground_type == "broken_sand" or ground_type == 18 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_sand_broken.png").convert()
            self.block_type = "broken_sand"
        elif ground_type == "small_broken_sand" or ground_type == 19 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_sand_small_broken.png").convert()
            self.block_type = "small_broken_sand"
        elif ground_type == "wood" or ground_type == 20 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_wood.png").convert()
            self.block_type = "wood"
        elif ground_type == "small_wood" or ground_type == 21 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_wood_small.png").convert()
            self.block_type = "small_wood"
        elif ground_type == "broken_wood" or ground_type == 22 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_wood_broken.png").convert()
            self.block_type = "broken_wood"
        elif ground_type == "small_broken_wood" or ground_type == 23 :
            self.image_2 = pygame.image.load("PNG/Environment/ground_wood_small_broken.png").convert()
            self.block_type = "small_broken_wood"
        elif ground_type == 24 :
            self.image_2 = pygame.image.load("PNG/Players/bunny1_stand.png").convert()
        elif ground_type == 25 :
            self.image_2 = pygame.image.load("PNG/Enemies/spikeMan_stand.png").convert()
        elif ground_type == 26 :
            self.image_2 = pygame.image.load("PNG/Enemies/flyMan_stand.png").convert()
        elif ground_type == 27 :
            self.image_2 = pygame.image.load("PNG/Enemies/cloud.png").convert()
        elif ground_type == 28 :
            self.image_2 = pygame.image.load("PNG/Enemies/wingMan1.png").convert()
        else :
            print("Valid blocks types :\r\n    grass\r\n    small_grass\r\n    broken_grass\r\n    small_broken_grass\r\n    stone\r\n    small_stone\r\n    broken_stone")
            print("    small_broken_stone\r\n    cake\r\n    small_cake\r\n    broken_cake\r\n    small_broken_cake\r\n    snow\r\n    small_snow\r\n    broken_snow")
            print("    small_broken_snow\r\n    sand\r\n    small_sand\r\n    broken_sand\r\n    small_broken_sand\r\n    wood\r\n    small_wood\r\n    broken_wood")
            print("    small_broken_wood")
        
        
        self.image_1 = pygame.transform.scale(self.image_1, [int(self.image_1.get_width()*self.conf.factor), int(self.image_1.get_height()*self.conf.factor)])
        self.image_2 = pygame.transform.scale(self.image_2, [int(self.image_2.get_width()/4.75), int(self.image_2.get_height()/4.75)])
        self.image = pygame.Surface([self.image_1.get_width(),self.image_1.get_height()])

        self.image.set_colorkey(Color.BLACK)
        self.image_1.set_colorkey(Color.BLACK)
        self.image_2.set_colorkey(Color.BLACK)

        ## Get sprite position
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = (self.conf.width/2 - self.width/2)
        self.rect.y = 32

        self.image_2_width = self.image_2.get_width()
        self.image_2_height = self.image_2.get_height()

        self.image.blit(self.image_1, [0,0])
        self.image.blit(self.image_2, [(self.width/2 - self.image_2_width/2), (self.height/2 - self.image_2_height/2)])


        if ground_type < 24 :
            self.entity_type = "block"
        elif ground_type == 24 :
            self.entity_type = "player"
        elif ground_type == 25 :
            self.entity_type = "enemie"
            self.enemie_type = "spikeman"
        elif ground_type == 26 :
            self.entity_type = "enemie"
            self.enemie_type = "flyman"
        elif ground_type == 27 :
            self.entity_type = "enemie"
            self.enemie_type = "cloud"
        elif ground_type == 28 :
            self.entity_type = "enemie"
            self.enemie_type = "wingman"
 
class Arrow(pygame.sprite.Sprite) :

    def __init__(self, arrow) :
        
        super().__init__()

        self.conf = Config()

        self.image_1 = pygame.image.load("PNG/gui/back_2.png")
         
        ## Import picture
        if arrow == 'left' :
            self.image_2 = pygame.image.load("PNG/gui/left.png").convert()
            self.entity_type = 'arrow'
            self.arrow_type = 'left'
        elif arrow == 'right' :
            self.image_2 = pygame.image.load("PNG/gui/right.png").convert()
            self.entity_type = 'arrow'
            self.arrow_type = 'right'
        elif arrow == 'up' :
            self.image_2 = pygame.image.load("PNG/gui/up.png").convert()
            self.entity_type = 'arrow'
            self.arrow_type = 'up'
        elif arrow == 'down' :
            self.image_2 = pygame.image.load("PNG/gui/down.png").convert()
            self.entity_type = 'arrow'
            self.arrow_type = 'down'


        self.image_1 = pygame.transform.scale(self.image_1, [int(self.image_1.get_width()*self.conf.factor), int(self.image_1.get_height()*self.conf.factor)])
        self.image_2 = pygame.transform.scale(self.image_2, [int(self.image_2.get_width()/2), int(self.image_2.get_height()/2)])
        self.image = pygame.Surface([self.image_1.get_width(),self.image_1.get_height()])

        self.image.set_colorkey(Color.BLACK)
        self.image_1.set_colorkey(Color.WHITE)
        self.image_2.set_colorkey(Color.BLACK)

        ## Get sprite position
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = (self.conf.width/2 - self.width/2)
        self.rect.y = 32

        self.image_2_width = self.image_2.get_width()
        self.image_2_height = self.image_2.get_height()

        self.image.blit(self.image_1, [0,0])
        self.image.blit(self.image_2, [(self.width/2 - self.image_2_width/2), (self.height/2 - self.image_2_height/2)])

class Cadre() :

    def __init__(self) :
        
        self.conf = Config()

        self.image_1 = pygame.image.load("PNG/gui/cadre_1.png")
        self.image_2 = pygame.image.load("PNG/gui/cadre_2.png")
         
        self.image_1 = pygame.transform.scale(self.image_1, [int(self.image_1.get_width()*self.conf.factor), int(self.image_1.get_height()*self.conf.factor)])
        self.image_2 = pygame.transform.scale(self.image_2, [int(self.image_2.get_width()*self.conf.factor), int(self.image_2.get_height()*self.conf.factor)])

        self.image_1.set_colorkey(Color.WHITE)
        self.image_2.set_colorkey(Color.WHITE)

        ## Get sprite position
        self.rect = self.image_1.get_rect()

        self.width = self.image_1.get_width()
        self.height = self.image_1.get_height()
        self.rect.x = (self.conf.width/2 - self.width/2)
        self.rect.y = 32

    def update_cadre(self, screen) :

        ## Print background on screen
        screen.blit(self.image_1, [20, 15])
    
    def update_fond(self, screen) :

        ## Print background on screen
        screen.blit(self.image_2, [20, 15])

class Trash(pygame.sprite.Sprite) :
    def __init__(self) :

        super().__init__()
        
        self.conf = Config()

        self.image = pygame.image.load("PNG/gui/trash.png")
         
        self.image = pygame.transform.scale(self.image, [int(self.image.get_width()*self.conf.factor), int(self.image.get_height()*self.conf.factor)])

        self.image.set_colorkey(Color.WHITE)

        ## Get sprite position
        self.rect = self.image.get_rect()

        self.entity_type = 'trash'

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = (self.conf.width/2 - self.width/2)
        self.rect.y = 32
