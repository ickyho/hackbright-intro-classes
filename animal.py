class Animal(object):
	def __init__(self,name,color,texture, fur):
		self.name = name
		self.color = color
		self.texture = texture
		self.fur = fur
	def has_fur(self):
		print self.fur 
dog = Animal("Ruby","black","Soft", "True")
fish = Animal("Nemo","orange","scaly", "False")
dog.has_fur()
fish.has_fur()
