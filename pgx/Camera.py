"""A module that controls all aspects of viewing the world using the pgx library."""
from . import Undrawable
from pygame import math
from pygame import transform
from pygame import surface

#local pos is always 0

#The Camera object is used as a special version of a plain surface. It's main purpose is to be a drawing surface for rendering
#the global game objects. You can stack multiple cameras to obtain functionality like split screen, UI, or whatever
#other funky biz you want.

#The global positions of all objects represent their rect in universe space and the position in universe space. Cameras
#have the job of drawing certain parts of global universe space within it's view frustrum based on it's own global position.

class Camera(Undrawable.Undrawable):
    """
    Inherits

    PGX: A class to control how a user views any instantiated pgx object types.

    pos:
        Vector2 position of the camera
    viewport:
        Width and height of cam
    origin:
        Where on the display the topleft of this cameras surface will be displayed
    camSurface:
        the surface to give to the camera initially
    ...

    Attributes
    ----------
    viewport:   (private) tuple: 
        Describes the height and width of the viewport 
    origin:     (private) tuple: 
        Describes the origin of this camera
    camSurface: (public) Surface: 
        The surface that acts as this cameras view frustrum onto
    zoom:       (private) Vector2: 
        The current camera zoom multiplier.

    Methods
    -------
    SetCamPos(absolutePos): absolutePos(Vector2);
        Sets the cameras global position, absolutely.

    MoveCam(relativePos): relativePos(Vector2);
        Sets the cameras global position, relatively.

    SetCamZoom(self, absoluteMultiplier, pygameDisplaySurface): absoluteMultiplier(float) pygameDisplaySurface(Surface)
        Zooms in or out on the cameras viewport.

    ScreenPosToGlobalPos(self,MousePos): MousePos(tuple);
        Returns: A pygame.math.Vector2 object representing the x and y coordinates of the adjusted mouse in units of
        global position measurement.
    """
    def __init__(self, pos, viewport, origin, camSurface):
        super().__init__(pos)
        
        self._viewport = viewport
        self._origin = origin
        self.camSurface = camSurface
        self._zoom = 1

    def SetCamPos(self, absolutePos):
        """
        Sets the cameras global position, absolutely

        absolutePos:    pygame.math.Vector2 object representing the new absolute position
        """
        #Inherited: self.gPosition (Vector2) - Global position
        self.gPosition = absolutePos

    def MoveCam(self, relativePos):
        """
        Sets the cameras global position, relatively

        relativePos:    pygame.math.Vector2 object representing the change in relative position
        """
        #Inherited: self.gPosition (Vector2) - Global position
        self.gPosition += relativePos

    def SetCamZoom(self, absoluteMultiplier, pygameDisplaySurface):
        """
        Transform scale the screen.
        Used to set the scale factor of the camera. Will zoom in and out based on topleft.
        Must be called every frame that the cameras zoom is not 1.

        abosluteMultiplier:     The absolute multiplier of the camera zoom.
        pygameDisplaySurface:   The pygame.display surface object representing the window.
        """
        if(absoluteMultiplier < 0):
            print(f"Attempted to set negative zoom on {self}")
            return

        #Set the new viewport size
        newViewportTuple = (int(self._viewport[0] * absoluteMultiplier),int(self._viewport[1] * absoluteMultiplier))
        #Create the new viewport surface
        newSurface = surface.Surface(newViewportTuple)
        newSurface.blit(self.camSurface, (0,0))
        
        pygameDisplaySurface.blit(transform.scale(self.camSurface,self._viewport),self._origin)
        self.camSurface = newSurface
        self._zoom = absoluteMultiplier

        pass

    def ScreenPosToGlobalPos(self,MousePos):
        """
        Returns: A pygame.math.Vector2 object representing the x and y coordinates of the adjusted mouse in units of
        global position measurement.
        For example: If there is an object whose topleft = (0,0), moving the camera around and hovering mouse over
        this top left area will return a value of (0,0), as that is the converted screen position to global position.

        MousePos:   Should just be the return value of pygame.mouse.get_pos(). Essentially, just a screen mouse position tuple.
        """
        
        return math.Vector2(MousePos[0] + (self.gPosition.x/self._zoom),MousePos[1] + (self.gPosition.y/self._zoom))

    def Clear(self,color,colorKey=None):
        """
        Clears the camera feed with a solid color;

        If colorKey is set, it will fill the screen with a color which is the same color as the color key,
        effectively laying a transparent mask fill. This is useful for things like UI elements.

        color:      pygame.color.Color object or triple set (,,)
        colorKey:   pygame.color.Color object or triple set (,,)
        """
        
        if(colorKey is not None):
            self.camSurface.set_colorkey(colorKey)
            self.camSurface.fill(colorKey)
        else:
            self.camSurface.fill(color)

