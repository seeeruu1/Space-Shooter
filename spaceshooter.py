import pygame,sys, random
from pygame.math import Vector2

class SHIP:      # player images, movements, animation
    def __init__(self):
        self.ship0 = pygame.image.load('img/0.png').convert_alpha()
        self.ship1 = pygame.image.load('img/1.png').convert_alpha()
        self.ship2 = pygame.image.load('img/2.png').convert_alpha()

        self.shield = pygame.image.load('img/protection.png').convert_alpha()

        self.exp1 = pygame.image.load('img/explosion1.png')
        self.exp2 = pygame.image.load('img/explosion2.png')
        self.exp3 = pygame.image.load('img/explosion3.png')
        self.exp4 = pygame.image.load('img/explosion4.png')
        self.exp5 = pygame.image.load('img/explosion5.png')
        self.exp6 = pygame.image.load('img/explosion6.png')

        self.explosions = [self.exp1, self.exp2,self.exp3, self.exp4,self.exp5, self.exp6]

        self.x_pos = 300
        self.y_pos = 550

        self.img_index = 0
        self.image = [self.ship0, self.ship1, self.ship2]

        self.rect = self.image[int(self.img_index)].get_rect(topleft = (self.x_pos,self.y_pos))
        self.shield_rect = self.shield.get_rect(center = (self.x_pos, self.y_pos))
        self.shield_on = False
        self.protection_timing = 300

        self.exploding = False
        self.dead = False
        

    def movement(self):
        keys = pygame.key.get_pressed()
        if not self.exploding:
            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                self.x_pos -= 5
            
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.x_pos += 5

        self.x_pos = max(25, min(self.x_pos, 1025 - self.rect.width))    

        self.rect = self.ship1.get_rect(center = (self.x_pos,self.y_pos))
        if self.shield_on:
            self.shield_rect = self.shield.get_rect(center = (self.x_pos, self.y_pos))


    def animation(self):
        screen.blit(self.image[int(self.img_index)], self.rect)

        if not self.exploding:
            self.img_index += 0.1
            if self.img_index >= len(self.image): 
                self.img_index = 0
            
        if self.exploding:
            self.image = self.explosions
            self.img_index += 0.1
            if self.img_index >= len(self.image):
                self.dead = True
                self.img_index -= 0.1
                  

    def protection(self):
        if self.protection_timing >= 0:
            screen.blit(self.shield,self.shield_rect)
            text = Font_20.render(f"{self.protection_timing // 10}",1,"White")
            screen.blit(text,(950,20))

        else:
            self.shield_on = False
            self.protection_timing = 300
        self.protection_timing -= 1
    
    

    def update(self):
        self.movement()
        self.animation()
        if self.shield_on:
            self.protection() 

class BULLET: #bullet and go up
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('img/bullet.png').convert_alpha()
        self.image2 = pygame.image.load('img/laser.png').convert_alpha()
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def go_up(self):
        if self.y > 50:
            self.y -= 10  # Move the bullet upward
            screen.blit(self.image, self.rect)
        self.rect.y = self.y  # Update the rect position

    def go_down(self):
        if self.y < 620:
            self.y += 10  # Move the bullet downward
            screen.blit(self.image2, self.rect)
        self.rect.y = self.y

