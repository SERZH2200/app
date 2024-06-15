import pygame
import sys
from time import sleep


pygame.init()
window = pygame.display.set_mode((800,450))
game_over = pygame.transform.scale(pygame.image.load('game_over2.jpg'),(800, 450))
u_win_pic = pygame.transform.scale(pygame.image.load('u_win.png'),(800, 450))
background = pygame.transform.scale(pygame.image.load('background.jpg'),(800, 450))
player_jump = pygame.transform.scale(pygame.image.load('hero_jump.png'),(115, 110))
player_run = pygame.transform.scale(pygame.image.load('hero_run.png'),(100, 100))
player_default = pygame.transform.scale(pygame.image.load('hero.png'),(100, 100))
player_shoot = pygame.transform.scale(pygame.image.load('hero_shoot.png'),(120, 112))
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.w = w
        self.image = pygame.transform.scale(pygame.image.load(image),(self.w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(Sprite):
    def __init__(self, image, x, y, w, h, speed_v, speed_h):
        Sprite.__init__(self, image, x, y, w, h)
        self.speed_v = speed_v
        self.speed_h = speed_h
    def update(self):
        self.rect.x += self.speed_h
        self.rect.y += self.speed_v
'''class Enemy(Sprite):
    def __init__(self, image, x, y, w, h, speed):
        Sprite.__init__(self, image, x, y, w, h)
        self.speed = speed
    def update(self):'''
boy_with_gun = Sprite(image = 'boy_gun.png', x = 0, y = 140, w = 165 / 1.65, h = 227 / 2.27)
platform_4 = Sprite(image = 'brick.png', x = 0, y = 238, w = 880 / 8, h = 294 / 8)
platform_h = Player(image = 'brick2.png', x = 360, y = 257, w = 880 / 12, h = 294 / 16, speed_h = 0, speed_v = 0)
platform_h2 = Sprite(image = 'brick.png', x = 552, y = 404, w = 880 / 4, h = 294 / 8)
'''platform_v = Sprite(image = 'brick_v.png', x = 360, y = 272, w = 282 / 6, h = 844 / 5)'''
platform_3 = Sprite(image = 'brick_v.png', x = 219, y = 272, w = 282 / 6, h = 844 / 5)
player = Player(image = 'hero.png', x = 5, y = 305, w = 500 / 5, h = 500 / 5, speed_v = 0, speed_h = 0)
enemy = Player(image = 'enemy.png', x = 542, y = 305, w = 550 / 5, h = 530 / 5, speed_v = 0, speed_h = 0)
floor = Sprite(image = 'brick.png', x = 0, y = 404, w = 880 / 4, h = 294 / 8)
bullet_2 = Player(image = 'bullet.png', x = boy_with_gun.rect.left + 50, y = boy_with_gun.rect.top + 53, w = 640/60, h = 1200/120, speed_v = 0, speed_h = 0)
bullet_2.image = pygame.transform.rotate(bullet_2.image, 270)
shoot = False
shoot1 = False
shoot2 = False
shoot3 = False
jump = False
u_lose = False
u_win = False
boy_with_gunshoot = False
jump_h = 50
enemy.image = pygame.transform.flip(enemy.image, flip_x = True, flip_y = False)
player_left = False
player_right = True
barriers = pygame.sprite.Group()
hor_barriers = pygame.sprite.Group()
floors = [floor, platform_h, platform_3, platform_4, platform_h2]
for floor_ in floors:
    hor_barriers.add(floor_)
i = 1
while True:
    level1 = True
    if enemy.rect.x in range(540, 544):
        enemy.speed_h = 2
    elif enemy.rect.x in range(750, 760):
        enemy.speed_h = -2
    if pygame.sprite.collide_rect(bullet_2, player):
        shoot1 = True
        u_lose = True
    if boy_with_gunshoot == False and bullet_2.rect.x in range(40,800):
        bullet_2.speed_h = 5
        boy_with_gunshoot = True
    if bullet_2.rect.x > 800 and shoot3 == False:
        bullet_2.rect.x = boy_with_gun.rect.left + 50
    if platform_h.rect.x in range(360, 365):
        platform_h.speed_h = 10
    elif platform_h.rect.x in range(650, 665):
        platform_h.speed_h = -10
    for abc in floors:
        if pygame.sprite.collide_rect(abc, player) and player.rect.top in range(abc.rect.bottom - 40, abc.rect.bottom):
            player.rect.top = abc.rect.bottom
        if pygame.sprite.collide_rect(abc, player) and player.rect.bottom in range(abc.rect.top - 36, abc.rect.top + 36):
            player.rect.bottom = abc.rect.top
        if pygame.sprite.collide_rect(abc, player) and player.rect.right in range(abc.rect.left - 10, abc.rect.left + 10):
            player.rect.x -= 5
        if pygame.sprite.collide_rect(abc, player) and player.rect.left in range(abc.rect.right - 10, abc.rect.right + 10):
            player.rect.x += 5
    if player.rect.bottom > 450:
        u_lose = True
    if u_lose == False:
        window.blit(background, (0, 0))
        '''barriers.draw(window)'''#по-моему это тут не надо
        if shoot3 == False:
            boy_with_gun.reset()
        platform_h.update()
        platform_h.reset()
        hor_barriers.draw(window)
        if shoot1 == False and u_lose == False:
            player.reset()
        if shoot2 == False:
            enemy.update()
            enemy.reset()
        bullet_2.reset()
        bullet_2.update()
    else:
        window.blit(game_over, (0, 0))
    try:
        if not pygame.sprite.spritecollide(bullet, hor_barriers, False):
            bullet.update()
            bullet.reset()
    except:
        pass
    if shoot2 == True and shoot3 == True:
        window.blit(u_win_pic, (0, 0))
        level1 = False
    if jump == True:#
        player.image = player_jump
        player.rect.y += jump_speed
        jump_speed += 5
        if player_left == True:
                player.image = pygame.transform.flip(player.image, flip_x = True, flip_y = False)#
    if not pygame.sprite.spritecollide(player,hor_barriers, False):
        player.rect.y += 10#тут поменял 5 на 10
        jump = True
    else:
        jump = False
    '''for wall in pygame.sprite.spritecollide(player, barriers, False):
        if player.rect.right > wall.rect.left:
            player.rect.x -= 6#'''
    for floor_ in pygame.sprite.spritecollide(player, hor_barriers, False):#тут поменял барьерс на хор_барьерс
        if player.rect.bottom < floor_.rect.top:
                player.rect.y += 10# что мы делаем тут?
        else:
            jump = False
            player.image = player_default
            jump_speed = 0#
            if player_left == True:
                player.image = pygame.transform.flip(player.image, flip_x = True, flip_y = False)
    if shoot == True:
        if player_left == True:
            player.image = pygame.transform.flip(player_shoot, flip_x = True, flip_y = False)
        else:
            player.image = player_shoot
    if pygame.sprite.collide_rect(platform_h, player):
        player.speed_h = platform_h.speed_h
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                shoot = True
                if player_left == True:
                    bullet = Player(image = 'bullet.png', x = player.rect.left + 50, y = player.rect.top + 40, w = 640/60, h = 1200/120, speed_v = 0, speed_h = -20)
                else:
                    player.image = player_shoot
                    bullet = Player(image = 'bullet.png', x = player.rect.left + 50, y = player.rect.top + 40, w = 640/60, h = 1200/120, speed_v = 0, speed_h = 20)
                bullet.image = pygame.transform.rotate(bullet.image, 270)
        if event.type == pygame.MOUSEBUTTONUP:
            shoot = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jump == False:
                jump = True
                jump_speed = -jump_h
            if event.key == pygame.K_w:
                player.speed_v = 0
            if event.key == pygame.K_s:
                player.speed_v = 0
            if event.key == pygame.K_d:
                player.speed_h = 5
                player_left = False
                player_right = True
            if event.key == pygame.K_a:
                player.speed_h = -5
                player_left = True
                player_right = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and jump == True:
                '''jump_speed = 0'''
            if event.key == pygame.K_w:
                player.speed_v = 0
            if event.key == pygame.K_w:
                player.speed_v = 0
            if event.key == pygame.K_s:
                player.speed_v = 0
            if event.key == pygame.K_d:
                player.speed_h = 0
                player_left = False
                player_right = True
            if event.key == pygame.K_a:
                player.speed_h = 0
                player_left = True
                player_right = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            print(x, y)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    try:
        if pygame.sprite.collide_rect(bullet, enemy):
            shoot2 = True
    except:
        pass
    try:
        if pygame.sprite.collide_rect(bullet, boy_with_gun):
            shoot3 = True
    except:
        pass
    if pygame.sprite.collide_rect(player, enemy) and player.rect.bottom in range(enemy.rect.top + 30, enemy.rect.top):
        player.rect.bottom = enemy.rect.top
    if pygame.sprite.collide_rect(player, enemy) and player.rect.right in range(enemy.rect.left - 30, enemy.rect.left):
        player.rect.right = enemy.rect.left
    if pygame.sprite.collide_rect(player, enemy) and player.rect.left in range(enemy.rect.right + 30, enemy.rect.right):
        player.rect.left = enemy.rect.right
    '''if level1 == False:'''
    player.update()
    pygame.display.update()
    pygame.time.delay(50)