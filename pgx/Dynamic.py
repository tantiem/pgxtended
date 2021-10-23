from . import Transformable

#Inherit from Transformable. Moveable
#Overloads for a movement fashion that includes both camera relative movement, and movement by input.

class Dynamic(Transformable.Transformable):
    def __init__(self,pos,image, group=None,layer=0):
        super().__init__(pos, image, group, layer)

    #Overload the methods if needed