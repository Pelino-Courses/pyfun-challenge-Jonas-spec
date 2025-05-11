from abc import ABC, abstractmethod
from typing import list,Iterator

# Descriptor for attribute validation
class PositiveInteger:
    def __set_name__(self, owner, name):
          self.name = name
     

    def __get__(self, instance, owner):
         return instance.__dict__.get(self.name)
    
    
    def __set__(self, instance, value):
        if not isinstance(value,int) or value <=0:
            raise ValueError(f"{self.name} must be a positive integer")
        instance.__dict__[self.name] = value    
                            
#Abstact base class 
class person (ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        @abstractmethod
        def get_role(self) -> str:
            pass
        #student and Instructor classes
            class student(person):
             def __init__(self, name: str, age: int):
                super().__init__(name, age)
                self.courses = []
        def enroll(self, course):
           self.courses.append(course)
           def get_role(self) -> str:
               return "student"
           
           def __iter__(self) -> Iterator[str]:
               return iter(self.courses)
           class instructor(person):
               def __init__(self, name: str, age: int, department: str):
                   super().__init__(name, age)
                   self.department = department
                   def get_role(self) -> str:
                       return "instructor"
                   
class TeachingAssistant(student, instructor): # type: ignore
   def __init__(self, name: str, age: int, department: str):
        student.__init__(self, name, age)
        instructor.__init__(self, name, age, department)  # type: ignore

   def get_role(self) -> str:
      return "Teaching assistant"

# Course class
class course:
   course_id = PositiveInteger()

   def __init__(self, name: str, course_id: int):
    self.name = name
    self.course_id = course_id
    self.students = []

   def enroll_student(self, student: student):  # type: ignore
    self.students.append(student)
    student.enroll(self.name)

   def __iter__(self) -> Iterator[student]: # type: ignore
       return iter(self.students) 

   def __add__(self, other):
     return Course(f"{self.name} & {other.name}", self.course_id + other.course_id) # type: ignore


class CourseFactory:
    @staticmethod
    def create_course(course_type: str, name: str, course_id: int):
        if course_type.lower() == "math":
            return course(f"Math: {name}", course_id)
        elif course_type.lower() == "science":
            return course(f"Science: {name}", course_id)
        else:
            return course(name, course_id)

# -Enrollment Class
class Enrollment:
    def __init__(self):
        self.records = []

    def enroll(self, student: student1, course: course): # type: ignore
        try:
            course.enroll_student(student)
            self.records.append((student, course))
        except Exception as e:
            print(f"Enrollment error: {e}")

# -------- Example Usage --------
if __name__ == "__main__":
    student1 = student1("Alice", 20) # type: ignore
    student2 = student1("Bob", 22)

    course1 = CourseFactory.create_course("math", "Calculus", 101)
    course2 = CourseFactory.create_course("science", "Physics", 102)

    enrollment_system = Enrollment()
    enrollment_system.enroll(student1, course1)
    enrollment_system.enroll(student2, course2)

    ta = TeachingAssistant("Charlie", 25, "Computer Science")
    print(f"{ta.name} is a {ta.get_role()}")

    for course in student1:
        print(f"{student1.name} is enrolled in {course.name}")

    for student in course1:
        print(f"{student.name} is in {course1.name}")