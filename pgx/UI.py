from . import Transformable
from pygame import math

#Inherit this class to make your own buttons with overridden OnClick methods.

class UI(Transformable.Transformable):
    def __init__(self,pos, image, group=None, layer=0):
        super().__init__(pos,image,group,layer)
        self.gPosition = pos
        #UI doesn't move with the camera
    def MoveAbsolute(self, vec2Pos):
        #Inherited: self.localPos (Vector2) - Local position
        self.gPosition = vec2Pos

    def MoveRelative(self, vec2Change):
        #Inherited: self.localPos (Vector2) - Local position
        self.gPosition += vec2Change

    def GetCamAlignPos(self, cam):
        #Due to update (11/2/2021), all this needs to do is return the global position.
        return self.gPosition

    def OnClick(self):
        #Any function this button has
        #Overload this method in your own needs.
        raise NotImplementedError()