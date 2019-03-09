from person import Person

class Teacher(Person):
	def greet(self, students):
		print self.name + ": Welcome to class, " + students.name