class ENEMY: #images and animation, movement
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        self.countdwn = random.randint(100,600)
        self.fire = False

        self.pos = Vector2(x,y)

        self.enemy1 = pygame.image.load('img/enemy1.png').convert_alpha()
        self.enemy2 = pygame.image.load('img/enemy2.png').convert_alpha()
        self.enemy3 = pygame.image.load('img/enemy3.png').convert_alpha()

        self.bomb1 = pygame.image.load('img/bomb1.png').convert_alpha()
        self.bomb2 = pygame.image.load('img/bomb2.png').convert_alpha()
        self.bomb3 = pygame.image.load('img/bomb3.png').convert_alpha()

            
        self.img_index = 0
        self.image = [self.enemy1, self.enemy2, self.enemy3] 

        self.rect = self.image[int(self.img_index)].get_rect(center = self.pos)

        self.explode = False

        self.bombing = [self.bomb1, self.bomb2, self.bomb3]

        self.dead = False

        self.direction = -1

    def animation(self):
        screen.blit(self.image[int(self.img_index)], self.rect)##
        
        if not self.explode:
            self.img_index += 0.1
            if self.img_index >= len(self.image): 
                self.img_index = 0

        elif self.explode:
            self.image = self.bombing
            self.img_index += 0.03
            if self.img_index >= len(self.image): 
                self.dead = True
                self.img_index = 0

    def movement(self):
        self.x += self.direction
        self.y += 0.1
        self.rect = self.image[int(self.img_index)].get_rect(center = (self.x, self.y))

    
    def shoot(self):
        self.countdwn -= 1
        if self.countdwn <= 0:
            self.fire = True
            self.countdwn = random.randint(100,600)

    def update(self):
        self.animation()
        self.movement()
        self.shoot()
        
