# my own GENERATOR function
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable,start=0):
    # implement your generator function here
    for i in range(len(iterable)):
        yield start+i, iterable[i]

for i, lesson in my_enumerate(lessons, 2):
    print("Lesson {}: {}".format(i, lesson))
