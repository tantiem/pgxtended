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
    def __init__(self, pos, viewport, origin, camSurface):
        super().__init__(pos)
        #viewport: (private) tuple: Describes the height and width of the viewport 
        #origin: (private) tuple: Describes the origin of this camera
        #camSurface: (public) Surface: The surface that acts as this cameras view frustrum onto
        #zoom: (private) Vector2: The current camera zoom multiplier.
        self._viewport = viewport
        self._origin = origin
        self.camSurface = camSurface
        self._zoom = 1

    def SetCamPos(self, absolutePos):
        #Inherited: self.gPosition (Vector2) - Global position
        self.gPosition = absolutePos

    def MoveCam(self, relativePos):
        #Inherited: self.gPosition (Vector2) - Global position
        self.gPosition += relativePos

    def SetCamZoom(self, absoluteMultiplier, pygameDisplaySurface):
        if(absoluteMultiplier < 0):
            print(f"Attempted to set negative zoom on {self}")
            return
        #Transform scale the screen.
        #Used to set the scale factor of the camera. Will zoom in and out based on topleft.
        #If you want to zoom in on, say the center, simply move the camera at the same time as calling this;
        #i.e; zoom to 2x, move the camera half viewport length left and up.

        #Set the new viewport size
        newViewportTuple = (int(self._viewport[0] * absoluteMultiplier),int(self._viewport[1] * absoluteMultiplier))
        #Create the new viewport surface
        newSurface = surface.Surface(newViewportTuple)
        newSurface.blit(self.camSurface, (0,0))
        
        pygameDisplaySurface.blit(transform.scale(self.camSurface,self._viewport),self._origin)
        self.camSurface = newSurface
        self._zoom = absoluteMultiplier

        pass

    def GetLocalMousePos(self,globalMousePos):
        #Problems arise when trying to click on zoomed objects represented by this camera.
        #Therefore, it is necessary that when trying to click on a scaled object on a camera, to translate that spot due to zoom.
        #The position is offset by a scale of the calculated zoom.
        #So, to return the proper position, one must multiply the coordinates of the global mouse by the current zoom factor of this
        #camera.
        #Returns: A pygame.math.Vector2 object representing the x and y coordinates of the adjusted mouse in local space.
        return math.Vector2(globalMousePos.x*self._zoom,globalMousePos.y*self._zoom)

    def Clear(self,color=None):
        #Basically, if a color is set, it is a solid fill surface background color.
        #If a color is not set, the surface is set to be transparent. This is useful for things like UI
        #Or even post processing.
        if(color is None):
            self.camSurface.set_colorkey((0,0,0))
            self.camSurface.fill((0,0,0))
        else:
            self.camSurface.fill(color)

    def InRange(self, other):
		#Returns whether or not the other object is in range of this camera based on camera view.
        #self: A Camera object.
        #other: A pgxObject
        raise NotImplementedError()
