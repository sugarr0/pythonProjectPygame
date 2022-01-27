import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Hero(pygame.sprite.Sprite):
    image = load_image("download.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.score = 0
        self.add(players)
        self.image = Hero.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(750, 300, self.rect.width, self.rect.height)
        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(-2, 0)
        self.l = False
        self.r = False
        self.u = False
        self.d = False

    def update(self, arg, event, f=False):
        pl = pygame.sprite.spritecollideany(self, vertical_borders_l)
        pr = pygame.sprite.spritecollideany(self, vertical_borders_r)
        pu = pygame.sprite.spritecollideany(self, horizontal_borders_u)
        pd = pygame.sprite.spritecollideany(self, horizontal_borders_d)
        if (pl and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, vertical_borders_l)) and
            self.direction[0] < 0) or (
                pr and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, vertical_borders_r)) and
                self.direction[0] > 0) or (
                pu and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, horizontal_borders_u)) and
                self.direction[1] < 0) or (
                pd and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, horizontal_borders_d)) and
                self.direction[1] > 0):
            self.u = False
        else:
            if (arg == pygame.K_UP or self.u) and event == pygame.KEYDOWN:
                self.position += self.direction
                self.u = True
            elif arg == pygame.K_UP and event == pygame.KEYUP:
                self.u = False
        if (pl and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, vertical_borders_l)) and
            self.direction[0] > 0) or (
                pr and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, vertical_borders_r)) and
                self.direction[0] < 0) or (
                pu and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, horizontal_borders_u)) and
                self.direction[1] > 0) or (
                pd and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, horizontal_borders_d)) and
                self.direction[1] < 0):
            self.d = False
        else:
            if (arg == pygame.K_DOWN or self.d) and event == pygame.KEYDOWN:
                self.position -= self.direction
                self.d = True
            elif arg == pygame.K_DOWN and event == pygame.KEYUP:
                self.d = False
        if (arg == pygame.K_LEFT or self.l) and event == pygame.KEYDOWN:
            self.direction.rotate_ip(-1)
            self.l = True
        elif arg == pygame.K_LEFT and event == pygame.KEYUP:
            self.l = False
        if (arg == pygame.K_RIGHT or self.r) and event == pygame.KEYDOWN:
            self.direction.rotate_ip(1)
            self.r = True
        elif arg == pygame.K_RIGHT and event == pygame.KEYUP:
            self.r = False

        if arg == pygame.K_SPACE and event == pygame.KEYDOWN:
            Shot(shots, (self.rect.x, self.rect.y), self.direction.copy(), self.position.copy())

        angle = self.direction.angle_to(pygame.math.Vector2(1.5, 0))
        self.image = pygame.transform.rotate(Hero.image, angle)
        self.rect = self.image.get_rect(center=(round(self.position.x), round(self.position.y)))

        if f:
            self.image = Hero.image
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect = pygame.Rect(750, 300, self.rect.width, self.rect.height)
            self.position = pygame.math.Vector2(self.rect.center)
            self.direction = pygame.math.Vector2(-2, 0)
            self.l = False
            self.r = False
            self.u = False
            self.d = False

        font = pygame.font.Font(None, 24)
        text = font.render(str(self.score), True, (0, 0, 0))
        text_x = width - 30
        text_y = 20
        screen.blit(text, (text_x, text_y))

        # pygame.draw.rect(screen, pygame.Color(0, 0, 0),
        #                  pygame.Rect(self.rect.x, self.rect.y, self.rect.width + 3, self.rect.height + 3))


