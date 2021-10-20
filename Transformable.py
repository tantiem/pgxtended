import Drawable

class Transformable(Drawable):
	def __init__(self,pos,image,layer=0):
		super().__init__(pos, image, layer)
		#_scale: (private) int: scale of the object. Usually 1. Modify only with methods, changing sprite transform can be wonky
		#_rotation: (private) float: rotation of the object. Usually 0. Modify only with methods, changing sprite transform can be wonky
		self._scale = 1
		self._rotation = 0.0

	def MoveTo(self, vec2Pos):
		#move to vec 2 pos, relatively
		pass
	
	def ScaleTo(self, intScale):
		#scale the object with a pygame transform, absolutely
		pass

	def RotateTo(self, floatRotation):
		#rotate object with pygame transform, absolutely
		pass

	def CamAlign(self, cam):
		#set position based on cam position
		#This probably does not need to be overloaded
		
		pass