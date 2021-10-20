import Transformable

class UI(Transformable):
    def __init__(self,pos, image,layer=0):
        super().__init__(pos,image,layer)

    def moveTo(self, vec2Pos):
        #move to vec 2 pos *Overload
        pass
	
    def scaleTo(self, intScale):
        #scale the object with a pygame transform *Overload
        pass

    def rotateTo(self, floatRotation):
        #rotate object with pygame transform *Overload
        pass
