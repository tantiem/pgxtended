import Physical

class PhysicsBody(Physical):
    def __init__(self, pos, layer=0):
        super().__init__(pos,layer)