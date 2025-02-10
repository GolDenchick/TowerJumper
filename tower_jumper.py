import random

import pygame
from screeninfo import get_monitors

for monitor in get_monitors():
    monx = 1440
    mony = 900

pygame.init()

on_pls = 0

knight_x, knight_y = monx // 12 * 3, monx // 6
direction_k = 'l'
lose = False
menu = True
at = False
anim = 0
attack = 0
en_an = 0
clock = pygame.time.Clock()
jump_time = 0

bg = []
bg1 = []
bg2 = []
level = 0
finish = -mony * 5
upp = 0
a = 0

k = mony // 400

g = 2
speed_d = 0

game = True

pls = []
pls1 = []
pls2 = []

speed_up = 0

bolt = pygame.mixer.Sound('music/molniya-shumnyii-blizkii-aktivnyii.mp3')
rain = pygame.mixer.Sound('music/Lambert - Skye.mp3')
the_fall = pygame.mixer.Sound('music/padenie-chelovecheskogo-tela-effekt-eho-24216.mp3')
miss = pygame.mixer.Sound('music/promah-pri-boe-na-mechah.mp3')
mad_father = pygame.mixer.Sound('music/Old_Doll_-_Mad_Father_piano_cover_by_a_really_tired_turnip_boy_76768353.mp3')
gamemus = pygame.mixer.Sound('music/undertale_065. CORE.mp3')
mad_father.set_volume(0)
rain.set_volume(0)
gamemus.set_volume(0)
miss.set_volume(0.3)
step_count = 0
lol = monx / mony

