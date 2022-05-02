import pygame
import sys

pygame.init()
clock = pygame.time.Clock()


class Character:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 2
        # Damage resist
        self.res = .01
        # Attack
        self.atk = 2
        # Max health
        self.hmax = 10
        # current health
        self.hcurr = 10
        # Armor
        self.armor = 0
        # Magic Shield
        self.mshield = 0
        # Max Mana
        self.mmax = 1
        # current mana
        self.mcurr = 1


class Player(Character):
    def __init__(self):
        super(Player, self).__init__()
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.mouseL_pressed = False
        self.mouseM_pressed = False
        self.mouseR_pressed = False
        self.facing_right = True
        self.pos = (self.x, self.y)
        self.velX = 0
        self.velY = 0
        self.surf = pygame.transform.scale(pygame.image.load('imgs/Fisher Man 1 right.png').convert_alpha(),
                                           (screenx*.025, screeny*.08))
        self.rect = self.surf.get_rect(midbottom=(self.x, self.y))

    def draw(self, s):
        """Draws the player on the given screen"""
        s.blit(self.surf, self.rect)

    def update(self):
        """updates player movement"""
        self.velX = 0
        self.velY = 0

        if self.left_pressed and not self.right_pressed:
            if self.facing_right:
                self.surf = pygame.transform.flip(self.surf, True, False)
                self.facing_right = False
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            if not self.facing_right:
                self.surf = pygame.transform.flip(self.surf, True, False)
                self.facing_right = True
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY
        self.rect = pygame.Rect(self.x, self.y, 16, 32)


class Enemy(Character):
    def __init__(self):
        super(Enemy, self).__init__()


class Ui:
    def __init__(self):
        self.pos = (0, 0)
        self.rect = None

    def update(self):
        """Updates the ui object"""
        pass

    def draw(self, s):
        """Draws the object on the given screen"""
        pass


class Bar(Ui):
    def __init__(self):
        super(Bar, self).__init__()


class Loot:
    def __init__(self):
        self.atk = 0
        self.res = 0
        self.mshield = 0
        self.armor = 0
        self.mmax = 0
        self.hmax = 0
        self.iswearing = False

    def is_wearing(self, p):
        """Checks if Character passed as object is wearing this item if so it applies stats of item"""
        # Item's attributes
        b = list(self.__dict__.keys())
        # Player's attributes
        p = list(p.__dict__.keys())
        # Filtered list of attributes
        fl = filter(lambda z: z in b, p)

        # if wearing apply stats
        if self.iswearing:
            for x in fl:
                print(x)
        # if not don't apply stats
        else:
            pass


screen = pygame.display.set_mode((960, 540))
screenx, screeny = screen.get_size()

player = Player()
ui = Ui()
# Keeps the script running.
while __name__ == '__main__':
    # main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.right_pressed = True
            if event.key == pygame.K_w:
                player.up_pressed = True
            if event.key == pygame.K_s:
                player.down_pressed = True
            if event.key == pygame.K_SPACE:
                player.space_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.right_pressed = False
            if event.key == pygame.K_w:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.down_pressed = False
            if event.key == pygame.K_SPACE:
                player.space_pressed = False

        # Mouse Controls
        player.mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.mouseL_pressed = True
            if event.button == 2:
                player.mouseM_pressed = True
            if event.button == 3:
                player.mouseR_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                player.mouseL_pressed = False
            if event.button == 2:
                player.mouseM_pressed = False
            if event.button == 3:
                player.mouseR_pressed = False

    # event listeners
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.right_pressed = True
            if event.key == pygame.K_w:
                player.up_pressed = True
            if event.key == pygame.K_s:
                player.down_pressed = True
            if event.key == pygame.K_SPACE:
                player.space_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.right_pressed = False
            if event.key == pygame.K_w:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.down_pressed = False
            if event.key == pygame.K_SPACE:
                player.space_pressed = False

        # Mouse Controls
        player.mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.mouseL_pressed = True
            if event.button == 2:
                player.mouseM_pressed = True
            if event.button == 3:
                player.mouseR_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                player.mouseL_pressed = False
            if event.button == 2:
                player.mouseM_pressed = False
            if event.button == 3:
                player.mouseR_pressed = False

    player.draw(screen)
    ui.draw(screen)
    player.update()
    pygame.display.flip()

    # frame rate
    clock.tick(60)
