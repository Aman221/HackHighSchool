class Building:
	def __init__ (self, name, capacity):
		self.name = name
		self.cap = capacity

	def get_info(self):
		print 'Building "' + self.name + '" can hold ' + str(self.cap) + ' people.'