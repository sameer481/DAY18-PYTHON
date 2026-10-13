# Day 18: Python Object-Oriented Programming (OOP) - Introduction 🧱

Welcome to **Day 18** of the Python Mastery Series! Today focuses on the foundational building blocks of **Object-Oriented Programming (OOP)** in Python.

OOP is a fundamental programming paradigm that models real-world entities as software **objects** that bundle state (**attributes**) and behavior (**methods**).

---

## 📁 Repository Structure

```text
DAY18-PYTHON/
│
├── 01_introduction_to_oops.py   # Hands-on code demonstrating all core OOP introductory concepts
├── .gitignore                   # Standard Python exclusions
└── README.md                    # Comprehensive masterclass guide & conceptual walkthrough
```

---

## 🧭 Why Object-Oriented Programming (OOP)?

In Procedural Programming, programs are organized around sequential functions and shared global data:
```text
[ Data ]  ---> Passed into --->  [ Function A ]  --->  [ Function B ]
```
As programs grow, data can easily be mutated inadvertently across distant functions.

In **Object-Oriented Programming (OOP)**, state and logic are encapsulated into self-contained units called **Objects**:
```text
+------------------------------------+
|               OBJECT               |
|  +------------------------------+  |
|  | State (Attributes):          |  |
|  |  - name: "Sam"               |  |
|  |  - age: 22                   |  |
|  +------------------------------+  |
|  | Behaviors (Methods):         |  |
|  |  - study()                   |  |
|  |  - get_average()             |  |
|  +------------------------------+  |
+------------------------------------+
```

### Key Benefits of OOP:
- **Modularity**: Code is structured into logical, autonomous components.
- **Reusability**: Blueprints can be instantiated as many times as needed.
- **Maintainability**: Changes to an object's internal state logic do not break external code.
- **Real-World Modeling**: Represents domains (users, accounts, products) naturally.

---

## 📚 Core Concepts & Code Walkthrough

### 1. Classes vs Objects

- **Class**: A blueprint or schema defining what attributes and methods an entity will have.
- **Object**: A concrete instance created from the class containing actual values in memory.

```python
# Class (Blueprint)
class Car:
    pass

# Objects (Instances)
car1 = Car()
car2 = Car()

print(car1 is car2)  # False (two distinct instances in memory)
```

---

### 2. The `__init__()` Constructor Method

The `__init__()` method is a special "dunder" (double-underscore) initialization method. Python calls it automatically whenever a new object is created.

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

p1 = Person("Alice", 25)
print(p1.name)  # Alice
print(p1.age)   # 25
```

---

### 3. Understanding the `self` Keyword

- `self` refers explicitly to the **current instance** of the class.
- When you invoke `p1.speak()`, Python translates it behind the scenes to: `Person.speak(p1)`.
- It ensures operations update and read the calling object's private memory space.

```python
class Device:
    def __init__(self, brand: str):
        self.brand = brand

    def identify(self):
        print(f"Device: {self.brand} at memory address {id(self)}")
```

---

### 4. Instance Methods (Behaviors)

Methods are functions declared inside a class definition that operate on the instance's data via `self`.

```python
class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())  # Buddy says Woof!
```

---

### 5. Class Attributes vs Instance Attributes

| Feature | Instance Attribute | Class Attribute |
| :--- | :--- | :--- |
| **Scope** | Unique to an individual object instance | Shared across **all** instances of the class |
| **Defined** | Inside `__init__()` via `self.var = val` | Directly in the class body outside any method |
| **Access** | `instance.var` | `ClassName.var` or `instance.var` |
| **Modification** | Affects only that single instance | Modifying via `ClassName.var` affects all instances |

```python
class Employee:
    company = "Tech Corp"  # Class attribute

    def __init__(self, name: str):
        self.name = name   # Instance attribute

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company)  # Tech Corp
print(e2.company)  # Tech Corp
```

---

### 6. Attribute Lifecycle (Modify, Add, Delete)

Python attributes are dynamic:

```python
class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

item = Item("Notebook", 5.0)

# 1. Modify
item.price = 4.5

# 2. Dynamically add
item.discount = 0.5

# 3. Delete
del item.discount
```

---

### 7. Readable String Representation (`__str__`)

By default, printing an object outputs its memory address (e.g., `<__main__.Car object at 0x... >`). Implementing `__str__()` provides a clean, human-readable representation:

```python
class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} (${self.price:.2f})"

p = Product("Headphones", 59.99)
print(p)  # Headphones ($59.99)
```

---

### 8. Quick Roadmap: The 4 Pillars of OOP

This introduction sets the stage for the four core principles of OOP:

```text
                  +--------------------------------+
                  |   4 Pillars of Python OOP      |
                  +---------------+----------------+
                                  |
    +-----------------+-----------+----------+-----------------+
    |                 |                      |                 |
    v                 v                      v                 v
[Encapsulation]  [Inheritance]         [Polymorphism]     [Abstraction]
Hiding internal  Deriving new          Same interface,    Hiding complex
state & logic    classes from base     different behavior implementation
via access rules classes               under the hood     details
```

---

## 🚀 Running the Code

Ensure you have **Python 3.8+** installed.

```bash
# Clone the repository (if not already local)
git clone https://github.com/sameer481/DAY18-PYTHON.git

# Navigate to the project directory
cd DAY18-PYTHON

# Run the introduction script
python 01_introduction_to_oops.py
```

---

## 💡 Summary Checklist

- [x] Defined what a **Class** (blueprint) and **Object** (instance) are.
- [x] Initialized object states using the **`__init__()`** constructor.
- [x] Understood how **`self`** links methods to the calling instance.
- [x] Implemented **Instance Methods** for object actions.
- [x] Differentiated between **Class Attributes** and **Instance Attributes**.
- [x] Managed object attributes dynamically (read, write, delete).
- [x] Customized object printing with the **`__str__()`** method.
