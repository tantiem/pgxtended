import Physical

class PhysicsBody(Physical):
    def __init__(self, pos, image,layer=0):
        super().__init__(pos,image,layer)