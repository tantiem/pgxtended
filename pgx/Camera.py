from . import Undrawable
from pygame import math

#local pos is always 0

class Camera(Undrawable.Undrawable):
    def __init__(self, pos):
        super().__init__(pos)

    def SetCamPos(self, absolutePos):
        pass

    def MoveCam(self, relativePos):
        #Inherited: self.gPosition (Vector2) - Global position
        self.gPosition += relativePos

    def SetCamZoom(self, absoluteMultiplier):
        pass
