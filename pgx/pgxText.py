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

    Attributes
    ----------
    self._font: (private) pygame.font.Font:
        A pygame font/sysfont object used for text rendering functionality.

    Methods
    -------
    ChangeText(text, antiAlias,color): text(string) antiAlias(bool) color(pygame.color.Color);
        Changes text string on text object.
    """
    def __init__(self,pos,fontName,text,size,group = None, layer = 0,color=color.Color(1,1,1),antiAlias=False,bold=False,italic=False):
        try:
            self._font = font.Font(fontName,size)
        except FileNotFoundError:
            if(font.match_font(fontName) is None):
                print(f"Couldn't find '{fontName}' as a custom font directory or a system font. Reverting to pygame default for {self.__str__}...")
            self._font = font.SysFont(fontName,size,bold,italic)

        fontSurface = self._font.render(text,antiAlias,color)
        super().__init__(pos, fontSurface, group, layer)

    def ChangeText(self,text,antiAlias=False,color=color.Color(1,1,1)):
        """
        Re-Render the font with different text.

        text: a string
        antiAlias: (OPTIONAL) bool whether or not text is AA'd
        color: (OPTIONAL) a pygame.Color or triple set describing a text color
        """
        self.image = self._font.render(text,antiAlias,color)

    #Overload the methods if needed