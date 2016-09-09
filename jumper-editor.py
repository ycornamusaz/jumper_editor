#!/usr/bin/python3

import pygame
import yaml
import color
from player import *
from ground import *
from config import *
from buton import *
from pointer import *
from background import *
from engine import *

class Game :
    def menu():
        ## Init pygame
        pygame.init()
        ## Initialise external data configuration
        conf = Config()
        ## Create engine
        engine = Engine()
        ## Init screen
        screen = pygame.display.set_mode([conf.width, conf.height], conf.get_screen_mode())
        ## Init windows title
        pygame.display.set_caption("JUMPER !!! - Menu")
        ## Hide mouse cursor
        pygame.mouse.set_visible(False)
        ## Init clock
        clock = pygame.time.Clock()
        ## Menu loop stat
        done_menu = False
        start_game = False
        start_options = False
        ## Set background
        background = Background()
        ## Create menu sprite group
        buton_list = pygame.sprite.Group()
        all_menu_sprites_list = pygame.sprite.Group()
        pointer_list = pygame.sprite.Group()
        ## Create pointer sprite
        pointer = Pointer()
        ## Add pointer to pointer's list
        pointer_list.add(pointer)
        ## Add pointer to menu sprite's group
        all_menu_sprites_list.add(pointer)
        ## Create butons
        buton1 = Buton("Play", Color.WHITE)
        buton2 = Buton("Options", Color.WHITE)
        buton3 = Buton("Quit", Color.WHITE)
        ## Set buton1 pos
        buton1.rect.x = (conf.width/2 - buton1.width/2)
        buton1.rect.y = (conf.height/2 - buton1.height/2 - 100)
        ## Set buton2 pos
        buton2.rect.x = (conf.width/3 - buton2.width/2)
        buton2.rect.y = (conf.height/2 - buton2.height/2 + 100)
        ## Set buton3 pos
        buton3.rect.x = (conf.width/3*2 - buton3.width/2)
        buton3.rect.y = (conf.height/2 - buton3.height/2 + 100)
        ## Add butons to buton list
        buton_list.add(buton1)
        buton_list.add(buton2)
        buton_list.add(buton3)
        ## Add butons to menu sprite's group
        all_menu_sprites_list.add(buton1)
        all_menu_sprites_list.add(buton2)
        all_menu_sprites_list.add(buton3)

        ## Start loop
        while not done_menu :

            ########## EVENT ZONE ##########

            ## For every events, filter event and refresh screen
            for event in pygame.event.get() :

                ## Filter events
                ## If the cross is pressed, quit game
                if event.type == pygame.QUIT :
                    done_menu = True
                
                ## If any mouse buton is pressed 
                if event.type == pygame.MOUSEBUTTONDOWN :
                    ## Detect if left mouse buton is pressed
                    if event.button == 1 :

                        ## Detect and retourn the pressed buton
                        butons = engine.get_pressed_buton(buton_list, pointer, [all_menu_sprites_list, buton_list])

                        for buton in butons :
                            ## If there's no buton pressed, do nothing
                            if buton == None :
                                pass

                            ## If play buton is pressed, launch the game
                            elif buton.text is "Play" :
                                start_game = True

                            ## If options buton is pressed, launch options menu
                            elif buton.text is "Options" :
                                start_options = True

                            ## If quit buton is pressed, quit the game
                            elif buton.text is "Quit" :
                                done_menu = True

            ########## LOGIC CODE ZONE ##########

            ## Check for restarting the game
            while start_game == True :
                ## Launch game
                Game.game()
                start_game = False
                ## One the player has gameover, launch gameover's screen
                done_menu = True

            ## Update mouse pos
            pos = pygame.mouse.get_pos()
            pointer.rect.x = pos[0]
            pointer.rect.y = pos[1]

            ## Detect bitmap colision between butons and pointer
            engine.update_selected_buton(buton_list, pointer, [all_menu_sprites_list, buton_list])

            ########## CLEAR SCREEN ZONE ##########

            ## Set the background
            background.update(screen)

            ########## DRAWING CODE ZONE ##########

            ## Draw all sprites to the screen
            all_menu_sprites_list.draw(screen)
            pointer_list.draw(screen)

            ########## REFRESH SCREEN ZONE ##########

            ## Refresh screen
            pygame.display.flip()

            ## Set game ticks (per second)
            clock.tick(60)

    def game() :
        ## Load config file
        conf = Config()
        ## Create engine
        engine = Engine()
        ## Init screen        
        screen = pygame.display.set_mode([conf.width, conf.height], conf.get_screen_mode())
        ## Init windows title
        pygame.display.set_caption("JUMPER !!! - Level ##")
        ## Init clock
        clock = pygame.time.Clock()
        ## Hide mouse cursor
        pygame.mouse.set_visible(True)
        ## Set background
        background = Background()
        gui = Cadre()

        ## Set game loop stat
        done_game = False

        entity = None
        entities = []
        direction = None

        ## Create game sprite groups
        mid_layer = pygame.sprite.Group()
        back_layer = pygame.sprite.Group()
        buton_list = pygame.sprite.Group()
        mouvable_list = pygame.sprite.Group()
        all_sprites_list = pygame.sprite.Group()
        pointer_list = pygame.sprite.Group()
        entity_list = pygame.sprite.Group()
        ghost_list = pygame.sprite.Group()

        ## Create pointer sprite
        pointer = Pointer()

        ## Add pointer to pointer's list
        pointer_list.add(pointer)

        ## Add pointer to menu sprite's group
        all_sprites_list.add(pointer)

        ## Generate map
        engine.gen_gui(back_layer, [buton_list, all_sprites_list])

        ## Start game loop
        while not done_game :

            ########## EVENT ZONE ##########

            ## For every events, filter event and refresh screen
            for event in pygame.event.get() :

                ## Filter events
                ## If the cross is pressed, quit game
                if event.type == pygame.QUIT :
                    done_game = True

                ## If a key is pressed
                if event.type == pygame.KEYDOWN :
                    ## If escape is pressed, quit game
                    if event.key == pygame.K_ESCAPE :
                        done_game = True

                    ## If 's' is pressed, save file
                    if event.key == pygame.K_s :
                        engine.gen_map_file(entity_list)

                    ## If the left arrow is pressed
                    if event.key == pygame.K_LEFT :
                        direction = 'left'

                    ## If the right arrow is pressed
                    if event.key == pygame.K_RIGHT :
                        direction = 'right'

                ## If a key is release
                if event.type == pygame.KEYUP :
                    ## If the left arrow is release
                    if event.key == pygame.K_LEFT :
                        direction = None

                    ## If the right arrow is release
                    if event.key == pygame.K_RIGHT :
                        direction = None

                ## If any mouse buton are release
                if event.type == pygame.MOUSEBUTTONUP :

                    if event.button == 1 or event.button == 3 :
                        ## If a entity is selected
                        if entity != None :
                            ## Release it
                            entity = None

                ## If any mouse buton is pressed 
                if event.type == pygame.MOUSEBUTTONDOWN :
                    ## Detect if left mouse buton is pressed
                    if event.button == 1 :

                        ## Return clicked entity
                        entities = engine.get_pressed_buton(entity_list, pointer, [all_sprites_list, back_layer, entity_list, mouvable_list])

                        if entities != [] :
                            ## If there's a clicked entity, you can move it
                            for entity in entities :
                                
                                shift_x = pointer.rect.x - entity.rect.x
                                shift_y = pointer.rect.y - entity.rect.y
                                try : 
                                    ## If entity has a ghost, the ghos will move with it
                                    if entity.has_ghost == True :
                                        shift_ghost_x = entity.ghost.rect.x - entity.rect.x
                                        shift_ghost_y = entity.ghost.rect.y - entity.rect.y

                                except :
                                    pass

                        else :
                            ## Detect and retourn the pressed buton
                            butons = engine.get_pressed_buton(buton_list, pointer, [all_sprites_list, back_layer, buton_list, back_layer])

                            if butons != [] :
                                for buton in butons :
                                    
                                    ## If there's no clicked entity entity 
                                    if buton.entity_type != None and buton.entity_type != 'arrow' and buton.entity_type != 'gui' and entity == None and pointer.rect.x > 148 * conf.factor and pointer.rect.x < 1651 * conf.factor :
                                        ## Create entity depends on buton
                                        entity = engine.create_entity(buton, [entity_list, all_sprites_list, back_layer, mouvable_list], [pointer.rect.x, pointer.rect.y])
                                        shift_x = pointer.rect.x - entity.rect.x
                                        shift_y = pointer.rect.y - entity.rect.y

                                    elif buton.entity_type == 'arrow' :
                                        if buton.arrow_type == 'right' :
                                            direction_gui = 'right'
                                        elif buton.arrow_type == 'left' :
                                            direction_gui = 'left'

                    ## If right buton is pressed
                    if event.button == 3 :

                        ## Return clicked entity
                        entities = engine.get_pressed_buton(entity_list, pointer, [all_sprites_list, back_layer, entity_list, mouvable_list])

                        ## I don't remember :P
                        if entities == [] or entities[0].entity_type == "block" or entities[0].entity_type != "player" and entities[0].has_ghost == True :
                            entities = engine.get_pressed_buton(ghost_list, pointer, [all_sprites_list, back_layer, ghost_list, mouvable_list])

                            for entity in entities :
                                ## If there's an entity, move it
                                shift_x = pointer.rect.x - entity.rect.x
                                shift_y = pointer.rect.y - entity.rect.y

                        ## If there's a enemie, place the ghost
                        if entities != [] :
                            for entity in entities :
                                if entity.entity_type != "block" and entity.entity_type != "player" and entity.is_ghost == False and entity.has_ghost == False :
                                    if entity.enemie_type == "wingman" :
                                        entity.to(pointer.rect.y, [all_sprites_list, back_layer, ghost_list, mouvable_list])
                                    else :
                                        entity.to(pointer.rect.x, [all_sprites_list, back_layer, ghost_list, mouvable_list])

                                    entity = entity.ghost

                if event.type == pygame.MOUSEBUTTONUP :
                    if event.button == 1 :
                        direction_gui = None
                        entity = None
                        entities = []

                    if event.button == 3 :
                        entity = None
                        entities = []

            ########## LOGIC CODE ZONE ##########

            ## Update mouse pos
            pos = pygame.mouse.get_pos()
            pointer.rect.x = pos[0]
            pointer.rect.y = pos[1]

            if direction != None :
                engine.move_map(direction, entity_list)

            if direction_gui != None :
                engine.move_gui(direction_gui, back_layer, buton_list)

            if entity != None :
                ## If there's a clicked entity
                try :
                    ## If this is a ghost, move it with entity specificity
                    if entity.is_ghost == True : 
                        if entity.enemie_type == "wingman" and pointer.rect.y - shift_y < entity.parent.rect.y :
                            entity.rect.y = pointer.rect.y - shift_y
                        elif entity.enemie_type == "spikeball" and pointer.rect.x > entity.parent.rect.x + entity.parent.width/2 :
                            entity.rect.x = entity.parent.rect.x + entity.parent.width/2 + 200
                            entity.rect.y = entity.parent.rect.y + 150
                        elif entity.enemie_type == "spikeball" and pointer.rect.x < entity.parent.rect.x + entity.parent.width/2 :
                            entity.rect.x = entity.parent.rect.x + entity.parent.width/2 - entity.width - 200
                            entity.rect.y = entity.parent.rect.y + 150
                        elif pointer.rect.x - shift_x > entity.parent.rect.x :
                            entity.rect.x = pointer.rect.x - shift_x
                    
                    ## If entity has a ghost, move the ghost with it
                    else :
                        if entity.has_ghost == True :
                            entity.rect.x = pointer.rect.x - shift_x
                            entity.rect.y = pointer.rect.y - shift_y
                            if entity.enemie_type == "wingman" :
                                entity.ghost.rect.x = entity.rect.x
                                entity.ghost.rect.y = entity.rect.y + shift_ghost_y
                            elif entity.enemie_type == "cloud" :
                                if entity.ghost.rect.x > entity.rect.x :
                                    entity.ghost.rect.x = entity.rect.x + entity.width/2 + 200
                                    entity.ghost.rect.y = entity.rect.y + 150
                                elif entity.ghost.rect.x < entity.rect.x :
                                    entity.ghost.rect.x = entity.rect.x + entity.width/2 - entity.ghost.width - 200
                                    entity.ghost.rect.y = entity.rect.y + 150
                            else : 
                                entity.ghost.rect.x = entity.rect.x + shift_ghost_x 
                                entity.ghost.rect.y = entity.rect.y
                        
                        entity.rect.x = pointer.rect.x - shift_x
                        entity.rect.y = pointer.rect.y - shift_y

                except :
                    ## If the entity is not or have not a ghost, just move it
                    entity.rect.x = pointer.rect.x - shift_x
                    entity.rect.y = pointer.rect.y - shift_y
            
            for buton in buton_list :
                if buton.entity_type == 'arrow' :
                    mid_layer.add(buton)

            ## Detect bitmap colision between butons and pointer
            #engine.update_selected_buton(buton_list, pointer, [all_sprites_list, buton_list])
 
            ########## CLEAR SCREEN ZONE ##########

            ## Set the entier screnn to white
            #screen.fill(Color.BLACK)
            background.update(screen)

            ########## DRAWING CODE ZONE ##########

            ## Draw all sprites to the screen
            #all_sprites_list.draw(screen)
            back_layer.draw(screen)
            gui.update_fond(screen)
            mid_layer.draw(screen)
            gui.update_cadre(screen)
            pointer_list.draw(screen)

            ########## REFRESH SCREEN ZONE ##########

            ## Refresh screen
            pygame.display.flip()

            ## Set game tick (per second)
            clock.tick(60)


Game.menu()
