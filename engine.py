import pygame 
import yaml
import ast
from buton import *
from config import *
from color import *
from enemies import *
from ground import *
from player import *
from pointer import *
from gui import *

class Engine() :
    def __init__(self) :

        self.conf = Config()

        ## Get the config var file
        self.conf_data = self.conf.get_config_data()

        ## Open the map configuration file
        try :
            with open(self.conf_data["Config"]["Map"]["file"]) as map_data :
                self.map_data = yaml.load(map_data)
        except :
            pass

        ## Set the shift of the map
        self.shift_x = 0
        ## Set the shift of the gui
        self.shift_gui = 0
        self.shift_pitch = 0

        ## Var to check if the player is used
        self.player_used = False

########## CREATE GUI ##########

    def gen_gui(self, graphic_group, groups) :
        arrow_l = Arrow('left')
        
        arrow_l.rect.x = 35.625 * self.conf.factor
        arrow_l.rect.y = 30 * self.conf.factor

        for group in groups :
            group.add(arrow_l)

        arrow_r = Arrow('right')

        arrow_r.rect.x = self.conf.width - 35.625 * self.conf.factor - arrow_r.width
        arrow_r.rect.y = 30 * self.conf.factor

        for group in groups :
            group.add(arrow_r)

        trash = Trash()

        trash.rect.x = self.conf.width - 35.625 * self.conf.factor - trash.width
        trash.rect.y = self.conf.height - 30 * self.conf.factor - trash.height

        graphic_group.add(trash)
        for group in groups :
            group.add(trash)

        try :
            if x > 0  :
                pass
        except :
            dalle = 0
            x = 0


        for i in range(29) :
            ## Create the dalle
            entity = Dalle(dalle)

            x = entity.width * i + 30 * i + 149
            y = 30

            entity.rect.x = x
            entity.rect.y = y
            entity.entity_number = i

            if (entity.rect.x + entity.width) > (148 * self.conf.factor) and entity.rect.x < (1651 * self.conf.factor) :
                graphic_group.add(entity)

            for group in groups :
                group.add(entity)

            dalle += 1

########## GUI SHIFT ##########

    def move_gui(self, direction, graphic_group, liste) :

        if direction == 'right' :
            for entity in liste :
                if entity.entity_type != 'arrow' and entity.entity_type != 'trash' and entity.entity_number == 28 and (entity.rect.x + entity.width) >= (1651 * self.conf.factor) :
                    self.shift_pitch = -10
                elif entity.entity_type != 'arrow' and entity.entity_type != 'trash' and entity.entity_number == 28 :
                    self.shift_pitch = 0
        elif direction == 'left' :
            for entity in liste :
                if entity.entity_type != 'arrow' and entity.entity_type != 'trash' and entity.entity_number == 0 and entity.rect.x <= (148 * self.conf.factor) :
                    self.shift_pitch = 10
                elif entity.entity_type != 'arrow' and entity.entity_type != 'trash' and entity.entity_number == 0 :
                    self.shift_pitch = 0

        for entity in liste :
            if entity.entity_type != 'arrow' and entity.entity_type != 'trash' :
                if (entity.rect.x + entity.width) <= (148 * self.conf.factor) or entity.rect.x >= (1651 * self.conf.factor) :
                    graphic_group.remove(entity)
                else :
                    graphic_group.add(entity)

                entity.rect.x += self.shift_pitch

        self.shift_gui += self.shift_pitch

########## MAP SHIFT ##########

    def move_map(self, direction, liste) :

        ## If the player is at 1/3 of je screen on the right side
        if direction == 'right' :

            ## Shift all the entities to the left
            for entity in liste :
                entity.rect.x -= 5
                try :
                    if entity.enemie_type != "wingman" :
                        entity.ghost.rect.x -= 5
                except :
                    pass
            self.shift_x -= 5

        ## If the player is at 1/16 of je screen on the left side
        if direction == 'left' :

            ## Shift all the entities to the right
            for entity in liste :
                entity.rect.x += 5
                try :
                    if entity.enemie_type != "wingman" :
                        entity.ghost.rect.x += 5
                except :
                    pass
            self.shift_x += 5

