'''Question 1

import datetime
def datedifference(dat1: str, date2: str) -> int:
    try:
        d1 = datetime.datetime.strptime(date1, "%Y-%m_%d")
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        delta = d2 - d1
        return delta.days
    except ValueError as Ve:
        raise ValueError("PLease provide dates in 'YYY-MM-DD' format.") from ve
    if __name__ == "__main__":
        try:
            print(date_difference("20203-04-01","2023-04-10"))
        except ValueError as e:
            print(f"Error: {e}")'''

question 2


'''
def process_operations(*args, **kwargs):
    
    if len(args) == 0: 
        raise ValueError("At least one number must be provided.")

    for arg in args: 
        if not isinstance(arg, (int, float)): 
            raise TypeError(f"Invalid argument {arg}. All positional arguments must be numbers.")

    results = {}

    if kwargs.get("add"):
        results["add"] = sum(args)

    if kwargs.get("subtract"):
        result = args[0]

        for num in args[1:]: 
            result -= num
        results["subtract"] = result
        
        
    if kwargs.get("multiply"):
        result = 1
        for num in args:
            result *= num
            
        results["multiply"] = result

    if kwargs.get("divide"):
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Cannot divide by zero.")
            result /= num
        results["divide"] = result

    return results

def calculate(*args, **kwargs):
    return process_operations(*args, **kwargs)

if __name__ == "__main__":
    __name__ == "__main__":
    print(calculate(10, 5, add=True, subtract=True)) 
    print(calculate(3, 4, multiply=True)) 
    print(calculate(100, 10, 2, divide=True))
'''

question 3
'''
def format_text(
        text: str,
        prefix: str = "",
        suffix: str = "",
        capitalizer: bool = False,
        max_length: int = None
) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(prefix,str):
        raise TypeError("prefix must be a string")
    if not isinstance(suffix, str):
      raise TypeError("suffix must be a string.")
   if not isinstance(capitalize, bool):
   raise TypeError("capitalize must be a boolean.")
   if max_length is not None:
   if not isinstance(max_length, int):
   raise TypeError("max_length must be an integer or None.")
      if max_length < 0:
    raise ValueError("max_length cannot be negative.")

if capitalize:
   text = text.capitalize()
   formatted = [:max_length]
return formatted
 
 if __name__== " __main__":
   print(format_text("hello", prefix=">>", siffix="<<"))
   print(format_text("hello", capitalize=True))
   print(format_text("hello world", max_length=5))

        '''

question 4
'''   class Product:

 def __init__(self, name: str, price: float, quantity: int):
     if not isinstance(name, str) or not name.strip():
      raise ValueError("Product name must be a non-empty string.")
 if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
                 if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.name = name
     self.price = float(price)
    self.quantity = quantity

   def add_inventory(self, amount: int):
       """Add inventory to the product."""
      if not isinstance(amount, int) or amount <= 0:
           raise ValueError("Amount to add must be a positive integer.")
         self.quantity += amount

    def remove_inventory(self, amount: int):
         
        if not isinstance(amount, int) or amount <= 0:
           raise ValueError("Amount to remove must be a positive integer.")
            if amount > self.quantity:
                 raise ValueError("Cannot remove more than available quantity.")
        self.quantity -= amount

      def total_value(self) -> float:
         
       return self.price * self.quantity

     def display_info(self):
    
     print(f"Product: {self.name}")
       print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.total_value():.2f}")

# Example usage
if __name__ == "__main__":
  try:
      p = Product("Laptop", 899.99, 10)
      p.display_info()
      p.add_inventory(5)
      p.remove_inventory(3)
      p.display_info()
     except ValueError as e:
     print(f"Error: {e}")
     '''
