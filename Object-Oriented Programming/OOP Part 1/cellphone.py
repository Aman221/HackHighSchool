class Cellphone:
	def call(self):
		print "Making a call..."
	def text(self):
		print "Sending a text..."
	def drop(self):
		print "CRASH! CRACK!"


def main():
	o4f = Cellphone()
	o4f.call()
	o4f.text()
	o4f.drop()

if __name__ == "__main__":
	main()