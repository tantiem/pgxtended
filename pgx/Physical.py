import Transformable

class Physical(Transformable):
    def __init__(self,pos,image,layer=0):
        super().__init__(pos,image,layer)

    def MoveTo(self, vec2Pos):
        #move to vec 2 pos *Overload
        pass
	
    def ScaleTo(self, intScale):
        #scale the object with a pygame transform *Overload
        pass

    def RotateTo(self, floatRotation):
        #rotate object with pygame transform *Overload
        pass