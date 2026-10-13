"""
================================================================================
Day 18: Introduction to Object-Oriented Programming (OOP) in Python
================================================================================
Object-Oriented Programming (OOP) is a programming paradigm based on the concept
of "objects", which contain data (attributes/properties) and code (methods/functions).

Core Concepts Covered in this Script:
1. What is a Class and an Object?
2. The __init__() Constructor
3. Understanding the 'self' Keyword
4. Instance Methods (Behaviors)
5. Class Attributes vs Instance Attributes
6. Modifying and Deleting Attributes
7. The __str__() Method (Friendly String Representation)
8. Practical Mini Example: Student Record System
================================================================================
"""

def print_separator(title: str):
    """Utility helper to print clear section banners."""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


# ==============================================================================
# 1. WHAT IS A CLASS AND AN OBJECT?
# ==============================================================================
# A Class is a blueprint (template) for creating objects.
# An Object is an instance of a class that contains actual values.

print_separator("1. Class Definition & Object Instantiation")

class Car:
    """A minimal blueprint representing a car."""
    pass

# Creating objects (instances of Car)
car1 = Car()
car2 = Car()

print("car1 object:", car1)
print("car2 object:", car2)
print("Are car1 and car2 the same object?", car1 is car2)
print("Type of car1:", type(car1))


# ==============================================================================
# 2. THE __init__() CONSTRUCTOR & INSTANCE ATTRIBUTES
# ==============================================================================
# __init__ is a special method automatically called when a new object is created.
# It initializes the object's attributes (state).

print_separator("2. The __init__() Constructor")

class Person:
    def __init__(self, name: str, age: int):
        # Instance attributes: unique to each instance
        self.name = name
        self.age = age

# Creating instances with initial values
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(f"Person 1: Name = {person1.name}, Age = {person1.age}")
print(f"Person 2: Name = {person2.name}, Age = {person2.age}")


# ==============================================================================
# 3. UNDERSTANDING 'self'
# ==============================================================================
# 'self' refers to the specific instance calling the method.
# It allows each object to access and modify its own data.

print_separator("3. Understanding 'self'")

class Device:
    def __init__(self, brand: str):
        self.brand = brand

    def identify(self):
        # 'self' points directly to the current instance
        print(f"Device brand is: {self.brand} (Memory ID: {id(self)})")

phone = Device("Apple")
laptop = Device("Dell")

print(f"phone memory id : {id(phone)}")
phone.identify()

print(f"laptop memory id: {id(laptop)}")
laptop.identify()


# ==============================================================================
# 4. INSTANCE METHODS (BEHAVIORS)
# ==============================================================================
# Methods are functions defined inside a class that operate on instance data.

print_separator("4. Instance Methods")

class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self):
        """Action method."""
        return f"{self.name} says Woof!"

    def describe(self):
        """Method accessing multiple instance attributes."""
        return f"{self.name} is a {self.breed}."

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())
print(my_dog.describe())


# ==============================================================================
# 5. CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# ==============================================================================
# Class Attributes: Shared by ALL instances of the class.
# Instance Attributes: Unique to EACH individual instance.

print_separator("5. Class Attributes vs Instance Attributes")

class Employee:
    # Class attribute (shared by all employees)
    company_name = "Tech Innovations Inc."

    def __init__(self, name: str, role: str):
        # Instance attributes (unique to each employee)
        self.name = name
        self.role = role

emp1 = Employee("John Doe", "Software Engineer")
emp2 = Employee("Jane Smith", "Product Manager")

print(f"{emp1.name} ({emp1.role}) works at {emp1.company_name}")
print(f"{emp2.name} ({emp2.role}) works at {emp2.company_name}")

# Modifying class attribute affects all instances
Employee.company_name = "Global Tech Corp."
print(f"After company rename, emp1 works at: {emp1.company_name}")
print(f"After company rename, emp2 works at: {emp2.company_name}")


# ==============================================================================
# 6. MODIFYING & DELETING ATTRIBUTES
# ==============================================================================
# Attributes can be updated, dynamically added, or deleted using 'del'.

print_separator("6. Modifying & Deleting Attributes")

class Book:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

book = Book("Fluent Python", 45.00)
print(f"Original price: ${book.price}")

# Updating an attribute
book.price = 39.99
print(f"Discounted price: ${book.price}")

# Dynamically adding a new attribute
book.rating = 4.8
print(f"Added attribute (rating): {book.rating}")

# Deleting an attribute
del book.rating
print(f"Does 'rating' exist after deletion? {'rating' in book.__dict__}")


# ==============================================================================
# 7. THE __str__() METHOD (STRING REPRESENTATION)
# ==============================================================================
# __str__() returns a human-readable string representation of the object.

print_separator("7. The __str__() Method")

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name='{self.name}', price=${self.price:.2f})"

item = Product("Wireless Mouse", 24.50)
# When printed or converted to str, Python automatically invokes __str__
print(item)


# ==============================================================================
# 8. PRACTICAL MINI EXAMPLE: STUDENT PROFILE
# ==============================================================================
# A concise, complete example bringing together class, attributes, and methods.

print_separator("8. Mini Practical Example: Student")

class Student:
    school_name = "Code Academy"

    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name
        self.grades: list[float] = []

    def add_grade(self, grade: float):
        """Add a grade between 0 and 100."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Added grade {grade} for {self.name}.")
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def get_average(self) -> float:
        """Calculate average grade."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        avg = self.get_average()
        return f"[{self.school_name}] Student #{self.student_id}: {self.name} | Average: {avg:.1f}"

# Testing the Student class
student1 = Student(101, "Sam")
student1.add_grade(88.5)
student1.add_grade(94.0)
student1.add_grade(79.5)

print(student1)
print(f"Final Average for {student1.name}: {student1.get_average():.2f}")
