import pygame

#Global holders
#dictionaries, each key is a layer number that contains a list of objects to draw.
CamAffected = {} 
CamIndependent = {}

#You can put a bunch of init code, funcs, classes and vars in here to be accessed package wide.
def init():
    pygame.init()