class Hero1(pygame.sprite.Sprite):
    image = load_image("download.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.score = 0
        self.add(players)
        self.image = Hero1.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(100, 300, self.rect.width, self.rect.height)
        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(2, 0)
        self.l = False
        self.r = False
        self.u = False
        self.d = False

    def update(self, arg, event, f=False):
        pl = pygame.sprite.spritecollideany(self, vertical_borders_l)
        pr = pygame.sprite.spritecollideany(self, vertical_borders_r)
        pu = pygame.sprite.spritecollideany(self, horizontal_borders_u)
        pd = pygame.sprite.spritecollideany(self, horizontal_borders_d)
        if (pl and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, vertical_borders_l)) and
            self.direction[0] < 0) or (
                pr and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, vertical_borders_r)) and
                self.direction[0] > 0) or (
                pu and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, horizontal_borders_u)) and
                self.direction[1] < 0) or (
                pd and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, horizontal_borders_d)) and
                self.direction[1] > 0):
            self.u = False
        else:
            if (arg == pygame.K_w or self.u) and event == pygame.KEYDOWN:
                self.position += self.direction
                self.u = True
            elif arg == pygame.K_w and event == pygame.KEYUP:
                self.u = False
        if (pl and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, vertical_borders_l)) and
            self.direction[0] > 0) or (
                pr and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, vertical_borders_r)) and
                self.direction[0] < 0) or (
                pu and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, horizontal_borders_u)) and
                self.direction[1] > 0) or (
                pd and pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, horizontal_borders_d)) and
                self.direction[1] < 0):
            self.d = False
        else:
            if (arg == pygame.K_s or self.d) and event == pygame.KEYDOWN:
                self.position -= self.direction
                self.d = True
            elif arg == pygame.K_s and event == pygame.KEYUP:
                self.d = False
        if (arg == pygame.K_a or self.l) and event == pygame.KEYDOWN:
            self.direction.rotate_ip(-1)
            self.l = True
        elif arg == pygame.K_a and event == pygame.KEYUP:
            self.l = False
        if (arg == pygame.K_d or self.r) and event == pygame.KEYDOWN:
            self.direction.rotate_ip(1)
            self.r = True
        elif arg == pygame.K_d and event == pygame.KEYUP:
            self.r = False

        if arg == pygame.K_e and event == pygame.KEYDOWN:
            Shot(shots, (self.rect.x, self.rect.y), self.direction.copy(), self.position.copy())

        angle = self.direction.angle_to(pygame.math.Vector2(1.5, 0))
        self.image = pygame.transform.rotate(Hero.image, angle)
        self.rect = self.image.get_rect(center=(round(self.position.x), round(self.position.y)))

        if f:
            self.image = Hero1.image
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect = pygame.Rect(100, 300, self.rect.width, self.rect.height)
            self.position = pygame.math.Vector2(self.rect.center)
            self.direction = pygame.math.Vector2(2, 0)
            self.l = False
            self.r = False
            self.u = False
            self.d = False

        font = pygame.font.Font(None, 24)
        text = font.render(str(self.score), True, (0, 0, 0))
        text_x = 70
        text_y = 20
        screen.blit(text, (text_x, text_y))
        # pygame.draw.rect(screen, pygame.Color(0, 0, 0),
        #                  pygame.Rect(self.rect.x, self.rect.y, self.rect.width + 3, self.rect.height + 3))


