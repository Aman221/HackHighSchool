from teacher import Teacher
from student import Student

class Classroom:
	def __init__ (self, capacity, name):
		self.cap = 20
		self.teacher = Teacher(name)
		self.people = []

	def add_students(self, student):
		self.people.append(student)

	def rollcall(self):
		for s in self.people:
			self.teacher.greet(s)
			s.reply(self.teacher)


	def class_stats(self):
		print "The classroom has a standard Capacity of " + str(self.cap) + " and is run by " + self.teacher.name + ". It currently has " + str(len(self.people)) + " students."