Question 5
'''
 import math

class Shape:
 

   def __init__(self, name: str):
      if not isinstance(name, str) or not name.strip():
         raise ValueError("Shape name must be a non-empty string.")
       self.name = name

     def area(self):
       """Returns the area of the shape. Must be overridden in subclasses."""
     raise NotImplementedError("Subclasses must implement this method.")

   def __str__(self):
     return f"{self.name} with area: {self.area():.2f}"

class Circle(Shape):


   def __init__(self, radius: float):
    super().__init__("Circle")
    if not isinstance(radius, (int, float)) or radius <= 0:
      raise ValueError("Radius must be a positive number.")
       self.radius = radius

    def area(self):
     return math.pi * self.radius ** 2

   def __str__(self):
       return f"Circle (radius={self.radius}) with area: {self.area():.2f}"

class Rectangle(Shape):
 
   def __init__(self, width: float, height: float):
     super().__init__("Rectangle")
      if not all(isinstance(x, (int, float)) and x > 0 for x in (width, height)):
           raise ValueError("Width and height must be positive numbers.")
    self.width = width
     self.height = height

     def area(self):
    return self.width * self.height

    def __str__(self):
     return f"Rectangle (width={self.width}, height={self.height}) with area: {self.area():.2f}"

class Triangle(Shape):


   def __init__(self, base: float, height: float):
     super().__init__("Triangle")
     if not all(isinstance(x, (int, float)) and x > 0 for x in (base, height)):
       raise ValueError("Base and height must be positive numbers.")
          self.base = base
       self.height = height

  def area(self):
       return 0.5 * self.base * self.height

    def __str__(self):
       return f"Triangle (base={self.base}, height={self.height}) with area: {self.area():.2f}"

# Example usage
if __name__ == "__main__":
    shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
  ]
   for shape in shapes:
     print(shape)

'''
        Question 6
from abc import ABC, abstractmethod
from typing import list,Iterator

# Descriptor for attribute validation
Class PositiveInteger:
def __Set_name__(self,owner,name):
    self.name = name

    def__get__(self, instance, ownner):
    return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not isinstance(value,int) or value <=0:
            raise ValueError(f"{self.name} must be a positive integer"
                             instance.__dict__[self.name] = value

#Abstact base class 
class person (ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        @abstractmethod
        def get_role(self) >- str:
            pass
            
''''

# Student and Instructor classes
class Student(Person):
   def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.courses = []

   def enroll(self, course):
     self.courses.append(course)

    def get_role(self) -> str:
       return "Student"
   
    def __iter__(self) -> Iterator[str]:
       return iter(self.courses) 

class Instructor(Person):
    def __init__(self, name: str, age: int, department: str):
      super().__init__(name, age)
       self.department = department

    def get_role(self) -> str:
      return "Instructor"


class TeachingAssistant(Student, Instructor):
   def __init__(self, name: str, age: int, department: str):
        Student.__init__(self, name, age)
        Instructor.__init__(self, name, age, department)

   def get_role(self) -> str:
      return "Teaching Assistant"

# Course class
class Course:
   course_id = PositiveInteger()

   def __init__(self, name: str, course_id: int):
    self.name = name
       self.course_id = course_id
       self.students = []

   def enroll_student(self, student: Student):
    self.students.append(student)
        student.enroll(self.name)

   def __iter__(self) -> Iterator[Student]:
       return iter(self.students) 

  def __add__(self, other):
     return Course(f"{self.name} & {other.name}", self.course_id + other.course_id)


class CourseFactory:
   @staticmethod
     def create_course(course_type: str, name: str, course_id: int):
       if course_type.lower() == "math":
         return Course(f"Math: {name}", course_id)
       elif course_type.lower() == "science":
        return Course(f"Science: {name}", course_id)
        else:
     return Course(name, course_id)

# Enrollment class
class Enrollment:
   def __init__(self):
      self.records = []

   def enroll(self, student: Student, course: Course):
       try:
            course.enroll_student(student)
            self.records.append((student, course))
         except Exception as e:
         print(f"Enrollment error: {e}")

# Example usage
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
course1 = CourseFactory.create_course("math", "Calculus", 101)
course2 = CourseFactory.create_course("science", "Physics", 102)

enrollment = Enrollment()
enrollment.enroll(student1, course1)
enrollment.enroll(student2, course2)

ta = TeachingAssistant("Charlie", 25, "Computer Science")
print(f"{ta.name} is a {ta.get_role()}")

for course in student1:
  print(f"{student1.name} is enrolled in {course}")

for student in course1:
  print(f"{student.name} is in {course1.name}")

'''

