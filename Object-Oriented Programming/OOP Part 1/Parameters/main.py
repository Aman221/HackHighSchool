from greeter import Greeter
from insult import InsultComic

def main():
	cordial = Greeter()
	roast = InsultComic()
	cordial.speak()
	roast.speak()

if __name__ == "__main__":
	main()