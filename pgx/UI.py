from . import Transformable
from pygame import math

#Inherit this class to make your own buttons with overridden OnClick methods.

class UI(Transformable.Transformable):
    """
    Inherits Transformable

    A purely abstract subclass of Transformable. Inherit and overload  for your needs; maintains properties of other pgxObjects.

    pos:    Position of object in global space.
    image:  s.e;
    group:  (OPTIONAL) input a pygame.sprite.Group object to make this object a part of that group.
    layer:  Local layer for whatever camera object is being drawn on. Determines draw order
    ...

    Attributes
    ----------
    gPosition: (public) pygame.math.Vector2:
        see readme for more info on the PGX GPS.

    Methods
    -------
    OnClick();
        A method to call when button is clicked.
    """
    def __init__(self,pos, image, group=None, layer=0):
        super().__init__(pos,image,group,layer)
        self.gPosition = pos
        #UI doesn't move with the camera

    def OnClick(self):
        """
        Overload this method with custom functionality. Future delegate-like system in the works.
        """
        #Any function this button has
        #Overload this method in your own needs.
        raise NotImplementedError()