import pgObject

class Drawable(pgOjbect):
	def __init__(self, pos, layer=0):
		super().__init__(pos)
		self.localLayer = layer

	def draw(self):
		#draw
		pass
