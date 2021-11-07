from . import Drawable
from pygame import rect
from pygame import transform
from pygame import math


class Transformable(Drawable.Drawable):
	"""
	Inherits Drawable

	The main parent class to all functional subtype drawn objects. Contains functionality for scaling, rotating, and moving
	drawn objects.

	pos:	s.e;
	image:	pygame.Surface object; any surface.
	group:	(OPTIONAL) pygame.sprite.Group object to belong to.
	layer:	(OPTIONAL) local draw layer.
	...

	Attributes
	----------
	name: (intended protection) type:
	    tabbed in description
	scale: (private) float:
		the current scale of this transformable object
	rotation: (private) float:
		the current rotation of this transformable object
	baseSize: (private) Vector2:
		used to keep track of the base size of this object to be used with scaling.

	Methods
	-------
	MethodName(param1, param2="foobar"): param1(int) param2(string);
	    short desc of method
	"""
	def __init__(self,pos,image, group=None, layer=0):
		super().__init__(pos, image, group, layer)
		#_scale: (private) int: scale of the object. Usually 1. Modify only with methods, changing sprite transform can be wonky
		#_rotation: (private) float: rotation of the object. Usually 0. Modify only with methods, changing sprite transform can be wonky
		#_baseSize: (private) Vector2: s.e; base size of object. Don't change this directly, unless you like headaches!
		self._scale = 1
		self._rotation = 0.0
		self._baseSize = math.Vector2(self.rect.width,self.rect.height)

	def MoveAbsolute(self, vec2Pos):
		"""
		Changes the global position, absolutely.

		vec2Change: pygame.math.Vector2 object representing new position
		"""
		self.gPosition = vec2Pos

	def MoveRelative(self, vec2Change):
		"""
		Changes the global position, relatively.

		vec2Change: pygame.math.Vector2 object representing position change
		"""
		
		self.gPosition += vec2Change
	
	def ScaleTo(self, floatScale):
		"""
		scale the object with a pygame transform, absolutely

		floatScale: float amount to scale
		"""
		if floatScale > 0:
			self._scale = floatScale
			self.image = transform.scale(self.image,(self._baseSize.x * floatScale, self._baseSize.y * floatScale))
		else:
			print("Trying to set an invalid scale! (<= 0)")
		

	def RotateTo(self, floatRotation):
		"""
		rotate object with pygame transform, absolutely
		Positive values are counter clockwise.

		floatRotation: float amount of rotation to set for this object.
		"""
		
		deltaRotation = (floatRotation % 360) - self._rotation
		self.Rotate(deltaRotation)

	def Rotate(self, deltaRotation):
		"""
		Use pygame.transform.rotate to additively rotate the surface.
		keeps track of current rotation.
		positive values are counter clockwise.

		deltaRotation: float amount to rotate
		"""
		self.image = transform.rotate(self.image,deltaRotation)
		self._rotation += deltaRotation
		if(self._rotation > 360 or self._rotation < -360):
			self._rotation %= 360

	def Update(self, cam):
		"""
		Makes sure that the rect object is updated for 'collision' purposes.
		Can be overridden.

		cam: vestigial at this point.

		"""
		self.rect.update(self.gPosition.x,self.gPosition.y,self.rect.width,self.rect.height)

	def GetRotation(self):
		"""Returns the value of the protected rotation member"""
		return self._rotation

	def GetScale(self):
		"""Returns the value of the protected scale member"""
		return self._scale

	def GetBaseSize(self):
		"""Returns the value of the protected base size member"""
		return self._baseSize