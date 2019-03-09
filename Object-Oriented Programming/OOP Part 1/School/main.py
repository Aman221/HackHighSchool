from classroom import Classroom
from person import Person
from student import Student
from teacher import Teacher

def main():
	class1 = Classroom(20, "Wesley")
	class2 = Classroom(20, "Anand")
	class1.add_students(Student("Alice"))
	class1.add_students(Student("Carol"))
	class1.add_students(Student("Eve"))
	class2.add_students(Student("Bob"))
	class2.add_students(Student("Dave"))
	class1.class_stats()
	class2.class_stats()
	class1.rollcall()
	class2.rollcall()


if __name__ == "__main__":
	main()