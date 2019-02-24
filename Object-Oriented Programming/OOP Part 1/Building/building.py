class Building:
	def __init__ (self, name, capacity):
		self.name = name
		self.cap = capacity

	def get_info1(self):
		return 'Building "' + self.name + '" can hold ' + self.cap + ' people.'