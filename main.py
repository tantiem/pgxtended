#Helpful for starting a new pygame project.
#'Engine' boilerplate
import pygame
import pygame.locals as locs
import os.path
from pgx import *

pygame.init()

FPS = 60
FPSclock = pygame.time.Clock()

scrX = 1080
scrY = 720

P_DISPLAY = pygame.display.set_mode((scrX, scrY))
screen = pygame.Surface((scrX,scrY))

G_SPR_MAP = pygame.sprite.Group()
G_SPR_UI = pygame.sprite.Group()

#You can choose whatever location for your images, this will just make a nice list from a folder
#images = [pygame.image.load(os.path.join("../images", x)).convert_alpha() for x in os.listdir("images")]
img1 = pygame.image.load("giornoemoji.png").convert_alpha()

obj1 = Dynamic.Dynamic(pygame.math.Vector2(0,0),img1,G_SPR_MAP)

class Button(UI.UI):
    def __init__(self,pos,img,group=None,layer=0):
        super().__init__(pos,img,group,layer)

    def OnClick(self):
        print("clicked")

newButton = Button(pygame.math.Vector2(0,0),img1,G_SPR_UI)

main_cam = Camera.Camera(pygame.math.Vector2(0,0),(scrX,scrY),(0,0),screen)
camSensitivity = 2

buttons = [newButton]

zoom = 1
running = True
while running:
    
    '''Held down key input
    ALSO we are doing some neat camera movement right here specifically, acceleration and stuff so far.'''
    held_keys = pygame.key.get_pressed()
    mouse_pos = [pygame.mouse.get_pos()[0] + main_cam.gPosition.x, pygame.mouse.get_pos()[1] + main_cam.gPosition.y]

    if held_keys[pygame.K_UP] or held_keys[pygame.K_DOWN] or held_keys[pygame.K_RIGHT] or held_keys[pygame.K_LEFT]:

        if held_keys[pygame.K_UP]:
            main_cam.MoveCam(pygame.math.Vector2(0,-1) * camSensitivity)

        if held_keys[pygame.K_DOWN]:
            main_cam.MoveCam(pygame.math.Vector2(0,1) * camSensitivity)

        if held_keys[pygame.K_LEFT]:
            main_cam.MoveCam(pygame.math.Vector2(-1,0) * camSensitivity)

        if held_keys[pygame.K_RIGHT]:
            main_cam.MoveCam(pygame.math.Vector2(1,0) * camSensitivity)
    

    '''End Camera Movement'''
    '''Start input'''
    for event in pygame.event.get():
        if event.type == locs.QUIT:
            running = False
        if event.type == locs.KEYDOWN:
            '''Key Presses'''
            if event.key == locs.K_w:
                zoom += 1
            if event.key == locs.K_s:
                zoom -= 1
        if event.type == locs.MOUSEBUTTONDOWN:
            '''Mouse Cliques'''
            for button in buttons:
                if button.rect.collidepoint(mouse_pos):
                    button.OnClick()
        if event.type == locs.MOUSEMOTION:
            pass
            '''Mouse Movement'''
    '''While loop updates'''
    main_cam.SetCamZoom(zoom,P_DISPLAY)
    main_cam.Clear()
    '''DrawStuff'''
    pygame.draw.rect(main_cam.camSurface, (100,100,100), newButton.rect)
    G_SPR_MAP.update(main_cam)
    G_SPR_UI.update(main_cam)
    '''Updating done'''
    G_SPR_MAP.draw(main_cam.camSurface)
    G_SPR_UI.draw(main_cam.camSurface)
    
    pygame.display.flip()
    FPSclock.tick(FPS)
else:
    pygame.quit()
