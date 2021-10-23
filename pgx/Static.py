from . import Transformable

#Inherit from Transformable. Static
#Overloads for a movement fashion regardless of a camera. 

class Static(Transformable.Transformable):
    def __init__(self,pos, image, group=None, layer=0):
        super().__init__(pos, image, group, layer)

    #Overload the methods if needed
