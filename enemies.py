import pygame
from config import *
from color import *

class SpikeMan(pygame.sprite.Sprite):
    
    def __init__(self):
        ## Call the parent class (Sprite) constructor
        super().__init__()

        self.conf = Config()

        ## Import textures
        self.spikeman_stand = pygame.image.load("PNG/Enemies/spikeMan_stand.png").convert()

        ## Resize images
        self.spikeman_stand = pygame.transform.scale(self.spikeman_stand, [int(self.spikeman_stand.get_width()*self.conf.factor), int(self.spikeman_stand.get_height()*self.conf.factor)])
        ## Set texture background to transparent
        self.spikeman_stand.set_colorkey(Color.BLACK)
       
        ## Set texture
        self.image = self.spikeman_stand

        ## Set mask
        self.mask = pygame.mask.from_surface(self.image)
       
        self.enemie_type = "spikeman"
        self.entity_type = "enemie"
        self.is_ghost = False
        self.has_ghost = False

        ## Get sprite position
        self.rect = self.image.get_rect()

        ## Get sprite width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        ## Set player default position
        self.rect.y = 1080 - 32 - 94 - self.height
        self.rect.x = 32

    def update(self, text, color_txt):

        ## Update text
        self.text = text
        ## Update text color
        self.color = color_txt
        ## Set font and font size
        self.font = pygame.font.SysFont("Ubuntu", int(25*self.conf.factor))
        ## Creat text object
        self.textSurf = self.font.render(self.text, 1, self.color)
        ## Get the text object width and height
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        ## Fuse text object with the buton
        self.image.blit(self.image_1, [0,0])
        self.image.blit(self.textSurf, [(self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)])

    def to(self, x, groups) :
        if self.is_ghost != True :
            ## Create ghost
            self.ghost = SpikeMan()
            ## Set ghost transparency
            self.ghost.image.set_alpha(100)
            ## Set position
            self.ghost.rect.y = self.rect.y
            self.ghost.rect.x = x
            ## Set ghost specific var
            self.ghost.is_ghost = True
            self.has_ghost = True
            self.ghost.parent = self

            ## Add to groups
            for group in groups :
                group.add(self.ghost)

class FlyMan(pygame.sprite.Sprite):
    
    def __init__(self):
        ## Call the parent class (Sprite) constructor
        super().__init__()

        self.conf = Config()

        ## Import textures
        self.flyman_stand = pygame.image.load("PNG/Enemies/flyMan_stand.png").convert()

        ## Resize images
        self.flyman_stand = pygame.transform.scale(self.flyman_stand, [int(self.flyman_stand.get_width()*self.conf.factor), int(self.flyman_stand.get_height()*self.conf.factor)])

        ## Set texture background to transparent
        self.flyman_stand.set_colorkey(Color.BLACK)
       
        ## Set texture
        self.image = self.flyman_stand

        ## Set mask
        self.mask = pygame.mask.from_surface(self.image)
        
        self.enemie_type = "flyman"
        self.entity_type = "enemie"
        self.is_ghost = False
        self.has_ghost = False

        ## Get sprite position
        self.rect = self.image.get_rect()

        ## Get sprite width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        ## Set player default position
        self.rect.y = 1080 - 32 - 94 - self.height
        self.rect.x = 32

    def update(self, text, color_txt):

        ## Update text
        self.text = text
        ## Update text color
        self.color = color_txt
        ## Set font and font size
        self.font = pygame.font.SysFont("Ubuntu", int(25*self.conf.factor))
        ## Creat text object
        self.textSurf = self.font.render(self.text, 1, self.color)
        ## Get the text object width and height
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        ## Fuse text object with the buton
        self.image.blit(self.image_1, [0,0])
        self.image.blit(self.textSurf, [(self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)])
    
    def to(self, x, groups) :
        if self.is_ghost != True :
            ## Create ghost
            self.ghost = FlyMan()
            ## Set ghost transparency
            self.ghost.image.set_alpha(100)
            ## Set position
            self.ghost.rect.y = self.rect.y
            self.ghost.rect.x = x
            ## Set ghost specific var
            self.ghost.is_ghost = True
            self.has_ghost = True
            self.ghost.parent = self

            ## Add to groups
            for group in groups :
                group.add(self.ghost)

