import pygame
from random import *

#define the class of small enemy
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy1_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)

#define the class of mid enemy
class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy2_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy2_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down4.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-10 * self.height, -self.height)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-10 * self.height, -self.height)


#define the class of big enemy
class BigEnemy(pygame.sprite.Sprite):
    energy = 20
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy3_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down4.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down5.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down6.png").convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-15 * self.height, -5 * self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-15 * self.height, -5 * self.height)

#define the class of boss
class Boss(pygame.sprite.Sprite):
    energy = 100
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/boss_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/boss_n2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/boss_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/boss_down1.png").convert_alpha(), \
            pygame.image.load("images/boss_down2.png").convert_alpha(), \
            pygame.image.load("images/boss_down3.png").convert_alpha(), \
            pygame.image.load("images/boss_down4.png").convert_alpha(), \
            pygame.image.load("images/boss_down5.png").convert_alpha(), \
            pygame.image.load("images/boss_down6.png").convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speedv = 0.5
        self.speedh = 1
        self.active = True
        self.rect.left, self.rect.top = 120, -95
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = Boss.energy
        self.hit = False
        self.boss_to_left = False
        self.boss_to_right = False
        self.boss_to_bottom = False
        self.boss_timer = 500

    def move(self):
        #Boss come down to the top of the screen
        #Boss come down to the bottom of the screen and attack every 5 seconds
        if self.boss_timer > 0:
            if self.rect.top < 0:
                self.rect.top += self.speedv
                self.boss_timer -= 1
            elif self.rect.top >= 0:
                self.speedv = 0
                self.boss_timer -= 1
        elif self.boss_timer <= 0:
            if self.rect.top >= 0 and self.rect.top < 605 and self.boss_to_bottom == False:
                self.rect.top += 3
                if self.rect.top >= 605:
                    self.boss_to_bottom = True
            elif self.rect.top >= 605 or self.boss_to_bottom == True:
                self.rect.top -= 3
                if self.rect.top < 0:
                    self.boss_timer = randint(1,6)*100
                    self.boss_to_bottom = False
                    self.speedv = 0.5
                
            
        
        #Boss move left and right
        if self.rect.left <= 0:
            self.rect.left += self.speedh
            self.boss_to_left = True
            self.boss_to_right = False
        elif self.rect.left > 0 and self.rect.left < 240 and self.boss_to_left == False and self.boss_to_right == False:
            self.rect.left += self.speedh
        elif self.rect.left > 0 and self.rect.left < 240 and self.boss_to_left == True and self.boss_to_right == False:
            self.rect.left += self.speedh
        elif self.rect.left > 0 and self.rect.left < 240 and self.boss_to_left == False and self.boss_to_right == True:
            self.rect.left -= self.speedh    
        elif self.rect.left > 0 and self.rect.left < 240 and self.boss_to_left == True and self.boss_to_right == True:
            self.rect.left -= self.speedh
            self.boss_to_left = False
            self.boss_to_right = False
        elif self.rect.left >= 240:
            self.rect.left -= self.speedh
            self.boss_to_left = False
            self.boss_to_right = True
            
        else:
            self.reset()

        

    def reset(self):
        self.active = True
        self.energy = Boss.energy
        self.rect.left, self.rect.top = 120, 0