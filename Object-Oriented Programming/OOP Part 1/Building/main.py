from building import Building
from campus import Campus

def main():
	build = Building("Math Building", 25)
	build2 = Building("Science Building", 17)
	camp = Campus()
	build.get_info()
	build2.get_info()
	camp.add_building(build)
	camp.add_building(build2)
	camp.get_info()


if __name__ == "__main__":
	main()