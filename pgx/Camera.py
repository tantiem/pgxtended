from . import Undrawable
from pygame import math
from pygame import transform
from pygame import surface

#local pos is always 0

class Camera(Undrawable.Undrawable):
    def __init__(self, pos, viewport, origin, camSurface):
        super().__init__(pos)
        #viewport: (private) tuple: Describes the height and width of the viewport 
        #origin: (private) tuple: Describes the origin of this camera
        #camSurface: (public) Surface: The surface that acts as this cameras view frustrum onto
        self._viewport = viewport
        self._origin = origin
        self.camSurface = camSurface

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

        pass

    def Clear(self):
        self.camSurface.fill((255,255,255))
