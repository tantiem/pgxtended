from . import Transformable
from pygame import math

#Inherit this class to make your own buttons with overridden OnClick methods.

class UI(Transformable.Transformable):
    def __init__(self,pos, image, group=None, layer=0):
        super().__init__(pos,image,group,layer)
        self.gPosition = math.Vector2(0,0)
        #UI doesn't move with the camera
        #Keep the localpos always low. Don't worry about global pos, it is unused.
    def MoveAbsolute(self, vec2Pos):
        #Inherited: self.localPos (Vector2) - Local position
        self.localPos = vec2Pos

    def MoveRelative(self, vec2Change):
        #Inherited: self.localPos (Vector2) - Local position
        self.localPos += vec2Change

    def CamAlign(self, cam):
        #Should already be aligned
        pass

    def OnClick(self):
        #Any function this button has
        #Overload this method in your own needs.
        raise NotImplementedError()
        pass