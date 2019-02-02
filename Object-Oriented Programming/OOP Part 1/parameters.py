name_input = raw_input("Alright, who's getting roasted?" + '\n' + "---> ")
class Greeter:
	def speak(self):
		print "Hello, " + name_input

class InsultComic:
	def speak(self):
		print "I'd say it's good to see you, " + name_input + ", but I'd be lying..."

def main():
	cordial = Greeter()
	roast = InsultComic()
	cordial.speak()
	roast.speak()

if __name__ == "__main__":
	main()