from greeter import Greeter

class InsultComic(Greeter):
	def speak(self):
		name_input = "Wesley"
		print "I'd say it's good to see you, " + name_input + ", but I'd be lying..."
