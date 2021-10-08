import Drawable

class Transformable(Drawable):
	def __init__(self,pos,layer=0):
		super().__init__(pos, layer)
		#_scale: (private) int: scale of the object. Usually 1. Modify only with methods, changing sprite transform can be wonky
		#_rotation: (private) float: rotation of the object. Usually 0. Modify only with methods, changing sprite transform can be wonky
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
		pass