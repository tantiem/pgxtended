from . import Transformable

class Physical(Transformable.Transformable):
    def __init__(self,pos,image,group=None,layer=0):
        super().__init__(pos,image,group,layer)

    #Overload methods if needed