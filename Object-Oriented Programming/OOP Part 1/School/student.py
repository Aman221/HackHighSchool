from person import Person

class Student(Person):
	def reply(self, teacher):
		print self.name + ": Good morning, " + teacher.name