########## BUTON UPDATE ##########

    def update_selected_buton(self, buton_list, pointer, groups) :

        ## Detect rect colision between pointer and buton group
        buton_pointer_list = pygame.sprite.spritecollide(pointer, buton_list, True)

        ## If a rect colision is detected
        if buton_pointer_list != [] : 
            ## For each buton who are in colision with pointer
            for buton in buton_pointer_list :
                if pygame.sprite.collide_mask(pointer, buton) != None :
                    ## Update text Color to red
                    if buton.color != Color.RED :
                        buton.update(buton.text , Color.RED)
                else :
                    ## Update text Color to white
                    if buton.color != Color.WHITE :
                        buton.update(buton.text, Color.WHITE)

                ## Re-add buton to sprite list
                for group in groups :
                    group.add(buton)
        else :
            for buton in buton_list :
                ## Update text Color to white
                if buton.color != Color.WHITE :
                    buton.update(buton.text, Color.WHITE)

########## GET BUTON ##########

    def get_pressed_buton(self, buton_list, pointer, groups) :

        ## Detect rect colision between pointer and buton group
        buton_pointer_list = pygame.sprite.spritecollide(pointer, buton_list, True)
        buton_selected = []
        ## For each butons
        for buton in buton_pointer_list :
            ## Check if the pointer mask and the buton mask are collide
            if pygame.sprite.collide_mask(pointer, buton) != None :
                ## Re-add the buton in the groups
                for group in groups :
                    group.add(buton)
                ## Return the buton
                buton_selected.append(buton)
            else :
                ## Re-add the buton in the groups
                for group in groups :
                    group.add(buton)

        return buton_selected

########## CLEAR ENTITIES ##########

    def clear_entity(self, entity_list) :

        for entity in entity_list :
            if entity.entity_type == 'enemie' and entity.has_ghost :
                entity.ghost.kill()
            entity.kill()

########## CREATE ENTITY FORM BUTON ##########

    def create_entity(self, buton, groups, axis) :

        ## Create entity depends on buton type
        if buton.entity_type == "block" :
            self.entity = Ground(buton.block_type)
        elif buton.entity_type == "player" and self.player_used == False :
            self.entity = Player()
        elif buton.entity_type == 'enemie' :
            if buton.enemie_type == "spikeman" :
                self.entity = SpikeMan()
            elif buton.enemie_type == "flyman" : 
                self.entity = FlyMan()
            elif buton.enemie_type == "cloud" : 
                self.entity = Cloud()
            elif buton.enemie_type == "wingman" : 
                self.entity = WingMan()

        ## Set position
        self.entity.rect.x = axis[0]
        self.entity.rect.y = axis[1]

        ## Add entity to group
        for group in groups :
            group.add(self.entity)

        return self.entity

