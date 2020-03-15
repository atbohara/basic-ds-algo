"""Demonstration of different built-in methods for sorting.
Ref: https://docs.python.org/3.3/howto/sorting.html
"""


# Using list.sort() method.
ls1 = [1, 3, 10, 2, 9]
print("Original list: ", ls1)
ls1.sort()
print("Original list after sort(): ", ls1)
print()


# Using sorted() method.
ls2 = [0, 4, 7, 1, 1]
print("Original list: ", ls2)
ls3 = sorted(ls2)
print("Original list after sorted(): ", ls2)
print("New sorted list: ", ls3)
print()


# Use of key function.
sentence = "This is a sorting example in Python!"
print("Original sentence: ", sentence)
ws = sorted(sentence.split(), key=str.lower)
print("Sorted words using key function: ", ws)
print()


# sorted() works on any iterable.
# More general key function usage.
student_tuples = [
	('jane', 'B', 12),
	('dave', 'B', 10),
	('john', 'A', 15)
]
print("Original order: ", student_tuples)
# Sort students on grade.
sorted_tuples = sorted(student_tuples, key=lambda student: student[1])
print("Sorted on grades: ", sorted_tuples)
print()


class Student:
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age

	def __repr__(self):
		return repr((self.name, self.grade, self.age))


student_objects = [
	Student('jane', 'B', 12),
	Student('dave', 'B', 10),
	Student('john', 'A', 15)
]
print("Original objects: ", student_objects)
sorted_objects = sorted(student_objects, key=lambda student: student.grade)
print("Sorted objects: ", sorted_objects)
print()


# Using 'operator' module's itemgetter(), attrgetter(), and methodcaller().
from operator import itemgetter, attrgetter
print("Student tuples sorted on age using itemgetter(): ", sorted(student_tuples, key=itemgetter(2)))
print()
print("Student objects sorted descending on age using attrgetter(): ", sorted(student_objects, key=attrgetter('age'), reverse=True))