class OBSTACLES:
    def __init__(self):
        self.x = random.choice([-60,1050])
        self.y = random.choice([-61,751])

        self.speed_x = 1
        self.speed_y = 1

        self.rock1 = pygame.image.load('img/rock1.png').convert_alpha()
        self.rock2 = pygame.image.load('img/rock2.png').convert_alpha()
        self.rock3 = pygame.image.load('img/rock3.png').convert_alpha()

        self.exp1 = pygame.image.load('img/exp1.png').convert_alpha()
        self.exp2 = pygame.image.load('img/exp2.png').convert_alpha()
        self.exp3 = pygame.image.load('img/exp3.png').convert_alpha()
        self.exp4 = pygame.image.load('img/exp4.png').convert_alpha()

        self.img_index = 0

        self.image = [self.rock1, self.rock2, self.rock3]
        self.explodings = [self.exp1, self.exp2, self.exp3, self.exp4]

        self.rect = self.image[int(self.img_index)].get_rect(center = (self.x,self.y))

        self.explode = False
        self.dead = False

        self.button = 0
    def move_it(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < -60 or self.x > 1050:
            self.speed_x *= -1
        
        if self.y < -61 or self.y > 751:
            self.speed_y *= -1

        self.rect = self.image[int(self.img_index)].get_rect(center = (self.x,self.y))
        screen.blit(self.image[int(self.img_index)], self.rect)
       

    def animation(self):
        screen.blit(self.image[int(self.img_index)], self.rect)

        if not self.explode:
            self.img_index += 0.1
            if self.img_index >= len(self.image): 
                self.img_index = 0

        if self.explode:
            self.image = self.explodings
            self.img_index += 0.25
            if self.img_index >= len(self.explodings): 
                self.dead = True
                self.img_index = 0

class HELP:
    def __init__(self,type,x,y):
        self.x = x
        self.y = y
        self.type = type

        if self.type == 'aids':
            self.image = pygame.image.load('img/aids.png').convert_alpha()
        else:
            self.image = pygame.image.load('img/shield.png').convert_alpha()
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def go_down(self):
        if self.y < 620:
            self.y += 5  # Move the bullet downward
            screen.blit(self.image, self.rect)
        self.rect.y = self.y

class MAIN():
    def __init__(self):
        self.bg2_img = pygame.image.load('img/bg2.png')

        self.health1 = pygame.image.load('img/01.png').convert_alpha()
        self.health2 = pygame.image.load('img/02.png').convert_alpha()
        self.health3 = pygame.image.load('img/03.png').convert_alpha()
        self.health4 = pygame.image.load('img/04.png').convert_alpha()
        self.health5 = pygame.image.load('img/05.png').convert_alpha()
        self.health6 = pygame.image.load('img/06.png').convert_alpha()

        self.shield_image = pygame.image.load('img/shield.png').convert_alpha()
        self.enemy_image = pygame.image.load('img/enemy.png').convert_alpha()

        self.bars = [self.health1, self.health2,self.health3,self.health4,self.health5,self.health6]

        self.health_stage = 0

        self.game_on = False

        self.state = None

        self.player = SHIP()
        
        self.enemy_spots = [
    Vector2(350, 70), Vector2(350, 120), Vector2(350, 170), Vector2(350, 220),Vector2(350,270),
    Vector2(400, 70), Vector2(400, 120), Vector2(400, 170), Vector2(400, 220),Vector2(400,270),
    Vector2(450, 70), Vector2(450, 120), Vector2(450, 170), Vector2(450, 220),Vector2(450,270),
    Vector2(500, 70), Vector2(500, 120), Vector2(500, 170), Vector2(500, 220),Vector2(500, 270),
    Vector2(550, 70), Vector2(550, 120), Vector2(550, 170), Vector2(550, 220),Vector2(550, 270),
    Vector2(600, 70), Vector2(600, 120), Vector2(600, 170), Vector2(600, 220),Vector2(600, 270),
    Vector2(650, 70), Vector2(650, 120), Vector2(650, 170), Vector2(650, 220),Vector2(650,270)
]
        
        self.obstacts = []
        self.bullets = []
        self.enemies = []
        self.lasers = []
        self.helps = []
        
        self.enemy_spawn()
        self.new_obs()

        self.button = 0

        self.options = True
        self.resetting = False
       
        #rects
        self.playl = pygame.Rect(1000 / 2 - 150, 250, 300,70)
        self.how_to = pygame.Rect(1000 / 2 -150, 350, 300,70)
        self.exit = pygame.Rect(1000 / 2 -150, 450, 300,70)
        self.back = pygame.Rect(1000 / 2 -150, 550, 300,70)

    def page(self):
        screen.blit(self.bg2_img,(0,0))

    #0 front #1 play #2 how to #3 exit
        if self.button == 0:
            #draw
            blue = '#000833'
            green = '#388e3c'
            pygame.draw.rect(screen,blue,self.playl,0,10)
            pygame.draw.rect(screen,blue,self.how_to,0,10)
            pygame.draw.rect(screen,blue,self.exit,0,10)

            mouse_pos = pygame.mouse.get_pos()

            if self.playl.collidepoint(mouse_pos):
                pygame.draw.rect(screen,green,self.playl,0,10)

            elif self.how_to.collidepoint(mouse_pos):
                pygame.draw.rect(screen,green,self.how_to,0,10)

            elif self.exit.collidepoint(mouse_pos):
                pygame.draw.rect(screen,green,self.exit,0,10)

            #text
            text_1 = Font.render('PLAY',1,"White")
            screen.blit(text_1,  (435,260))

            text_2 = Font_40.render('How to play',1,"White")
            screen.blit(text_2, (390,365))

            text_3 = Font.render('EXIT',1,"White")
            screen.blit(text_3, (435,460))

        elif self.button == 1:
            self.game_on = True

        elif self.button == 2:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                tips = pygame.image.load('img/tips2.png')
            else:
                tips = pygame.image.load('img/tips.png')

            
            
            screen.blit(tips, (0,0))
            self.back_page()
            text_it = Font_20.render("Press 'A' to view Arabic translation", 1, "Red")
            screen.blit(text_it, (150,10))
        elif self.button == 3:
            pygame.quit()
            sys.exit()

    def back_page(self):
        pygame.draw.rect(screen,'#000833',self.back,0,10)

        if self.back.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen,'#388e3c',self.back,0,10)

        text_3 = Font_20.render('BACK TO MAIN PAGE',1,"White")
        screen.blit(text_3, (400,575))
        self.resetting = True

    def health_bar(self):
            if self.health_stage < len(self.bars):
                screen.blit(self.bars[self.health_stage],(880,600))
            else:
                screen.blit(self.bars[-1],(880,600))
                self.player.exploding = True

    def new_obs(self):
        if self.game_on and len(self.enemies) >0:
            self.obstacts.append(OBSTACLES())
        
    def enemy_spawn(self):
        for _ in range(len(self.enemy_spots)):
            for spot in self.enemy_spots:
                self.enemies.append(ENEMY(spot.x, spot.y))
                self.enemy_spots.remove(spot)
     
    def enemy_shooting(self):
        for enemy in self.enemies:
            if enemy.fire:
                self.lasers.append(BULLET(enemy.x, enemy.y))
                laser_sound.play()
                enemy.fire = False

    def player_shooting(self):
        self.bullets.append(BULLET(main.player.x_pos,main.player.y_pos))
        bullet_sound.play()

    def enemy_direct(self):
        if self.enemies:
            if self.enemies[0].x <= 20 or self.enemies[-1].x >= 930:
                for enemy in self.enemies:
                    enemy.direction *= -1

    def shoot(self):
        for bullet in self.bullets:
            bullet.go_up()
            if bullet.y <= 50:
                self.bullets.remove(bullet)
                 
        if self.lasers:
            for laser in self.lasers:
                laser.go_down()
                if laser.y >= 620:
                    self.lasers.remove(laser)

        if self.helps:
            for help in self.helps:
                help.go_down()
                if help.y >= 620:
                    self.helps.remove(help)
        
    def collisions(self):
        #enemy and bullet
        for enemy in self.enemies:
            for bullet in self.bullets: 
                if enemy.rect.colliderect(bullet.rect):
                    enemy.explode = True
                    explo_enemy.play()
                    self.bullets.remove(bullet)

        #player and enemy
            if self.player.rect.colliderect(enemy.rect):
                enemy.explode = True
                explo_enemy.play()
                self.player.exploding = True
                self.health_stage = 5
            if enemy.dead:
                self.enemies.remove(enemy)
                

        #obstat and player
        if self.obstacts:
            for obs in self.obstacts:
                if self.player.rect.colliderect(obs.rect):
                    self.obstacts.remove(obs)
                    if not self.player.shield_on:
                       self.player.exploding = True
                       

        
        #obstazct and bullet 
        if self.obstacts:
            for obs in self.obstacts: 
                for bullet in self.bullets:
                    if bullet.rect.colliderect(obs.rect):
                        self.bullets.remove(bullet)
                        obs.explode = True 
                        explo_astro.play()
                        
                if obs.dead:
                    self.helps.append(HELP(random.choice(['aids','shield']),obs.x, obs.y))
                    self.obstacts.remove(obs)
                    
        #laser and player
        if self.lasers:
            for laser in self.lasers:
                if self.player.rect.colliderect(laser.rect):
                    self.lasers.remove(laser)
                    if not self.player.shield_on:
                        if self.health_stage < 7:
                            self.health_stage += 1
                      
        #helps and player
        if self.helps:
            for help in self.helps:
                if self.player.rect.colliderect(help.rect):
                    helps_sound.play()
                    if help.type == 'aids':
                        if self.health_stage > 0:
                            self.health_stage -= 1
                    else:
                        self.player.shield_on = True
                        self.player.protection_timing = 300
                    self.helps.remove(help)

       #lasers and bullets 
        if self.bullets :
            if self.lasers:
                for bullet in self.bullets:
                    for laser in self.lasers: 
                        if bullet.rect.colliderect(laser.rect):
                            self.lasers.remove(laser)
                            self.bullets.remove(bullet)
                             
    def assets(self):
            self.health_bar()
            text = Font_20.render(f'{len(self.enemies)}',1,"White")
            screen.blit(text, (50,15))
            screen.blit(self.enemy_image, (10, 10))

            if not self.player.shield_on:
                text = Font_20.render("0",1,"White")
                screen.blit(text,(950,20))
            screen.blit(self.shield_image, (915,10))

    def win_or_lose(self):
        if len(self.enemies) <= 0 and len(self.obstacts)<= 0 and not self.player.exploding:
            self.state = "win"
        
        if self.player.dead:
                self.state = "lose"
        
        if self.state != None:
            self.game_on = False

    def winner_or_loser(self):
        if self.state != None:
            screen.fill((26, 39, 55))

            if self.state == 'win':
                text = Font.render("YOU WIN !",1,'White')
                
            elif self.state == 'lose':
                text = Font.render("YOU LOST !",1,'White')

            screen.blit(text, ((1000 - text.get_rect().width) / 2, 250))
            self.back_page()
            
    def reset(self):
            self.obstacts.clear()
            self.bullets.clear()
            self.enemies.clear()
            self.lasers.clear()
            self.helps.clear()
                
            self.health_stage = 0
            self.game_on = False
            self.state = None
            self.player = SHIP()
            
            self.enemy_spots = [
    Vector2(350, 70), Vector2(350, 120), Vector2(350, 170), Vector2(350, 220),Vector2(350,270),
    Vector2(400, 70), Vector2(400, 120), Vector2(400, 170), Vector2(400, 220),Vector2(400,270),
    Vector2(450, 70), Vector2(450, 120), Vector2(450, 170), Vector2(450, 220),Vector2(450,270),
    Vector2(500, 70), Vector2(500, 120), Vector2(500, 170), Vector2(500, 220),Vector2(500, 270),
    Vector2(550, 70), Vector2(550, 120), Vector2(550, 170), Vector2(550, 220),Vector2(550, 270),
    Vector2(600, 70), Vector2(600, 120), Vector2(600, 170), Vector2(600, 220),Vector2(600, 270),
    Vector2(650, 70), Vector2(650, 120), Vector2(650, 170), Vector2(650, 220),Vector2(650,270)
]
    
         
            self.obstacts = []
            self.bullets = []
            self.enemies = []
            self.lasers = []
            self.helps = []
            self.enemy_spawn()
            self.new_obs()
            self.resetting = False
     

    def update(self):
        if self.game_on:
            self.enemy_shooting()
            self.enemy_direct()
            self.shoot()
            self.collisions()
            self.player.update()
            self.assets()

            for enemy in self.enemies:
                enemy.update()

            if self.obstacts:
                for obs in self.obstacts:
                    obs.animation()
                    if not obs.dead:
                        obs.move_it()

            self.win_or_lose()
            if self.player.exploding:
                explo_player.play()
        
        if not self.game_on and not self.state:
            self.page()

        if not self.game_on and self.state:
            self.winner_or_loser()
        
        

