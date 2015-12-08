class Food(object):
	def __init__(self, name, color, recipe):
		self.name = name
		self.color = color
		self.recipe = recipe 
	def print_recipe(self):
		print self.recipe
apple = Food("apple","red", "cut apple")
applepie = Food("apple", "green", "bake pie at 350F")
apple.print_recipe()
applepie.print_recipe()
