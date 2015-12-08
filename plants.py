class Plant(object):
	def __init__(self,age,color,season):
		self.age = age
		self.color = color
		self.season = season

	def set_is_flowering(self, season):
		if(self.age>2 and self.season == "spring"):
			print True
		else:
			print False
sunflower = Plant(2, "yellow", "Summer")
daisy = Plant(1, "white", "Spring")
tulips = Plant(3, "red", "spring")
sunflower.set_is_flowering(bool)
daisy.set_is_flowering(bool)
tulips.set_is_flowering(bool)