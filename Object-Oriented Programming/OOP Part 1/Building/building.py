class Building:
	def __init__ (self, name, capacity):
		self.name = name
		self.cap = capacity

	def get_info1(self):
		return 'Building "' + self.name + '" can hold ' + self.cap + ' people.'

class Building2:
	def __init__ (self, name, capacity):
		self.name2 = name
		self.cap2 = capacity

	def get_info2(self):
		return 'Building "' + self.name2 + '" can hold ' + self.cap2 + ' people.'

class Campus:
	def get_info3(self):
		print "The campus has 2 building(s) with a combined capacity of " + str(int(self.cap)+int(self.cap2)) + " people."

Build1 = str(raw_input("What is the name of the first Building? "))
Cap1 = str(raw_input("How many people are in that building? "))
Build2 = str(raw_input("What is the name of the second Building? "))
Cap2 = str(raw_input("How many people are in that building? "))
TotalPeople = str(int(Cap1) + int(Cap2))

x = Building(Build1, Cap1)
y = Building2(Build2, Cap2)

print (x.get_info1())
print (y.get_info2())
print ("The campus has 2 building(s) with a combined capacity of " + TotalPeople + " people.")