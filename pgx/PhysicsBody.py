from . import Physical

class PhysicsBody(Physical.Physical):
    def __init__(self, pos, image,group=None,layer=0):
        super().__init__(pos,image,group,layer)