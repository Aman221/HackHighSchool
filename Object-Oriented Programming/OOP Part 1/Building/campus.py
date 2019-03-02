from building import Building

class Campus:
	def __init__ (self):
		self.building = []
		self.num_buildings = 0
		self.capacity = 0

	def add_building(self, building):
		self.building.append(building)
		self.num_buildings += 1
		self.capacity = building.cap

	def get_info(self):
		print "The campus has " + str(self.num_buildings) + " buildings with a combined capacity of " + str(self.capacity) + "."