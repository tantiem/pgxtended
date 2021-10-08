import Physical

class Particle(Physical):
    def __init__(self, pos, layer=0):
        super().__init__(pos,layer)