########## CREATE, CONFIGURE BLOCKS AND DEFAULT PLAYER POSITION  ##########

    def gen_map(self, groups) :

    ##### BLOCKS #####
        try :
            ## For each block types
            for ground_type in self.map_data["Levels"][0]["Blocks"] :
                i = 0

                ## For each blocks
                for x, y in self.map_data["Levels"][0]["Blocks"][ground_type] :

                    ## Read x and y axes
                    x = self.map_data["Levels"][0]["Blocks"][ground_type][i]["x"]*self.conf.factor
                    y = (1000 - self.map_data["Levels"][0]["Blocks"][ground_type][i]["y"])*self.conf.factor

                    ## Create block
                    ground0 = Ground(ground_type)

                    ## Set x and y position
                    ground0.rect.x = x
                    ground0.rect.y = y

                    ## For each groups 
                    for group in groups :
                        ## Add the block to the group
                        group.add(ground0)

                    i += 1
        except :
            pass

    ##### PLAYER #####

        try :
            x = self.map_data["Levels"][0]["Player"]["x"]*self.conf.factor
            y = (1000 - self.map_data["Levels"][0]["Player"]["y"])*self.conf.factor

            player = Player()

            player.rect.x = x
            player.rect.y = y

            for group in groups :
                group.add(player)

        except :
            pass

    ##### ENEMIES #####
        try :
            for enemie_type in self.map_data["Levels"][0]["Enemies"] :
                i = 0

                for x, y, to in self.map_data["Levels"][0]["Enemies"][enemie_type] :
                    x = self.map_data["Levels"][0]["Enemies"][enemie_type][i]["x"]*self.conf.factor
                    y = (1000 - self.map_data["Levels"][0]["Enemies"][enemie_type][i]["y"])*self.conf.factor
                    to = self.map_data["Levels"][0]["Enemies"][enemie_type][i]["to"]*self.conf.factor

                    if enemie_type == "flyman" :
                        enemie0 = FlyMan()

                    elif enemie_type == "spikeman" :
                        enemie0 = SpikeMan()

                    elif enemie_type == "cloud" :
                        enemie0 = Cloud()

                    elif enemie_type == "wingman" :
                        enemie0 = WingMan()

                    enemie0.rect.x = x
                    enemie0.rect.y = y
                    enemie0.start_from = x
                    enemie0.end_to = to
                    enemie0.start_from_base = x
                    enemie0.end_to_base = to
                    if enemie_type == "wingman" :
                        enemie0.start_from = y
                        enemie0.start_from_base = y
                        enemie0.end_to = 1000 - to
                        enemie0.end_to_base = 1000 - to

                    for group in groups :
                        group.add(enemie0)

                    i += 1
        except :
            pass

########## CREATE map.yaml FILE ##########

    def gen_map_file(self, entity_list) :

        ## Vars to check the presence of different parts
        have_blocks = False
        have_enemies = False
        have_player = False
        
        ## Init text vars
        map_data_txt = ''
        enemie_txt = ''
        block_txt = ''
        player_txt = ''

        ## Init lists
        enemie_list = ['spikeman', 'flyman', 'cloud', 'wingman']
        block_list = ['grass', 'small_grass', 'broken_grass', 'small_broken_grass', 'stone', 'small_stone', 'broken_stone', 'small_broken_stone', 'cake', 'small_cake', 'broken_cake', 'small_broken_cake', 'snow', 'small_snow', 'broken_snow', 'small_broken_snow', 'sand', 'small_sand', 'broken_sand', 'small_broken_sand', 'wood', 'small_wood', 'broken_wood', 'small_broken_wood']

        ## Init vars
        for grd_type in block_list :
            exec("%s = ''" % grd_type)
            exec("%s%s = 0" % (grd_type, "_num"))

        for enm_type in enemie_list :
            exec("%s = ''" % enm_type)
            exec("%s%s = 0" % (enm_type, "_num"))

        exec("%s = ''" % 'player')

        ## Scan all entities
        for entity in entity_list :

            ## If the entity is a enemie
            if entity.entity_type == "enemie" :
                ## Mark enemies as present
                have_enemies = True

                ## If there's already an enemie of the same type
                if eval("%s_num" % entity.enemie_type) > 0 :
                    ## Add coma
                    exec("%s += ', '" % entity.enemie_type)

                ## Else
                else :
                    ## Add start text
                    exec("%s += '\\\'%s\\\': ['" % (entity.enemie_type, entity.enemie_type))

                ## Wingman is particular, so make a condition
                if entity.enemie_type == 'wingman' :
                    ## Create the position text
                    exec("%s += '{\\\'x\\\': %d, \\\'y\\\': %d, \\\'to\\\': %d}'" % (entity.enemie_type, entity.rect.x, 1000 - entity.rect.y, 1000 - entity.ghost.rect.y))
                else :
                    ## Create the position text
                    exec("%s += '{\\\'x\\\': %d, \\\'y\\\': %d, \\\'to\\\': %d}'" % (entity.enemie_type, entity.rect.x, 1000 - entity.rect.y, entity.ghost.rect.x))

                ## Increment enemie type number
                exec("%s%s += 1" % (entity.enemie_type, "_num"))

            ## If the entity is a block
            if entity.entity_type == "block" :
                ## Mark the block as present
                have_blocks = True

                ## If there's already a block of the same type
                if eval("%s_num" % entity.ground_type) > 0 :
                    ## Add coma
                    exec("%s += ', '" % entity.ground_type)

                ## Else
                else :
                    ## Add start text
                    exec("%s += '\\\'%s\\\': ['" % (entity.ground_type, entity.ground_type))

                ## Create the position text
                exec("%s += '{\\\'x\\\': %d, \\\'y\\\': %d}'" % (entity.ground_type, entity.rect.x, 1000 - entity.rect.y))
                ## Increment enemie type number
                exec("%s%s += 1" % (entity.ground_type, "_num"))

            ## If the entity is player
            if entity.entity_type == "player" :
                ## Mark player as present
                have_player = True
                
                ## Create the position text
                exec("%s += '{\\\'x\\\': %d, \\\'y\\\': %d}'" % ('player', entity.rect.x, 1000 - entity.rect.y))

