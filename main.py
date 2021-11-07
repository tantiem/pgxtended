#Helpful for starting a new pygame project.
#'Engine' boilerplate
import pygame
import pygame.locals as locs
import os.path
from pgx import *
import pgx
from pgx import pgxText
#You always pygame init. These are just the rules lol. pygame init will call init for all common processes, you can call extra 
#here if you want to.
pygame.init()
#End inits-----------------------------------------------------------------------
#Begin global variables----------------------------------------------------------

#Setting FPS is one way to keep track of delta time.
#Don't set this to lower than the screen's refresh rate.
FPS = 60
#Make a clock object to keep track of time.
FPSclock = pygame.time.Clock()


#Set the window size variables.
scrX = 1024
scrY = 768

#P_DISPLAY is what im naming a global constant surface object that we will use as the main display surface.
P_DISPLAY = pygame.display.set_mode((scrX, scrY))
#These other displays are made for our pgx Cameras.
screen = pygame.Surface((scrX,scrY))
screen2 = pygame.Surface((scrX,scrY))
ui_screen = pygame.Surface((scrX,scrY))

#These groups are helpful to keep track of masses of sprite objects.
G_SPR_MAP = pygame.sprite.Group()
G_SPR_UI = pygame.sprite.Group()

#You can choose whatever location for your images, this will just make a nice list from a folder
#images = [pygame.image.load(os.path.join("../images", x)).convert_alpha() for x in os.listdir("images")]

#convert alpha for only the png images. Do a straight convert for non transparent images.
#RESOURCE CREATION
img1 = pygame.image.load("giornoemoji.png").convert_alpha()
img2 = pygame.image.load("saucer.png").convert_alpha()

font1 = pygame.font.SysFont("comic-sans",100)
sometext = font1.render("Sug mah nootz",True,pygame.color.Color(50,50,50))

pgxObject.pgxObject

#The only way to utilize pgx UI is by making a new object that inherits the UI, because of the need to make custom
#functions per button. If I find a better way to do this I will change.
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
main_cam = Camera.Camera(pygame.math.Vector2(0,0),(scrX/2,scrY-100),(0,0),screen)
main_cam_2 = Camera.Camera(pygame.math.Vector2(0,0),(scrX/2,scrY-100),(scrX/2,0),screen2)
#This is the UI camera. It is cleared with a transparent background. Is not affected by the zoom of the main cam.
main_cam_ui = Camera.Camera(pygame.math.Vector2(0,0),(scrX,scrY),(0,0),ui_screen)
camSensitivity = 8

#OBJ CREATION
obj1 = Dynamic.Dynamic(pygame.math.Vector2(100,100),img2,G_SPR_MAP)
obj2a = Static.Static(pygame.math.Vector2(0,0),square2,G_SPR_MAP)
obj2b = Static.Static(pygame.math.Vector2(200,0),square2,G_SPR_MAP)
obj2c = Static.Static(pygame.math.Vector2(200,200),square2,G_SPR_MAP)
obj2d = Static.Static(pygame.math.Vector2(0,200),square2,G_SPR_MAP)
textobject = pgxText.Text(pygame.math.Vector2(100,100),'verdana',"AHHHHHHHhhHHHhHH!",100,G_SPR_MAP)


#SOUNDS
sound1 = AudioSource.AudioSource("Slash.wav",pygame.math.Vector2(0,0),True)

#Keep track of buttons how ever you want.
buttons = [newButton]

zoom = 1
running = True
while running:
    

    '''Get mouse positions'''
    screen_mouse_pos = pygame.mouse.get_pos() #Use this for interacting with UI
    global_mouse_pos_main_cam = main_cam.ScreenPosToGlobalPos(screen_mouse_pos) #Use this to interact with Non-UI Transformable

    '''Held down key input'''
    held_keys = pygame.key.get_pressed()

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
            if event.key == locs.K_SPACE:
                sound1.Play()
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
    main_cam_2.SetCamZoom(zoom,P_DISPLAY)
    main_cam_ui.SetCamZoom(1,P_DISPLAY)

    main_cam_2.Clear((255,255,255))
    main_cam.Clear((255,255,255)) #This means clear with a white background
    main_cam_ui.Clear() #This means clear with a transparent background

    '''Update stuff'''
    G_SPR_MAP.update(main_cam_2) #Updates any objects that want updating. Acts as the intro to an update frame.
    G_SPR_MAP.update(main_cam)
    G_SPR_UI.update(main_cam_ui)

    '''Updating done'''
    

    '''DrawStuff'''
    for spr in G_SPR_MAP:
        spr.Draw(main_cam)
        spr.Draw(main_cam_2)

    for spr in G_SPR_UI:
        spr.Draw(main_cam_ui)

    '''End of frame work.'''    
    pygame.display.flip() #This transfers all the surfaces written onto the pygame.display surface onto the actual window.
    FPSclock.tick(FPS) #Clocks the FPS counter.
else:
    pygame.quit()
