import Drawable

class Transformable(Drawable):
	def __init__(self,pos,layer=0):
		super().__init__(pos, layer)
		self._scale = 1
		self._rotation = 0.0

	def moveTo(self, vec2Pos):
		#move to vec 2 pos
		pass
	
	def scaleTo(self, intScale):
		#scale the object with a pygame transform
		pass

	def rotateTo(self, floatRotation):
		#rotate object with pygame transform