class Shot(pygame.sprite.Sprite):
    image = load_image("boll.png")

    def __init__(self, group, cords, v, p):
        super().__init__(group)
        self.direction = v
        self.position = p
        self.position += 24 * self.direction
        self.image = Shot.image
        self.mask = pygame.mask.from_surface(self.image)
        angle = self.direction.angle_to(pygame.math.Vector2(1, 0))
        self.image = pygame.transform.rotate(Shot.image, angle)
        self.rect = self.image.get_rect(center=(round(self.position.x), round(self.position.y)))

    def update(self):
        self.position += 1.4 * self.direction
        angle = self.direction.angle_to(pygame.math.Vector2(1, 0))
        self.image = pygame.transform.rotate(Shot.image, angle)
        self.rect = self.image.get_rect(center=(round(self.position.x), round(self.position.y)))

        if pygame.sprite.spritecollideany(self, horizontal_borders_d) or \
                pygame.sprite.spritecollideany(self, horizontal_borders_u):
            self.direction[1] = -self.direction[1]
        if pygame.sprite.spritecollideany(self, vertical_borders_l) or \
                pygame.sprite.spritecollideany(self, vertical_borders_r):
            self.direction[0] = -self.direction[0]

        if pygame.sprite.spritecollideany(self, players) and \
                pygame.sprite.collide_mask(self, pygame.sprite.spritecollideany(self, players)):
            if pygame.sprite.spritecollideany(self, players) == h:
                h1.score += 1
            elif pygame.sprite.spritecollideany(self, players) == h1:
                h.score += 1
            shots.empty()
            players.update(None, None, True)


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.image = pygame.Surface([x2 - x1, y2 - y1])
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
        if x2 - x1 != 1:
            Border(x1, y1, x1 + 1, y2).add(vertical_borders_r)
            Border(x2 - 1, y1, x2, y2).add(vertical_borders_l)
        elif x1 == 1 and x2 == 2:
            self.add(vertical_borders_l)
        elif x1 == width - 2 and x2 == width - 1:
            self.add(vertical_borders_r)
        if y2 - y1 != 1:
            Border(x1, y1, x2, y1 + 1).add(horizontal_borders_d)
            Border(x1, y2 - 1, x2, y2).add(horizontal_borders_u)
        elif y1 == 1 and y2 == 2:
            self.add(horizontal_borders_u)
        elif y1 == height - 2 and y2 == height - 1:
            self.add(horizontal_borders_d)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Герой')
    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)

    back = pygame.sprite.Sprite()
    im1 = load_image("back.png")
    im3 = load_image("back1.png")
    im2 = load_image("lavles.png")
    back.image = im1
    back.rect = back.image.get_rect()
    back.rect.x = 0
    back.rect.y = 0

    players = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(back)
    shots = pygame.sprite.Group()
    horizontal_borders_u = pygame.sprite.Group()
    horizontal_borders_d = pygame.sprite.Group()
    vertical_borders_r = pygame.sprite.Group()
    vertical_borders_l = pygame.sprite.Group()
    ex = pygame.sprite.Sprite()
    ex.image = load_image("exit.png")
    ex.rect = ex.image.get_rect()
    ex.rect.x = 10
    ex.rect.y = 10

    # h = Hero(all_sprites)
    # h1 = Hero1(all_sprites)

    # Border(1, 1, width - 2, 2)
    # Border(1, height - 2, width - 2, height - 1)
    # Border(1, 1, 2, height - 2)
    # Border(width - 2, 1, width - 1, height - 1)
    # Border(250, 100, width - 630, height - 100)
    # Border(width - 630, height - 120, width - 430, height - 100)
    # Border(630, 100, width - 250, height - 100)
    # Border(width - 450, 100, width - 250, 120)

    clock = pygame.time.Clock()
    ev = ''
    running = True
    while running:
        clock.tick(60)
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if len(all_sprites.sprites()) > 1 and (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP):
                ev = event.type
                players.update(event.key, event.type)
            if back.image == im1 and event.type == pygame.MOUSEBUTTONUP and \
                    pygame.Rect(235, 198, 425, 203).collidepoint(event.pos):
                back.image = im2
            elif back.image == im2 and event.type == pygame.MOUSEBUTTONUP and \
                    pygame.Rect(100, 220, 120, 120).collidepoint(event.pos):
                all_sprites.empty()
                h = Hero(all_sprites)
                h1 = Hero1(all_sprites)
                all_sprites.add(ex)
                Border(1, 1, width - 2, 2)
                Border(1, height - 2, width - 2, height - 1)
                Border(1, 1, 2, height - 2)
                Border(width - 2, 1, width - 1, height - 1)
                Border(250, 100, width - 630, height - 100)
                Border(width - 630, height - 120, width - 430, height - 100)
                Border(630, 100, width - 250, height - 100)
                Border(width - 450, 100, width - 250, 120)
            elif back.image == im2 and event.type == pygame.MOUSEBUTTONUP and \
                    pygame.Rect(390, 220, 120, 120).collidepoint(event.pos):
                all_sprites.empty()
                h = Hero(all_sprites)
                h1 = Hero1(all_sprites)
                all_sprites.add(ex)
                Border(1, 1, width - 2, 2)
                Border(1, height - 2, width - 2, height - 1)
                Border(1, 1, 2, height - 2)
                Border(width - 2, 1, width - 1, height - 1)
                Border(250, 1, width - 630, height - 100)
                Border(630, 100, width - 250, height - 1)
                Border(430, 100, 450, height - 100)
            elif back.image == im2 and event.type == pygame.MOUSEBUTTONUP and \
                    pygame.Rect(680, 220, 120, 120).collidepoint(event.pos):
                all_sprites.empty()
                h = Hero(all_sprites)
                h1 = Hero1(all_sprites)
                all_sprites.add(ex)
                Border(1, 1, width - 2, 2)
                Border(1, height - 2, width - 2, height - 1)
                Border(1, 1, 2, height - 2)
                Border(width - 2, 1, width - 1, height - 1)
                Border(630, 0, width - 250, height - 100)
                Border(1, 380, 200, 400)
                Border(180, 100, 200, 380)
            if len(all_sprites.sprites()) > 1 and event.type == pygame.MOUSEBUTTONUP and \
                    ex.rect.collidepoint(event.pos):
                all_sprites.empty()
                players.empty()
                shots.empty()
                horizontal_borders_u.empty()
                horizontal_borders_d.empty()
                vertical_borders_r.empty()
                vertical_borders_l.empty()
                all_sprites.add(back)
        players.update(None, pygame.KEYDOWN)
        shots.update()
        shots.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
