from animal import Animal
from dog import Dog
from cat import Cat

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