class Cloud(pygame.sprite.Sprite):
    
    def __init__(self):
        ## Call the parent class (Sprite) constructor
        super().__init__()

        self.conf = Config()

        ## Import textures
        self.cloud = pygame.image.load("PNG/Enemies/cloud.png").convert()

        ## Resize images
        self.cloud = pygame.transform.scale(self.cloud, [int(self.cloud.get_width()*self.conf.factor), int(self.cloud.get_height()*self.conf.factor)])

        ## Set texture background to transparent
        self.cloud.set_colorkey(Color.BLACK)
       
        ## Set texture
        self.image = self.cloud

        ## Set mask
        self.mask = pygame.mask.from_surface(self.image)
        
        self.enemie_type = "cloud"
        self.entity_type = "enemie"
        self.is_ghost = False
        self.has_ghost = False

        ## Get sprite position
        self.rect = self.image.get_rect()

        ## Get sprite width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        ## Set player default position
        self.rect.y = 1080 - 32 - 94 - self.height
        self.rect.x = 32

    def update(self, text, color_txt):

        ## Update text
        self.text = text
        ## Update text color
        self.color = color_txt
        ## Set font and font size
        self.font = pygame.font.SysFont("Ubuntu", int(25*self.conf.factor))
        ## Creat text object
        self.textSurf = self.font.render(self.text, 1, self.color)
        ## Get the text object width and height
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        ## Fuse text object with the buton
        self.image.blit(self.image_1, [0,0])
        self.image.blit(self.textSurf, [(self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)])
    
    def to(self, x, groups) :
        if self.is_ghost != True :
            ## Create ghost
            self.ghost = SpikeBall()
            ## Set ghost transparency
            self.ghost.image.set_alpha(100)
            ## Set position
            self.ghost.rect.y = self.rect.y
            self.ghost.rect.x = x
            ## Set ghost specific var
            self.ghost.is_ghost = True
            self.has_ghost = True
            self.ghost.parent = self

            ## Add to groups
            for group in groups :
                group.add(self.ghost)

class SpikeBall(pygame.sprite.Sprite):
    
    def __init__(self):
        ## Call the parent class (Sprite) constructor
        super().__init__()

        self.conf = Config()

        ## Import textures
        self.spikeball_1 = pygame.image.load("PNG/Enemies/spikeBall_1.png").convert()

        ## Resize images
        self.spikeball_1 = pygame.transform.scale(self.spikeball_1, [int(self.spikeball_1.get_width()*self.conf.factor), int(self.spikeball_1.get_height()*self.conf.factor)])

        ## Set texture background to transparent
        self.spikeball_1.set_colorkey(Color.BLACK)
       
        ## Set texture
        self.image = self.spikeball_1

        ## Set mask
        self.mask = pygame.mask.from_surface(self.image)
        
        self.enemie_type = "spikeball"
        self.entity_type = "enemie"
        self.is_ghost = False
        self.has_ghost = False

        ## Get sprite position
        self.rect = self.image.get_rect()

        ## Get sprite width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        ## Set player default position
        self.rect.y = 1080 - 32 - 94 - self.height
        self.rect.x = 32

    def update(self, text, color_txt):

        ## Update text
        self.text = text
        ## Update text color
        self.color = color_txt
        ## Set font and font size
        self.font = pygame.font.SysFont("Ubuntu", int(25*self.conf.factor))
        ## Creat text object
        self.textSurf = self.font.render(self.text, 1, self.color)
        ## Get the text object width and height
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        ## Fuse text object with the buton
        self.image.blit(self.image_1, [0,0])
        self.image.blit(self.textSurf, [(self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)])

    def to(self, x, groups) :
        if self.is_ghost != True :
            ## Create ghost
            self.ghost = SpikeBall()
            ## Set ghost transparency
            self.ghost.image.set_alpha(100)
            ## Set position
            self.ghost.rect.y = self.rect.y
            self.ghost.rect.x = x
            ## Set ghost specific var
            self.ghost.is_ghost = True
            self.has_ghost = True
            self.ghost.parent = self

            ## Add to groups
            for group in groups :
                group.add(self.ghost)

class WingMan(pygame.sprite.Sprite):
    
    def __init__(self):
        ## Call the parent class (Sprite) constructor
        super().__init__()

        self.conf = Config()

        ## Import textures
        self.wingman_1 = pygame.image.load("PNG/Enemies/wingMan1.png").convert()

        ## Resize images
        self.wingman_1 = pygame.transform.scale(self.wingman_1, [int(self.wingman_1.get_width()*self.conf.factor), int(self.wingman_1.get_height()*self.conf.factor)])

        ## Set texture background to transparent
        self.wingman_1.set_colorkey(Color.BLACK)
       
        ## Set texture
        self.image = self.wingman_1

        ## Set mask
        self.mask = pygame.mask.from_surface(self.image)
        
        self.enemie_type = "wingman"
        self.entity_type = "enemie"
        self.is_ghost = False
        self.has_ghost = False

        ## Get sprite position
        self.rect = self.image.get_rect()

        ## Get sprite width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        ## Set player default position
        self.rect.y = 1080 - 32 - 94 - self.height
        self.rect.x = 32

    def update(self, text, color_txt):

        ## Update text
        self.text = text
        ## Update text color
        self.color = color_txt
        ## Set font and font size
        self.font = pygame.font.SysFont("Ubuntu", int(25*self.conf.factor))
        ## Creat text object
        self.textSurf = self.font.render(self.text, 1, self.color)
        ## Get the text object width and height
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        ## Fuse text object with the buton
        self.image.blit(self.image_1, [0,0])
        self.image.blit(self.textSurf, [(self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)])

    def to(self, y, groups) :
        if self.is_ghost != True :
            ## Create ghost
            self.ghost = WingMan()
            ## Set ghost transparency
            self.ghost.image.set_alpha(100)
            ## Set position
            self.ghost.rect.y = y
            self.ghost.rect.x = self.rect.x
            ## Set ghost specific var
            self.ghost.is_ghost = True
            self.has_ghost = True
            self.ghost.parent = self

            ## Add to groups
            for group in groups :
                group.add(self.ghost)