knight_rect = pygame.transform.scale(pygame.image.load("sprites/knight/knight_rect.png"),
                                     ((monx // 10) // 32 * 17, (mony // 10 * lol) // 32 * 4))
knight_lose_rect = pygame.transform.scale(pygame.image.load("sprites/knight/knight_rect.png"),
                                     ((monx // 10) // 32 * 17, (mony // 10 * lol)))
enemy_rects = pygame.transform.scale(pygame.image.load("sprites/enemys/enemy_rect.png"),
                                     ((monx // 10) // 32 * 18, (mony // 10 * lol) // 32 * 20))
attack_rect = pygame.transform.scale(pygame.image.load("sprites/knight/knight_rect.png"),
                                     ((monx // 10) // 32 * 26, (mony // 10 * lol) // 32 * 28))

pl = pygame.transform.scale(pygame.image.load("sprites/bg/platform.png"), (monx // 10, mony // 10 * lol // 5))
pl1 = pygame.transform.scale(pygame.image.load("sprites/bg1/platform.png"), (monx // 10, mony // 10 * lol // 5))
pl2 = pygame.transform.scale(pygame.image.load("sprites/bg2/platform.png"), (monx // 10, mony // 10 * lol // 5))
screen = pygame.display.set_mode((monx, mony), pygame.FULLSCREEN)
stand_left = pygame.image.load(
    "sprites/knight/idol/left/knight_standing(left).png").convert_alpha()
stand_left = pygame.transform.scale(stand_left, (monx // 10, mony // 10 * lol))
stand_right = pygame.image.load(
    "sprites/knight/idol/right/knight_standing(right).png").convert_alpha()
stand_right = pygame.transform.scale(stand_right, (monx // 10, mony // 10 * lol))
fall_left = pygame.image.load(
    "sprites/knight/falling/left/knight_falling(left).png").convert_alpha()
fall_left = pygame.transform.scale(fall_left, (monx // 10, mony // 10 * lol))
fall_right = pygame.image.load(
    "sprites/knight/falling/right/knight_falling(right).png").convert_alpha()
fall_right = pygame.transform.scale(fall_right, (monx // 10, mony // 10 * lol))
escape_logo = pygame.image.load("sprites/escape.png").convert_alpha()
bg_s = []
bg_s1 = []
bg_s2 = []
walk_left = []
walk_right = []
attack_left = []
attack_right = []
logo = []
endlogo = []
logo_anim = 1
lose_anim = 1
enemy_l = []
enemy_r = []
enemy_list = []

for i in range(1, 5):
    enemy_l.append(pygame.transform.scale(pygame.image.load(f"sprites/enemys/eye/idol/left/pink_eye(left){i}.png"),
                                        (monx // 10, mony // 10 * lol)))
    enemy_l.append(pygame.transform.scale(pygame.image.load(f"sprites/enemys/eye/idol/left/pink_eye(left){i}.png"),
                                        (monx // 10, mony // 10 * lol)))
    enemy_r.append(pygame.transform.scale(pygame.image.load(f"sprites/enemys/eye/idol/right/pink_eye(right){i}.png"),
                                        (monx // 10, mony // 10 * lol)))
    enemy_r.append(pygame.transform.scale(pygame.image.load(f"sprites/enemys/eye/idol/right/pink_eye(right){i}.png"),
                                        (monx // 10, mony // 10 * lol)))
for i in range(1, 9):
    walk_left.append(pygame.transform.scale(pygame.image.load(f"sprites/knight/walk/left/knight_walking(left){i}.png"),
                                            (monx // 10, mony // 10 * lol)))
    walk_right.append(pygame.transform.scale(pygame.image.load(f"sprites/knight/walk/right/knight_walking(right){i}."
                                                               f"png"), (monx // 10, mony // 10 * lol)))
for i in range(1, 11):
    attack_left.append((pygame.transform.scale(pygame.image.load(f"sprites/knight/attack/left/knight_attack(left){i}."
                                                                 f"png"), (monx // 10, mony // 10 * lol))))
    attack_right.append((pygame.transform.scale(pygame.image.load(
        f"sprites/knight/attack/right/knight_attack(right){i}"
        f".png"), (monx // 10, mony // 10 * lol))))
    logo.append((pygame.transform.scale(pygame.image.load(f"sprites/logo/tower_jumper_logo{i}.png"),
                                        (monx, mony))))
for i in range(1, 8):
    bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{i}.png"),
                                       (monx // 10, mony // 10 * lol)))
    bg_s1.append(pygame.transform.scale(pygame.image.load(f"sprites/bg1/wall{i}.png"),
                                       (monx // 10, mony // 10 * lol)))
    bg_s2.append(pygame.transform.scale(pygame.image.load(f"sprites/bg2/wall{i}.png"),
                                       (monx // 10, mony // 10 * lol)))
for i in range(1, 6):
    endlogo.append((pygame.transform.scale(pygame.image.load(f"sprites/lose_screen/lose_screen{i}.png"),
                                           (monx, mony))))

bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{1}.png"), (monx // 10, mony // 10 * lol)))
bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{2}.png"), (monx // 10, mony // 10 * lol)))
bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{5}.png"), (monx // 10, mony // 10 * lol)))
bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{6}.png"), (monx // 10, mony // 10 * lol)))
bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{8}.png"), (monx // 10, mony // 10 * lol)))
bg_s1.append(pygame.transform.scale(pygame.image.load(f"sprites/bg1/wall{1}.png"), (monx // 10, mony // 10 * lol)))
bg_s1.append(pygame.transform.scale(pygame.image.load(f"sprites/bg1/wall{2}.png"), (monx // 10, mony // 10 * lol)))
bg_s1.append(pygame.transform.scale(pygame.image.load(f"sprites/bg1/wall{5}.png"), (monx // 10, mony // 10 * lol)))
bg_s1.append(pygame.transform.scale(pygame.image.load(f"sprites/bg1/wall{6}.png"), (monx // 10, mony // 10 * lol)))
bg_s1.append(pygame.transform.scale(pygame.image.load(f"sprites/bg1/wall{8}.png"), (monx // 10, mony // 10 * lol)))
bg_s2.append(pygame.transform.scale(pygame.image.load(f"sprites/bg2/wall{1}.png"), (monx // 10, mony // 10 * lol)))
bg_s2.append(pygame.transform.scale(pygame.image.load(f"sprites/bg2/wall{2}.png"), (monx // 10, mony // 10 * lol)))
bg_s2.append(pygame.transform.scale(pygame.image.load(f"sprites/bg2/wall{5}.png"), (monx // 10, mony // 10 * lol)))
bg_s2.append(pygame.transform.scale(pygame.image.load(f"sprites/bg2/wall{6}.png"), (monx // 10, mony // 10 * lol)))
bg_s2.append(pygame.transform.scale(pygame.image.load(f"sprites/bg2/wall{8}.png"), (monx // 10, mony // 10 * lol)))


class knight():
    def __init__(self, anim, attack):
        self.anim = anim
        self.attack = attack

    def move(self):
        global knight_x, direction_k, knight_y, upp, step_count, speed_up, on_pls, speed_d, k, menu,\
            jump_time, finish, level, lose, enemy_list

        if jump_time > 0 and jump_time < 12:
            jump_time += 1
        elif jump_time == 12:
            jump_time = 0

        finish += mony // 200 * a

        knight_y += mony // 200 * a

        if finish >= knight_y:
            finish = -mony * 5
            level += 1
            background.create_bagraund()
            knight_y = monx // 6

        if upp != 0:
            pass

        if direction_k == 'r':
            p_rect = knight_rect.get_rect(topleft=(knight_x + (monx // 10) // 32 * 3, knight_y
                                                   + (mony // 10 * lol) // 32 * 31))

        if direction_k == 'l':
            p_rect = knight_rect.get_rect(topleft=(knight_x + (monx // 10) // 32 * 12, knight_y
                                                   + (mony // 10 * lol) // 32 * 31))

        for z in range(len(pls)):
            if pls[z][3] == 1 and mony + 170 > pls[z][2] > -200:
                pl_rect = pls[z][0].get_rect(topleft=(pls[z][1], pls[z][2]))
                if p_rect.colliderect(pl_rect):
                    speed_d = 0
                    on_pls = 1

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (not keys[pygame.K_RIGHT] and not keys[pygame.K_d]):
            if knight_x > 0:
                knight_x -= monx // 10 // 6
            if not at:
                screen.blit(walk_left[self.anim], (knight_x, knight_y))
            direction_k = 'l'

        if (not keys[pygame.K_LEFT] and not keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            if knight_x < monx - monx // 10:
                knight_x += monx // 10 // 6
            if not at:
                screen.blit(walk_right[self.anim], (knight_x, knight_y))
            direction_k = 'r'

        if ((not keys[pygame.K_LEFT] and not keys[pygame.K_a] and not keys[pygame.K_RIGHT] and not keys[pygame.K_d]) or
                ((keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]))):
            step_count = -1
            if not at:
                if direction_k == 'l':
                    screen.blit(stand_left, (knight_x, knight_y))
                if direction_k == 'r':
                    screen.blit(stand_right, (knight_x, knight_y))

        if on_pls == 1 and knight_y > 0:
            k = mony // 400
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and jump_time == 0:
                jump_time += 1
                speed_up = mony // 30

        if on_pls == 0 and speed_up <= 0 and mony > knight_y:
            speed_d += g
            knight_y += speed_d
        on_pls = 0

        if speed_up > 0:
            if knight_y > 0:
                speed_up -= mony // 400
                knight_y -= speed_up
            else:
                speed_up = 0
        if knight_y > mony:
            menu = True
            lose = True
            level = 0
            knight_x, knight_y = monx // 12 * 3, monx // 6
            background.create_bagraund()
            enemy_list = []
    def attacking(self):
        global at, knight_x, knight_y, direction_k
        if keys[pygame.K_z] or keys[pygame.K_SPACE]:
            at = True


class background():
    def create_bagraund(self):
        global bg, pls
        bg = []
        pls = []
        for i in range(monx, -monx, round(-mony // 10 * lol)):
            for z in range(mony, -mony * 6, -monx // 10):
                f = random.randrange(1, 3)
                if level == 0:
                    bg.append((random.choice(bg_s), i, z))
                    if f == 1:
                        pls.append((pl, i, z, f))
                if level == 1:
                    bg.append((random.choice(bg_s1), i, z))
                    if f == 1:
                        pls.append((pl1, i, z, f))
                if level == 2:
                    bg.append((random.choice(bg_s2), i, z))
                    if f == 1:
                        pls.append((pl2, i, z, f))

    def bagraund(self):
        global bg, pls, a
        for i in range(len(bg)):
            if mony + 170 > bg[i][2] > -200:
                screen.blit(bg[i][0], (bg[i][1], bg[i][2]))
            bg[i] = [bg[i][0], bg[i][1], bg[i][2] + mony // 200 * a]
        for i in range(len(pls)):
            if pls[i][3] == 1 and mony + 170 > pls[i][2] > -200:
                screen.blit(pls[i][0], (pls[i][1], pls[i][2]))
            pls[i] = [pls[i][0], pls[i][1], pls[i][2] + mony // 200 * a, pls[i][3]]


class enemy():
    def enemy_list_delete(self):
        global enemy_list
        enemy_list = []

    def enemy_create(self):
        for i in range(monx, -monx, round(-mony // 10 * lol)):
            for z in range(mony, -mony * 22, -monx // 10):
                if level == 0:
                    f = random.randrange(1, 31)
                    if f == 1:
                        enemy_list.append((i, z, random.randrange(1, 3), f, 1))
                if level == 1:
                    f = random.randrange(1, 31)
                    if f == 1:
                        enemy_list.append((i, z, random.randrange(1, 3), f, 1))
                if level == 2:
                    f = random.randrange(1, 31)
                    if f == 1:
                        enemy_list.append((i, z, random.randrange(1, 3), f, 1))

    def enemy_blit(self):
        global en_an, lose, menu, enemy_rect, pk_rect, attack, rect_at
        en_an += 1
        if direction_k == 'r':
            pk_rect = knight_lose_rect.get_rect(topleft=(knight_x + (monx // 10) // 32 * 3, knight_y))
            if 2 < attack < 8:
                rect_at = attack_rect.get_rect(topleft=(knight_x + (monx // 10) // 32 * 16, knight_y))
            else:
                rect_at = attack_rect.get_rect(topleft=(- 1000, 0))

        if direction_k == 'l':
            pk_rect = knight_lose_rect.get_rect(topleft=(knight_x + (monx // 10) // 32 * 12, knight_y))
            if 2 < attack < 8:
                rect_at = attack_rect.get_rect(topleft=(knight_x - (monx // 10) // 32 * 6, knight_y))
            else:
                rect_at = attack_rect.get_rect(topleft=(- 1000, 0))
        if en_an == 8:
            en_an = 0

        for i in range(len(enemy_list)):
            if enemy_list[i][3] == 1 and mony > enemy_list[i][1] > round(-mony // 10 * lol) and enemy_list[i][4] == 1:
                if enemy_list[i][2] == 1:
                    screen.blit(enemy_l[en_an], (enemy_list[i][0], enemy_list[i][1]))
                    enemy_rect = enemy_rects.get_rect(topleft=(enemy_list[i][0],
                                                                   enemy_list[i][1] + (mony // 10 * lol) // 32 * 10))
                elif enemy_list[i][2] == 2:
                    screen.blit(enemy_r[en_an], (enemy_list[i][0], enemy_list[i][1]))
                    enemy_rect = enemy_rects.get_rect(topleft=(enemy_list[i][0],
                                                                   enemy_list[i][1] + (mony // 10 * lol) // 32 * 10))
                if pk_rect.colliderect(enemy_rect):
                    menu = True
                    lose = True
                if rect_at.colliderect(enemy_rect):
                    enemy_list[i] = (enemy_list[i][0], enemy_list[i][1], enemy_list[i][2], enemy_list[i][3], 0)

            enemy_list[i] = (enemy_list[i][0], enemy_list[i][1] + mony // 200 * a,
                             enemy_list[i][2], enemy_list[i][3], enemy_list[i][4])

ng = 0
rain.play(-1)
background = background()
enemy = enemy()
enemy.enemy_create()
background.create_bagraund()
while game:
    keys = pygame.key.get_pressed()
    screen.fill('black')
    if menu:
        if not lose:
            finish = -mony * 5
            knight_x, knight_y = monx // 12 * 3, monx // 6
            background.create_bagraund()
            level = 0
            if random.randint(1, 401) == 1:
                logo_anim = 1
            if logo_anim == 1:
                bolt.play()
            clock.tick(16)
            if logo_anim != 0 and logo_anim < 9:
                logo_anim += 1
            else:
                logo_anim = 0
            screen.blit(logo[logo_anim], (0, 0))
            if keys[pygame.K_SPACE]:
                gamemus.play(-1)
                menu = False
        else:
            speed_d = 0
            finish = -mony * 5
            knight_x, knight_y = monx // 12 * 3, monx // 6
            enemy.enemy_list_delete()
            enemy.enemy_create()
            background.create_bagraund()
            level = 0
            gamemus.stop()
            if lose_anim == 4:
                the_fall.play()
            if lose_anim == 1:
                mad_father.play()
            screen.blit(endlogo[lose_anim], (0, 0))
            if keys[pygame.K_ESCAPE]:
                rain.play(-1)
                mad_father.stop()
                lose = False
            if keys[pygame.K_SPACE]:
                mad_father.stop()
                gamemus.play(-1)
                menu = False
            if lose_anim != 0 and lose_anim < 4:
                lose_anim += 1
            else:
                lose_anim = 0
    else:
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        logo_anim = 1
        lose_anim = 1
        if finish >= 0:
            a = 0
        else:
            if knight_y < mony / 3 * 2 - (mony // 10 * lol // 2):
                a = mony / knight_y / 4
            else:
                a = 0
        rain.stop()
        bolt.stop()
        clock.tick(30)
        if anim == 7:
            anim = 0
        else:
            anim += 1

        knight_ = knight(anim, attack)

        background.bagraund()
        enemy.enemy_blit()

        knight_.move()

        if at:
            attack += 1
            if direction_k == 'l':
                screen.blit(attack_left[attack], (knight_x, knight_y))
            elif direction_k == 'r':
                screen.blit(attack_right[attack], (knight_x, knight_y))
        if attack == 1:
            miss.play()
        if attack == 9:
            attack = 0
            at = False

        knight_.attacking()
    screen.blit(escape_logo, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (keys[pygame.K_ESCAPE] and not lose) and logo_anim == 0) or level == 3:
            pygame.quit()
