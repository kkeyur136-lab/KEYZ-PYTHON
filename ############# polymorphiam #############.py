############# polymorphiam #################


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


### inheritance #########

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

####### encapulation #################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

############# class funtion ##############

###### task -7 ################
# CRATE 3 CLASS 
#CRATE 2 OBJECT PER CLASS 
# CRATE _ INIT__ METHOD AMD ADD 3 VARIABLES :
# CREATE 2 METHOD  USING GET - 3 VARIABLES ,, POST USING 3 VARIABLES 







class Student1:
    def __init__(self, name, math, science):
        self.name = name
        self.math = math
        self.science = science

    def display(self):
        print("Student Name:", self.name)
        print("Math:", self.math)
        print("Science:", self.science)


class Student2:
    def __init__(self, name, english, computer):
        self.name = name
        self.english = english
        self.computer = computer

    def display(self):
        print("Student Name:", self.name)
        print("English:", self.english)
        print("Computer:", self.computer)


class Student3:
    def __init__(self, name, physics, chemistry):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry

    def display(self):
        print("Student Name:", self.name)
        print("Physics:", self.physics)
        print("Chemistry:", self.chemistry)


# Objects
s1 = Student1("Keyur", 85, 90)
s2 = Student2("Rahul", 78, 88)
s3 = Student3("Priya", 92, 89)

# Output
s1.display()
print()

s2.display()
print()

s3.display()


############ GET varibales ################

from django.shortcuts import render

def student_get(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    city = request.GET.get("city")

    return render(request, "student.html", {
        "name": name,
        "age": age,
        "city": city
    })


# POST USING 3 VARIABLES ####


from django.shortcuts import render

def student_post(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        marks = request.POST.get("marks")

        print(name)
        print(subject)
        print(marks)

    return render(request, "student.html")





