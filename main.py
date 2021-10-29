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
ui_screen = pygame.Surface((scrX,scrY))

G_SPR_MAP = pygame.sprite.Group()
G_SPR_UI = pygame.sprite.Group()

#You can choose whatever location for your images, this will just make a nice list from a folder
#images = [pygame.image.load(os.path.join("../images", x)).convert_alpha() for x in os.listdir("images")]

#convert alpha for only the png images. Do a straight convert for non transparent images.
#RESOURCE CREATION
img1 = pygame.image.load("giornoemoji.png").convert_alpha()
img2 = pygame.image.load("saucer.png").convert_alpha()



class Button(UI.UI):
    def __init__(self,pos,img,group=None,layer=0):
        super().__init__(pos,img,group,layer)

    def OnClick(self):
        print("clicked")

#If you want to make a placeholder, images are all in fact, surfaces. So just do soemthing like this:
square1 = pygame.surface.Surface((200,100))
square1.fill((50,200,100))

square2 = pygame.surface.Surface((50,50))
square2.fill((56,50,20))
#Now you can use this as an image.

#UI CREATION
newButton = Button(pygame.math.Vector2(0,scrY-square1.get_rect().height),square1,G_SPR_UI)

#CAMERA CREATION
#This is my main camera surface. Draw most of the game here.
main_cam = Camera.Camera(pygame.math.Vector2(0,0),(scrX,scrY),(0,0),screen)
#This is the UI camera. It is cleared with a transparent background. Is not affected by the zoom of the main cam.
main_cam_ui = Camera.Camera(pygame.math.Vector2(0,0),(scrX,scrY),(0,0),ui_screen)
camSensitivity = 8

#OBJ CREATION
obj1 = Dynamic.Dynamic(pygame.math.Vector2(100,100),img2,G_SPR_MAP)
obj2a = Static.Static(pygame.math.Vector2(0,0),square2,G_SPR_MAP)
obj2b = Static.Static(pygame.math.Vector2(200,0),square2,G_SPR_MAP)
obj2c = Static.Static(pygame.math.Vector2(200,200),square2,G_SPR_MAP)
obj2d = Static.Static(pygame.math.Vector2(0,200),square2,G_SPR_MAP)

buttons = [newButton]

zoom = 0.5
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
    plSpeed = 5
    if held_keys[pygame.K_w]:
        obj1.MoveRelative(pygame.math.Vector2(0,-plSpeed))
    if held_keys[pygame.K_s]:
        obj1.MoveRelative(pygame.math.Vector2(0,plSpeed))
    if held_keys[pygame.K_a]:
        obj1.MoveRelative(pygame.math.Vector2(-plSpeed,0))
    if held_keys[pygame.K_d]:
        obj1.MoveRelative(pygame.math.Vector2(plSpeed,0))

    for event in pygame.event.get():
        if event.type == locs.QUIT:
            running = False
        if event.type == locs.KEYDOWN:
            '''Key Presses'''
            #if event.key == locs.K_w:
        if event.type == locs.MOUSEBUTTONDOWN:
            '''Mouse Cliques'''
            for button in buttons:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    button.OnClick()
        if event.type == locs.MOUSEMOTION:
            pass
            '''Mouse Movement'''
    '''While loop updates'''
    main_cam.SetCamZoom(zoom,P_DISPLAY)
    main_cam_ui.SetCamZoom(1,P_DISPLAY)
    main_cam.Clear((255,255,255))
    main_cam_ui.Clear()
    '''DrawStuff'''
    G_SPR_MAP.update(main_cam)
    G_SPR_UI.update(main_cam_ui)
    '''Updating done'''
    G_SPR_MAP.draw(main_cam.camSurface)
    G_SPR_UI.draw(main_cam_ui.camSurface)
    
    pygame.display.flip()
    FPSclock.tick(FPS)
else:
    pygame.quit()