pygame.init()
screen = pygame.display.set_mode((1000,650))
clock = pygame.time.Clock()

main = MAIN()

bg_img = pygame.image.load('img/bg.png')

Font = pygame.font.Font("font/Minecraft.ttf",60)
Font_40 = pygame.font.Font("font/Minecraft.ttf",40)
Font_20 = pygame.font.Font("font/Minecraft.ttf",20)

bullet_sound = pygame.mixer.Sound('sound/bullet.wav')
laser_sound = pygame.mixer.Sound('sound/laser.wav')
laser_sound.set_volume(0.7)
helps_sound = pygame.mixer.Sound('sound/PowerUp.wav')
explo_astro = pygame.mixer.Sound('sound/expl.wav')
explo_player = pygame.mixer.Sound('sound/explo.wav')
explo_enemy = pygame.mixer.Sound('sound/explos.wav')



NEW_OBS = pygame.USEREVENT
pygame.time.set_timer(NEW_OBS,5000)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == NEW_OBS and main.game_on:
            main.new_obs()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and main.game_on:
                main.player_shooting()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main.back.collidepoint(pygame.mouse.get_pos()):
                main.options = True
                main.button = 0
                main.state = None
                if main.resetting:
                    main.reset()



            if main.options:
                if main.playl.collidepoint(pygame.mouse.get_pos()):
                    main.button = 1
                    main.options = False
                if main.how_to.collidepoint(pygame.mouse.get_pos()):
                    main.button = 2
                    main.options = False
                if main.exit.collidepoint(pygame.mouse.get_pos()):
                    main.button = 3
      
    screen.blit(bg_img,(0,0))
    main.update()


    pygame.display.update()
    clock.tick(60)   