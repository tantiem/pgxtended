from . import Transformable
from pygame import font
from pygame import color

#Inherit from Transformable. Moveable.
#Store pygame font rendering information and functionality.

class Text(Transformable.Transformable):
    """
    Store pygame font rendering information and functionality
    ...
    The constructor is a doozy. Controls everything about the font and text

    pos (Vector2): Vector2 topleft position
    fontName (str, union sys.path): name of the font to look for. Will look for a custom font first, then default to sys file, then to pygame default.
    text (str): text you want it to display
    size (int): size in pixels, the height of the letters.
    group (pygame.sprite.Group): (OPTIONAL) a python sprite group.
    layer (int): (OPTIONAL) default = 0. Order to draw.
    color (pygame.color.Color): (OPTIONAL) default = black.
    antiAlias (bool): (OPTIONAL) default = false. Anti alias text rendering.
    bold (bool): (OPTIONAL) default = false. s.e;
    italic (bool): (OPTIONAL) default = false. s.e;
    """
    def __init__(self,pos,fontName,text,size,group = None, layer = 0,color=color.Color(1,1,1),antiAlias=False,bold=False,italic=False):
        if(font.match_font(fontName) is not None):
            self._font = font.Font(fontName,size)
        else:
            self._font = font.SysFont(fontName,size,bold,italic)
        fontSurface = self._font.render(text,antiAlias,color)
        super().__init__(pos, fontSurface, group, layer)

    def ChangeText(self,text,antiAlias=False,color=color.Color(1,1,1)):
        self.image = self._font.render(text,antiAlias,color)

    #Overload the methods if needed