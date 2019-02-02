class Animal:
	def __init__(self):
		print "Making an Animal"
	def speak(self):
		pass
	def sleep(self):
		print "Zzzz..."

class Dog(Animal):
	def __init__(self):
		print "Making a Dog"
	def speak(self):
		print "Woof"

class Cat(Animal):
	def __init__(self):
		print "Making a Cat"
	def speak(self):
		print "Meow"

def main():
	ob4a = Animal()
	ob4d = Dog()
	ob4c = Cat()
	ob4a.speak()
	ob4d.speak()
	ob4c.speak()
	ob4a.sleep()
	ob4d.sleep()
	ob4c.sleep()

if __name__ == "__main__":
	main()