##### PLAYER STRING GENERATOR #####

        ## If the player is present
        if have_player :
            ## Add player's text start
            player_txt += "'Player': "
            ## Add player's position
            player_txt += eval("%s" % 'player')

##### ENEMIE STRING GENERATOR #####

        ## If enemies are present
        if have_enemies :
            ## Add enemie's text start
            enemie_txt += "'Enemies': {"

            ## For each enemie
            for enemie in enemie_list :

                ## If there's more than 0 enemie
                if eval("%s_num" % enemie) > 0 :
                    ## If this is not the first enemie
                    if enemie_txt != "'Enemies': {" :
                        ## Add coma
                        enemie_txt += ', '

                    ## Add enemies text
                    enemie_txt += eval("%s" % enemie)
                    ## Close list
                    enemie_txt += ']'

            ## Close dictionary
            enemie_txt += '}'

##### BLOCK STRING GENERATOR #####

        ## If blocks are present
        if have_blocks :
            ## Add block's start text
            block_txt += "'Blocks': {"

            ## For each block
            for block in block_list :

                ## If there's more than 0 block
                if eval("%s_num" % block) > 0 :
                    ## If this is not the first block
                    if block_txt != "'Blocks': {" :
                        ## Add coma
                        block_txt += ', '

                    ## Add blocks text
                    block_txt += eval("%s" % block)
                    ## Close text
                    block_txt += ']'

            ## Close dictionary
            block_txt += '}'

##### MAP STRING GENERATOR #####

        ## Set text start
        map_data_txt = "{'Levels': [{"
        
        ## If player is present
        if have_player :
            ## Add player string to map string
            map_data_txt += player_txt
            ## If blocks or enemies are present
            if have_blocks or have_enemies :
                ## Add coma
                map_data_txt += ', '
        
        ## If blocks are present
        if have_blocks :
            ## Add player string to map string
            map_data_txt += block_txt
            ## If blocks or enemies are present
            if have_enemies :
                ## Add coma
                map_data_txt += ', '
        
        ## If enemies are present
        if have_enemies :
            ## Add player string to map string
            map_data_txt += enemie_txt
        
        ## Close dictionary, list, dictionary
        map_data_txt += "}]}"

        ## Convert map text to dictionary
        map_data = ast.literal_eval(map_data_txt)

        ## Open map.yaml file in write mode
        with open('map.yaml', 'w') as outfile:
            ## Write map_data dictionary as yaml
            outfile.write(yaml.dump(map_data, default_flow_style=False))

        print('Saved !')
