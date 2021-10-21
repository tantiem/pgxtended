#Helpful for starting a new pygame project.
import pygame
import pygame.locals as locs
import os.path
from pgx import *

pygame.init()

FPS = 60
FPSclock = pygame.time.Clock()

scrX = 1080
scrY = 720

screen = pygame.display.set_mode((scrX, scrY))

G_SPR_MAP = pygame.sprite.Group()
G_SPR_UI = pygame.sprite.Group()

#You can choose whatever location for your images, this will just make a nice dict from a folder
#images = [pygame.image.load(os.path.join("../images", x)).convert_alpha() for x in os.listdir("images")]
img1 = pygame.image.load("giornoemoji.png").convert_alpha()
#A basic camera operated with arrow keys/wasd
class Camera:

    def __init__(self, pos, sensitivity, max_accel, accel_rate):
        # x and y vector coordinates
        self.pos = pos
        self.sensitivity = sensitivity
        self.max_accel = max_accel
        self.acceleration = 1
        self.accel_rate = accel_rate


obj_count = 0
main_cam = Camera([0, 0], 10, 3, 1.1)
buttons = []
img_index = 0
static = False
#I originally made this compatible with UI, you can either salvage what I've got here or just start over lol.

running = True
while running:
    '''Held down key input
    ALSO we are doing some neat camera movement right here specifically, acceleration and stuff so far.'''
    held_keys = pygame.key.get_pressed()
    mouse_pos = [pygame.mouse.get_pos()[0] + main_cam.pos[0], pygame.mouse.get_pos()[1] + main_cam.pos[1]]
    camera_movement = main_cam.sensitivity * main_cam.acceleration

    if held_keys[pygame.K_UP] or held_keys[pygame.K_DOWN] or held_keys[pygame.K_RIGHT] or held_keys[pygame.K_LEFT]:
        if main_cam.acceleration <= main_cam.max_accel:
            main_cam.acceleration *= main_cam.accel_rate

        if held_keys[pygame.K_UP]:
            main_cam.pos[1] -= camera_movement

        if held_keys[pygame.K_DOWN]:
            main_cam.pos[1] += camera_movement

        if held_keys[pygame.K_LEFT]:
            main_cam.pos[0] -= camera_movement

        if held_keys[pygame.K_RIGHT]:
            main_cam.pos[0] += camera_movement

    elif main_cam.acceleration > 1:
        main_cam.acceleration /= main_cam.accel_rate
    '''End Camera Movement'''
    '''Start input'''
    for event in pygame.event.get():
        if event.type == locs.QUIT:
            running = False
        if event.type == locs.KEYDOWN:
            '''Key Presses'''
        if event.type == locs.MOUSEBUTTONDOWN:
            '''Mouse Cliques'''
            for button in buttons:
                if button.rect.collidepoint(mouse_pos):
                    button.DoAction()
        if event.type == locs.MOUSEMOTION:
            pass
            '''Mouse Movement'''
    '''While loop updates'''
    screen.fill((255, 255, 255))
    '''DrawStuff'''

    '''Updating done'''
    G_SPR_MAP.draw(screen)
    G_SPR_UI.draw(screen)
    pygame.display.flip()
    FPSclock.tick(FPS)
else:
    pygame.quit()
