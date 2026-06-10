# Python Full Course 🐍

Let's go. No fluff, pure code. Run everything as we go.

---

## 1. Variables & Types

```python
name = "Alice"
age = 25
height = 5.6
is_cool = True
nothing = None

print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_cool))  # <class 'bool'>
```

---

## 2. Strings

```python
s = "hello world"

print(s.upper())           # HELLO WORLD
print(s.capitalize())      # Hello world
print(s.replace("world", "python"))  # hello python
print(s[0:5])              # hello
print(s.split(" "))        # ['hello', 'world']
print(len(s))              # 11

# f-strings (use these, always)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
```

---

## 3. Numbers & Math

```python
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...
print(10 // 3)  # 3  (floor division)
print(10 % 3)   # 1  (modulo)
print(10 ** 3)  # 1000 (power)

import math
print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.14159...
print(math.ceil(4.2))  # 5
print(math.floor(4.9)) # 4
```

---

## 4. Lists

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")       # add to end
fruits.insert(1, "grape")    # add at index
fruits.remove("banana")      # remove by value
fruits.pop()                 # remove last
fruits.pop(0)                # remove by index

print(fruits[0])             # first item
print(fruits[-1])            # last item
print(fruits[1:3])           # slice

fruits.sort()                # sort in place
print(sorted(fruits))        # returns sorted copy

print(len(fruits))           # length
print("apple" in fruits)     # True/False
```

---

## 5. Tuples & Sets

```python
# Tuple - immutable list
coords = (10, 20)
x, y = coords         # unpacking
print(x, y)           # 10 20

# Set - unique values only
nums = {1, 2, 3, 3, 2, 1}
print(nums)           # {1, 2, 3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # union     {1,2,3,4,5}
print(a & b)   # intersect {3}
print(a - b)   # diff      {1,2}
```

---

## 6. Dictionaries

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "Nairobi"
}

print(person["name"])           # Alice
print(person.get("country", "Unknown"))  # safe get

person["email"] = "alice@mail.com"   # add key
person["age"] = 26                   # update
del person["city"]                   # delete

print(person.keys())
print(person.values())
print(person.items())

# loop
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 7. Conditionals

```python
age = 20

if age < 13:
    print("child")
elif age < 18:
    print("teenager")
elif age < 65:
    print("adult")
else:
    print("senior")

# one-liner (ternary)
status = "adult" if age >= 18 else "minor"

# match (Python 3.10+)
command = "quit"
match command:
    case "start":
        print("Starting...")
    case "quit":
        print("Quitting...")
    case _:
        print("Unknown command")
```

---

## 8. Loops

```python
# for loop
for i in range(5):        # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2): # 2,4,6,8
    print(i)

# loop over list
for fruit in ["apple", "banana", "mango"]:
    print(fruit)

# enumerate (index + value)
for i, fruit in enumerate(["apple", "banana"]):
    print(i, fruit)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# break & continue
for i in range(10):
    if i == 3: continue   # skip 3
    if i == 7: break      # stop at 7
    print(i)
```

---

## 9. List Comprehensions

```python
# old way
squares = []
for i in range(10):
    squares.append(i ** 2)

# new way (use this)
squares = [i ** 2 for i in range(10)]
evens   = [i for i in range(20) if i % 2 == 0]
words   = ["hello", "world"]
upper   = [w.upper() for w in words]

# dict comprehension
squared = {i: i**2 for i in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}
```

---

## 10. Functions

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))             # Hello, Alice!
print(greet("Bob", "Hey"))        # Hey, Bob!

# *args - multiple positional args
def add(*nums):
    return sum(nums)

print(add(1, 2, 3, 4))  # 10

# **kwargs - keyword args
def profile(**info):
    for k, v in info.items():
        print(f"{k}: {v}")

profile(name="Alice", city="Nairobi", age=25)

# lambda (anonymous function)
double = lambda x: x * 2
print(double(5))   # 10

square = lambda x: x ** 2
nums = [1,2,3,4,5]
print(list(map(square, nums)))         # [1,4,9,16,25]
print(list(filter(lambda x: x>2, nums)))  # [3,4,5]
```

---

## 11. Classes & OOP

```python
class Animal:
    # class variable
    kingdom = "Animalia"

    def __init__(self, name, sound):
        self.name = name      # instance variable
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __repr__(self):
        return f"Animal({self.name})"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"


dog = Dog("Rex")
print(dog.speak())       # Rex says Woof
print(dog.fetch("ball")) # Rex fetched the ball!
print(dog.kingdom)       # Animalia
```

---

## 12. Decorators

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

slow_function()  # slow_function took 1.0001s


# property decorator
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area)  # 78.539... (no parentheses needed)
```

---

## 13. Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type or Value error: {e}")
else:
    print("No error occurred")     # runs if no exception
finally:
    print("This always runs")      # cleanup


# raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b

# custom exception
class InsufficientFundsError(Exception):
    def __init__(self, amount):
        super().__init__(f"Need {amount} more funds")

raise InsufficientFundsError(500)
```

---

## 14. File I/O

```python
# write
with open("data.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# read all
with open("data.txt", "r") as f:
    content = f.read()

# read lines
with open("data.txt", "r") as f:
    lines = f.readlines()

# append
with open("data.txt", "a") as f:
    f.write("Appended line\n")

# JSON
import json

data = {"name": "Alice", "scores": [95, 87, 92]}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r") as f:
    loaded = json.load(f)

print(loaded["name"])  # Alice
```

---

## 15. Modules & Packages

```python
# built-in modules
import os
import sys
import random
import datetime
from pathlib import Path

print(os.getcwd())                    # current directory
print(os.listdir("."))                # list files
os.makedirs("myfolder", exist_ok=True)

print(random.randint(1, 100))        # random number
print(random.choice(["a","b","c"]))  # random pick
random.shuffle([1,2,3,4,5])

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))

p = Path("data.txt")
print(p.exists())
print(p.suffix)   # .txt
print(p.stem)     # data
```

---

## 16. Generators & Iterators

```python
# generator function - memory efficient
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)   # 5,4,3,2,1

# generator expression
gen = (x**2 for x in range(1000000))  # doesn't load all in memory
print(next(gen))  # 0
print(next(gen))  # 1

# infinite generator
def integers():
    n = 0
    while True:
        yield n
        n += 1

from itertools import islice
first10 = list(islice(integers(), 10))
print(first10)  # [0,1,2,...,9]
```

---

## 17. Context Managers

```python
# using contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    try:
        yield name
    finally:
        print(f"Releasing {name}")

with managed_resource("database") as res:
    print(f"Using {res}")

# class-based
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, *args):
        import time
        self.elapsed = time.time() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")

with Timer():
    sum(range(1_000_000))
```

---

## 18. Async / Await

```python
import asyncio

async def fetch_data(name, delay):
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)      # simulates network call
    return f"{name} data"

async def main():
    # run concurrently
    results = await asyncio.gather(
        fetch_data("users", 2),
        fetch_data("products", 1),
        fetch_data("orders", 3),
    )
    for r in results:
        print(r)

asyncio.run(main())
# all 3 finish in ~3s instead of 6s
```

---

## 19. Type Hints

```python
from typing import Optional, Union, List, Dict, Tuple

def greet(name: str) -> str:
    return f"Hello {name}"

def add(a: int, b: int) -> int:
    return a + b

def process(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

def maybe(val: Optional[str] = None) -> str:
    return val or "default"

# Python 3.10+ union shorthand
def flex(val: int | str | None) -> str:
    return str(val)

# dataclass
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    tags: List[str] = field(default_factory=list)

    def is_adult(self) -> bool:
        return self.age >= 18

u = User("Alice", 25, ["admin", "user"])
print(u)
print(u.is_adult())
```

---

## 20. Real Mini Project — CLI Todo App

```python
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List

DB = Path("todos.json")

@dataclass
class Todo:
    id: int
    task: str
    done: bool = False

def load() -> List[Todo]:
    if not DB.exists():
        return []
    data = json.loads(DB.read_text())
    return [Todo(**t) for t in data]

def save(todos: List[Todo]):
    DB.write_text(json.dumps([asdict(t) for t in todos], indent=2))

def add(task: str):
    todos = load()
    new_id = max((t.id for t in todos), default=0) + 1
    todos.append(Todo(id=new_id, task=task))
    save(todos)
    print(f"✅ Added: {task}")

def complete(todo_id: int):
    todos = load()
    for t in todos:
        if t.id == todo_id:
            t.done = True
            save(todos)
            print(f"✔️  Done: {t.task}")
            return
    print("Not found")

def list_todos():
    todos = load()
    if not todos:
        print("Nothing to do 🎉")
        return
    for t in todos:
        status = "✔" if t.done else "○"
        print(f"[{status}] {t.id}. {t.task}")

def delete(todo_id: int):
    todos = [t for t in load() if t.id != todo_id]
    save(todos)
    print(f"🗑️  Deleted {todo_id}")

# --- run it ---
add("Learn Python")
add("Build a project")
add("Get a job")
list_todos()
complete(1)
delete(2)
list_todos()
```

---
# OOP in Python — Deep Dive 🏗️

---

## 1. Classes & Objects — What's Actually Happening

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

d = Dog("Rex", 3)

# every object has a __dict__
print(d.__dict__)          # {'name': 'Rex', 'age': 3}
print(d.__class__)         # <class '__main__.Dog'>
print(Dog.__dict__)        # all class attributes & methods
print(isinstance(d, Dog))  # True
print(type(d))             # <class '__main__.Dog'>
print(type(d) is Dog)      # True
```

---

## 2. Class vs Instance vs Static

```python
class Employee:
    company = "Acme Inc"      # class variable — shared by ALL instances
    _count = 0                # private by convention

    def __init__(self, name, salary):
        self.name = name      # instance variable — unique per object
        self.salary = salary
        Employee._count += 1

    def get_info(self):                  # instance method — gets self
        return f"{self.name} at {self.company}"

    @classmethod
    def get_count(cls):                  # class method — gets cls
        return f"{cls._count} employees"

    @classmethod
    def from_string(cls, s):             # alternate constructor pattern
        name, salary = s.split(",")
        return cls(name, int(salary))

    @staticmethod
    def validate_salary(salary):         # static — no self, no cls
        return salary > 0

e1 = Employee("Alice", 50000)
e2 = Employee.from_string("Bob,60000")

print(e1.get_info())          # Alice at Acme Inc
print(Employee.get_count())   # 2 employees
print(Employee.validate_salary(-100))  # False

# class variable trap
e1.company = "NewCo"          # creates INSTANCE variable, doesn't change class
print(e1.company)             # NewCo
print(e2.company)             # Acme Inc  ← unchanged
print(Employee.company)       # Acme Inc  ← unchanged
```

---

## 3. Inheritance

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # call parent __init__
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetched the {item}"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def speak(self):                     # override parent method
        base = super().speak()           # call parent version
        return f"{base}... (ignores you)"


dog = Dog("Rex", "Labrador")
cat = Cat("Whiskers")

print(dog.speak())    # Rex says Woof
print(cat.speak())    # Whiskers says Meow... (ignores you)
print(repr(dog))      # Dog('Rex')

# MRO — Method Resolution Order
print(Dog.__mro__)
# (<class 'Dog'>, <class 'Animal'>, <class 'object'>)
```

---

## 4. Multiple Inheritance & MRO

```python
class A:
    def who(self): return "A"

class B(A):
    def who(self): return f"B -> {super().who()}"

class C(A):
    def who(self): return f"C -> {super().who()}"

class D(B, C):       # inherits from both B and C
    def who(self): return f"D -> {super().who()}"

d = D()
print(d.who())       # D -> B -> C -> A
print(D.__mro__)     # D, B, C, A, object  (C3 linearization)

# Mixin pattern — the RIGHT way to use multiple inheritance
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__, indent=2)

class LogMixin:
    def log(self, msg):
        print(f"[{self.__class__.__name__}] {msg}")

class TimestampMixin:
    from datetime import datetime
    def created_at(self):
        return self.datetime.now().isoformat()

class User(JSONMixin, LogMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

u = User("Alice", "alice@mail.com")
print(u.to_json())
u.log("User created")
```

---

## 5. Encapsulation — Public, Protected, Private

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # public   — anyone
        self._balance = balance      # protected — convention, "don't touch"
        self.__pin = "1234"          # private  — name mangled

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(acc.get_balance())      # 1500

# protected — accessible but "please don't"
print(acc._balance)           # 1500 (works but bad practice)

# private — name mangled to _BankAccount__pin
# acc.__pin                   # AttributeError
print(acc._BankAccount__pin)  # "1234" (still accessible if you really want)

# --- property decorator for controlled access ---
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):               # getter
        return self._celsius

    @celsius.setter
    def celsius(self, val):          # setter with validation
        if val < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = val

    @celsius.deleter
    def celsius(self):               # deleter
        del self._celsius

    @property
    def fahrenheit(self):            # computed property — no setter needed
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0
t.celsius = 100
print(t.fahrenheit)   # 212.0
# t.celsius = -300    # ValueError
```

---

## 6. Polymorphism

```python
# same interface, different behavior
class Shape:
    def area(self): raise NotImplementedError
    def perimeter(self): raise NotImplementedError
    def describe(self):
        return f"{self.__class__.__name__}: area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): import math; return math.pi * self.r**2
    def perimeter(self): import math; return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, w, h): self.w = w; self.h = h
    def area(self): return self.w * self.h
    def perimeter(self): return 2*(self.w + self.h)

class Triangle(Shape):
    def __init__(self, a, b, c): self.a=a; self.b=b; self.c=c
    def area(self):
        s = (self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    def perimeter(self): return self.a+self.b+self.c

shapes = [Circle(5), Rectangle(4,6), Triangle(3,4,5)]

# polymorphic — same call, different result
for s in shapes:
    print(s.describe())

# total area — doesn't care what shape it is
total = sum(s.area() for s in shapes)
print(f"Total area: {total:.2f}")
```

---

## 7. Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def fuel_type(self) -> str:          # MUST be implemented
        pass

    @abstractmethod
    def max_speed(self) -> int:
        pass

    def description(self):               # concrete method
        return f"{self.year} {self.make} {self.model}"

    @property
    @abstractmethod
    def num_wheels(self) -> int:         # abstract property
        pass


class ElectricCar(Vehicle):
    def fuel_type(self): return "Electric"
    def max_speed(self): return 250

    @property
    def num_wheels(self): return 4


class Motorcycle(Vehicle):
    def fuel_type(self): return "Petrol"
    def max_speed(self): return 200

    @property
    def num_wheels(self): return 2


# Vehicle()  # TypeError: Can't instantiate abstract class
car = ElectricCar("Tesla", "Model S", 2024)
print(car.description())    # 2024 Tesla Model S
print(car.fuel_type())      # Electric
print(car.num_wheels)       # 4
```

---

## 8. Dunder (Magic) Methods — The Full Set

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # --- string representations ---
    def __repr__(self):               # for devs — eval-able
        return f"Vector({self.x}, {self.y})"

    def __str__(self):                # for users
        return f"({self.x}, {self.y})"

    # --- arithmetic ---
    def __add__(self, other):         # v1 + v2
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):         # v1 - v2
        return Vector(self.x-other.x, self.y-other.y)

    def __mul__(self, scalar):        # v * 3
        return Vector(self.x*scalar, self.y*scalar)

    def __rmul__(self, scalar):       # 3 * v
        return self.__mul__(scalar)

    def __neg__(self):                # -v
        return Vector(-self.x, -self.y)

    def __abs__(self):                # abs(v) — magnitude
        return (self.x**2 + self.y**2)**0.5

    # --- comparison ---
    def __eq__(self, other):          # v1 == v2
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):          # v1 < v2
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    # --- container-like ---
    def __len__(self):                # len(v)
        return 2

    def __getitem__(self, idx):       # v[0], v[1]
        return (self.x, self.y)[idx]

    def __iter__(self):               # for val in v
        yield self.x
        yield self.y

    def __contains__(self, val):      # 3 in v
        return val in (self.x, self.y)

    # --- bool ---
    def __bool__(self):               # bool(v) / if v:
        return self.x != 0 or self.y != 0

    # --- callable ---
    def __call__(self, scale):        # v(2) — call like function
        return Vector(self.x*scale, self.y*scale)


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)        # (4, 6)
print(v1 - v2)        # (2, 2)
print(v1 * 3)         # (9, 12)
print(3 * v1)         # (9, 12)
print(abs(v1))        # 5.0
print(v1 == v2)       # False
print(v1 > v2)        # True
print(list(v1))       # [3, 4]
print(3 in v1)        # True
print(v1(2))          # (6, 8)
print(bool(Vector(0,0)))  # False
```

---

## 9. Dataclasses

```python
from dataclasses import dataclass, field, asdict, astuple
from typing import List

@dataclass
class Point:
    x: float
    y: float

    def distance(self):
        return (self.x**2 + self.y**2)**0.5

p = Point(3, 4)
print(p)              # Point(x=3, y=4)  — __repr__ for free
print(p.distance())   # 5.0

@dataclass(order=True, frozen=True)   # frozen = immutable
class Card:
    rank: int
    suit: str

    def __str__(self):
        ranks = {11:'J',12:'Q',13:'K',14:'A'}
        r = ranks.get(self.rank, str(self.rank))
        return f"{r}{self.suit}"

c1 = Card(14, "♠")
c2 = Card(7, "♥")
print(c1 > c2)   # True (order=True gives comparison for free)
# c1.rank = 5    # FrozenInstanceError

@dataclass
class Deck:
    cards: List[Card] = field(default_factory=list)
    name: str = "Standard Deck"
    _size: int = field(init=False, repr=False)  # computed, hidden

    def __post_init__(self):          # runs after __init__
        self._size = len(self.cards)

    def add(self, card: Card):
        self.cards.append(card)
        self._size += 1

deck = Deck()
deck.add(Card(14,"♠"))
deck.add(Card(7,"♥"))
print(deck)
print(asdict(deck))   # convert to dict
```

---

## 10. Design Patterns

### Singleton
```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, val):
        self.val = val

a = Singleton(1)
b = Singleton(2)
print(a is b)      # True — same object
print(a.val)       # 2 — b overwrote it
```

### Factory
```python
class Notification:
    def send(self, msg): raise NotImplementedError

class Email(Notification):
    def send(self, msg): return f"Email: {msg}"

class SMS(Notification):
    def send(self, msg): return f"SMS: {msg}"

class Push(Notification):
    def send(self, msg): return f"Push: {msg}"

class NotificationFactory:
    _types = {"email": Email, "sms": SMS, "push": Push}

    @classmethod
    def create(cls, kind: str) -> Notification:
        if kind not in cls._types:
            raise ValueError(f"Unknown type: {kind}")
        return cls._types[kind]()

n = NotificationFactory.create("sms")
print(n.send("Hello!"))   # SMS: Hello!
```

### Observer
```python
class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args, **kwargs):
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)

    def off(self, event, callback):
        if event in self._listeners:
            self._listeners[event].remove(callback)


emitter = EventEmitter()

def on_login(user):
    print(f"Welcome {user}")

def log_login(user):
    print(f"[LOG] {user} logged in")

emitter.on("login", on_login)
emitter.on("login", log_login)
emitter.emit("login", "Alice")
# Welcome Alice
# [LOG] Alice logged in
```

### Decorator Pattern
```python
class Coffee:
    def cost(self): return 5
    def desc(self): return "Coffee"

class MilkDecorator:
    def __init__(self, coffee): self._coffee = coffee
    def cost(self): return self._coffee.cost() + 2
    def desc(self): return self._coffee.desc() + " + Milk"

class SugarDecorator:
    def __init__(self, coffee): self._coffee = coffee
    def cost(self): return self._coffee.cost() + 1
    def desc(self): return self._coffee.desc() + " + Sugar"

c = Coffee()
c = MilkDecorator(c)
c = SugarDecorator(c)
c = MilkDecorator(c)

print(c.desc())   # Coffee + Milk + Sugar + Milk
print(c.cost())   # 10
```

### Strategy
```python
from typing import Protocol

class SortStrategy(Protocol):
    def sort(self, data: list) -> list: ...

class BubbleSort:
    def sort(self, data):
        d = data[:]
        for i in range(len(d)):
            for j in range(len(d)-i-1):
                if d[j] > d[j+1]: d[j],d[j+1] = d[j+1],d[j]
        return d

class QuickSort:
    def sort(self, data):
        if len(data) <= 1: return data
        pivot = data[len(data)//2]
        left  = [x for x in data if x < pivot]
        mid   = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + mid + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

sorter = Sorter(QuickSort())
print(sorter.sort([5,3,1,4,2]))    # [1,2,3,4,5]
sorter.set_strategy(BubbleSort())
print(sorter.sort([5,3,1,4,2]))    # [1,2,3,4,5]
```

---

## 11. Slots — Memory Optimization

```python
import sys

class NormalClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedClass:
    __slots__ = ['x', 'y']   # no __dict__, fixed attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = NormalClass(1, 2)
s = SlottedClass(1, 2)

print(sys.getsizeof(n))              # ~48 bytes
print(sys.getsizeof(s))              # ~56 bytes (slot descriptor)
print(sys.getsizeof(n.__dict__))     # ~232 bytes extra!
# s.__dict__                         # AttributeError — no dict

# slots are faster attribute access + less memory
# trade-off: can't add new attributes dynamically
```

---

## 12. Metaclasses — Classes that make Classes

```python
# everything in Python is an object, including classes
# type is the metaclass of all classes

print(type(int))     # <class 'type'>
print(type(str))     # <class 'type'>
print(type(list))    # <class 'type'>

# create a class dynamically with type
Dog = type("Dog", (object,), {
    "sound": "Woof",
    "speak": lambda self: f"{self.__class__.__name__} says {self.sound}"
})
print(Dog().speak())  # Dog says Woof

# custom metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self, url):
        self.url = url

db1 = Database("postgres://localhost/app")
db2 = Database("postgres://localhost/other")
print(db1 is db2)    # True
print(db1.url)       # postgres://localhost/app

# __init_subclass__ — run code when a class is subclassed
class Plugin:
    _registry = {}

    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin._registry[name or cls.__name__] = cls

class AuthPlugin(Plugin, name="auth"):
    def run(self): return "Auth running"

class CachePlugin(Plugin, name="cache"):
    def run(self): return "Cache running"

print(Plugin._registry)
# {'auth': <class 'AuthPlugin'>, 'cache': <class 'CachePlugin'>}
print(Plugin._registry["auth"]().run())  # Auth running
```

---
# Data Structures & Algorithms in Python 🧠

---

## 1. Arrays & Dynamic Arrays (Lists under the hood)

```python
# Python list IS a dynamic array — doubles capacity when full
# O(1) access, O(n) insert at beginning, O(1) amortized append

arr = [1, 2, 3, 4, 5]

# access      O(1)
print(arr[2])

# append      O(1) amortized
arr.append(6)

# insert at i O(n) — shifts everything right
arr.insert(0, 0)

# delete      O(n)
arr.pop(0)

# search      O(n)
print(3 in arr)

# slice creates a NEW list O(k)
sub = arr[1:4]

# --- 2D array ---
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])  # 6

# flatten
flat = [val for row in matrix for val in row]
```

---

## 2. Linked List (built from scratch)

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):              # O(n)
        node = Node(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def prepend(self, val):             # O(1)
        node = Node(val)
        node.next = self.head
        self.head = node

    def delete(self, val):              # O(n)
        if not self.head: return
        if self.head.val == val:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return
            cur = cur.next

    def to_list(self):
        result, cur = [], self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def reverse(self):                  # O(n)
        prev, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

ll = LinkedList()
for v in [1,2,3,4,5]: ll.append(v)
ll.reverse()
print(ll.to_list())  # [5,4,3,2,1]
```

---

## 3. Doubly Linked List

```python
class DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):              # O(1) — we have tail
        node = DNode(val)
        if not self.tail:
            self.head = self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def pop(self):                      # O(1)
        if not self.tail: return
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val

    def to_list(self):
        result, cur = [], self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

dll = DoublyLinkedList()
for v in [10,20,30,40]: dll.append(v)
print(dll.pop())       # 40
print(dll.to_list())   # [10,20,30]
```

---

## 4. Stack

```python
# Stack = LIFO
class Stack:
    def __init__(self):
        self._data = []

    def push(self, val):    # O(1)
        self._data.append(val)

    def pop(self):          # O(1)
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self):         # O(1)
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

s = Stack()
s.push(1); s.push(2); s.push(3)
print(s.pop())   # 3
print(s.peek())  # 2

# --- Real use: balanced parentheses ---
def is_balanced(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("({[]})"))   # True
print(is_balanced("({[})"))    # False
```

---

## 5. Queue & Deque

```python
from collections import deque

# Queue = FIFO
class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, val):  # O(1)
        self._data.append(val)

    def dequeue(self):       # O(1) — THIS is why we use deque not list
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.popleft()

    def peek(self):
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

q = Queue()
q.enqueue("a"); q.enqueue("b"); q.enqueue("c")
print(q.dequeue())  # a
print(q.dequeue())  # b

# Deque — both ends O(1)
dq = deque([1,2,3])
dq.appendleft(0)     # [0,1,2,3]
dq.append(4)         # [0,1,2,3,4]
dq.popleft()         # 0
dq.pop()             # 4
print(dq)            # deque([1,2,3])

# sliding window max using deque
def sliding_window_max(nums, k):
    dq, result = deque(), []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))
# [3,3,5,5,6,7]
```

---

## 6. Hash Map (Dict internals + custom)

```python
# Python dict = hash map, O(1) avg get/set/delete

# --- build one from scratch ---
class HashMap:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, val):            # O(1) avg
        idx = self._hash(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                pair[1] = val
                return
        self.buckets[idx].append([key, val])

    def get(self, key):                 # O(1) avg
        idx = self._hash(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):              # O(1) avg
        idx = self._hash(key)
        self.buckets[idx] = [p for p in self.buckets[idx] if p[0] != key]

hm = HashMap()
hm.set("name", "Alice")
hm.set("age", 25)
print(hm.get("name"))  # Alice
hm.delete("age")
print(hm.get("age"))   # None

# --- collections.Counter (dict on steroids) ---
from collections import Counter, defaultdict

words = ["apple","banana","apple","cherry","banana","apple"]
count = Counter(words)
print(count)                    # Counter({'apple': 3, ...})
print(count.most_common(2))     # [('apple',3),('banana',2)]

# defaultdict — no KeyError
graph = defaultdict(list)
graph["a"].append("b")
graph["a"].append("c")
print(graph["a"])   # ['b','c']
print(graph["z"])   # []  — no error
```

---

## 7. Binary Tree

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# build a tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# --- Traversals ---
def inorder(node):      # Left Root Right  → sorted for BST
    if not node: return
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)

def preorder(node):     # Root Left Right
    if not node: return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)

def postorder(node):    # Left Right Root
    if not node: return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=" ")

def level_order(root):  # BFS level by level
    from collections import deque
    if not root: return []
    q, result = deque([root]), []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result

inorder(root)               # 4 2 5 1 3 6
print()
print(level_order(root))    # [[1],[2,3],[4,5,6]]

# tree height
def height(node):
    if not node: return 0
    return 1 + max(height(node.left), height(node.right))

print(height(root))  # 3
```

---

## 8. Binary Search Tree (BST)

```python
class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):                      # O(log n) avg
        def _insert(node, val):
            if not node: return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            elif val > node.val:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def search(self, val):                      # O(log n) avg
        def _search(node, val):
            if not node: return False
            if val == node.val: return True
            if val < node.val: return _search(node.left, val)
            return _search(node.right, val)
        return _search(self.root, val)

    def delete(self, val):                      # O(log n) avg
        def _min(node):
            while node.left: node = node.left
            return node

        def _delete(node, val):
            if not node: return None
            if val < node.val:
                node.left = _delete(node.left, val)
            elif val > node.val:
                node.right = _delete(node.right, val)
            else:
                if not node.left: return node.right
                if not node.right: return node.left
                successor = _min(node.right)
                node.val = successor.val
                node.right = _delete(node.right, successor.val)
            return node
        self.root = _delete(self.root, val)

bst = BST()
for v in [5,3,7,1,4,6,8]: bst.insert(v)
print(bst.search(4))   # True
print(bst.search(9))   # False
bst.delete(3)
inorder(bst.root)      # 1 4 5 6 7 8
```

---

## 9. Heap / Priority Queue

```python
import heapq

# Python heapq = min-heap by default
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

print(heapq.heappop(heap))   # 1  (smallest)
print(heapq.heappop(heap))   # 3

# heapify in O(n)
nums = [4, 1, 7, 3, 8, 2]
heapq.heapify(nums)
print(nums[0])   # 1 (min is always at index 0)

# max-heap trick: negate values
max_heap = []
for n in [4,1,7,3]: heapq.heappush(max_heap, -n)
print(-heapq.heappop(max_heap))  # 7

# nlargest / nsmallest
nums = [4,1,7,3,8,2,9,5]
print(heapq.nlargest(3, nums))   # [9,8,7]
print(heapq.nsmallest(3, nums))  # [1,2,3]

# --- K most frequent elements ---
def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count, key=count.get)

print(top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]
```

---

## 10. Graph — Adjacency List

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, w=1):
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))

    def bfs(self, start):               # O(V+E)
        visited, queue, order = {start}, deque([start]), []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nei, _ in self.adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        return order

    def dfs(self, start):               # O(V+E)
        visited, order = set(), []
        def _dfs(node):
            visited.add(node)
            order.append(node)
            for nei, _ in self.adj[node]:
                if nei not in visited:
                    _dfs(nei)
        _dfs(start)
        return order

    def has_cycle(self):                # undirected only
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for nei, _ in self.adj[node]:
                if nei not in visited:
                    if dfs(nei, node): return True
                elif nei != parent:
                    return True
            return False
        for node in self.adj:
            if node not in visited:
                if dfs(node, -1): return True
        return False

g = Graph()
for u,v in [(1,2),(1,3),(2,4),(3,4),(4,5)]:
    g.add_edge(u, v)

print(g.bfs(1))   # [1,2,3,4,5]
print(g.dfs(1))   # [1,2,4,3,5]  (order may vary)
print(g.has_cycle())  # True (1-2-4-3-1)
```

---

## 11. Dijkstra's Shortest Path

```python
import heapq

def dijkstra(graph, start):             # O((V+E) log V)
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]    # (cost, node)

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for nei, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[nei]:
                dist[nei] = new_cost
                heapq.heappush(heap, (new_cost, nei))

    return dist

g = defaultdict(list)
edges = [(1,2,4),(1,3,1),(3,2,2),(2,4,1),(3,4,5)]
for u, v, w in edges:
    g[u].append((v, w))
    g[v].append((u, w))

print(dijkstra(g, 1))
# {1:0, 2:3, 3:1, 4:4}
```

---

## 12. Sorting Algorithms

```python
# --- Bubble Sort O(n²) ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# --- Merge Sort O(n log n) ---
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(l, r):
    result, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i]); i += 1
        else:
            result.append(r[j]); j += 1
    return result + l[i:] + r[j:]

# --- Quick Sort O(n log n) avg ---
def quick_sort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo >= hi: return
    pivot = partition(arr, lo, hi)
    quick_sort(arr, lo, pivot - 1)
    quick_sort(arr, pivot + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i + 1

arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr[:]))   # [11,12,22,25,34,64,90]
quick_sort(arr)
print(arr)                  # [11,12,22,25,34,64,90]
```

---

## 13. Binary Search

```python
# O(log n) — array MUST be sorted

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:   return mid
        elif arr[mid] < target:  lo = mid + 1
        else:                    hi = mid - 1
    return -1

print(binary_search([1,3,5,7,9,11,13], 7))   # 3
print(binary_search([1,3,5,7,9,11,13], 6))   # -1

# find leftmost position
def bisect_left(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target: lo = mid + 1
        else: hi = mid
    return lo

# search in rotated sorted array
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        if nums[lo] <= nums[mid]:           # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                               # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

print(search_rotated([4,5,6,7,0,1,2], 0))  # 4
```

---

## 14. Dynamic Programming

```python
# --- Fibonacci (memoization) ---
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

print([fib(i) for i in range(10)])  # [0,1,1,2,3,5,8,13,21,34]

# --- Fibonacci (tabulation) ---
def fib_tab(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

# --- Longest Common Subsequence ---
def lcs(a, b):                          # O(mn)
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(lcs("abcde", "ace"))  # 3

# --- 0/1 Knapsack ---
def knapsack(weights, values, capacity):    # O(n * capacity)
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w],
                               values[i-1] + dp[i-1][w - weights[i-1]])
    return dp[n][capacity]

print(knapsack([2,3,4,5], [3,4,5,6], 8))  # 10

# --- Coin Change ---
def coin_change(coins, amount):             # O(amount * coins)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1,5,6,9], 11))  # 2  (5+6)
```

---

## 15. Trie (Prefix Tree)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):             # O(m)
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):             # O(m)
        node = self.root
        for ch in word:
            if ch not in node.children: return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):      # O(m)
        node = self.root
        for ch in prefix:
            if ch not in node.children: return False
            node = node.children[ch]
        return True

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children: return []
            node = node.children[ch]
        results = []
        def dfs(node, path):
            if node.is_end: results.append(prefix + path)
            for ch, child in node.children.items():
                dfs(child, path + ch)
        dfs(node, "")
        return results

t = Trie()
for w in ["apple","app","application","apply","banana"]:
    t.insert(w)

print(t.search("app"))          # True
print(t.starts_with("appl"))    # True
print(t.autocomplete("app"))    # ['app','apple','application','apply']
```

---

## 16. Union Find (Disjoint Set)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):              # O(α(n)) ≈ O(1)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):          # O(α(n)) ≈ O(1)
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(6)
uf.union(0,1); uf.union(1,2); uf.union(3,4)
print(uf.connected(0, 2))   # True
print(uf.connected(0, 3))   # False
print(uf.components)        # 3

# --- detect cycle in undirected graph using UF ---
def has_cycle(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return True
    return False

print(has_cycle(4, [(0,1),(1,2),(2,3),(3,1)]))  # True
```

---

## 17. Complexity Cheat Sheet

```
Structure         | Access | Search | Insert | Delete
------------------|--------|--------|--------|-------
Array/List        | O(1)   | O(n)   | O(n)   | O(n)
Linked List       | O(n)   | O(n)   | O(1)*  | O(1)*
Stack/Queue       | O(n)   | O(n)   | O(1)   | O(1)
Hash Map          | -      | O(1)   | O(1)   | O(1)
BST (balanced)    | O(logn)| O(logn)| O(logn)| O(logn)
Heap              | O(1)** | O(n)   | O(logn)| O(logn)
Trie              | O(m)   | O(m)   | O(m)   | O(m)

* at known position
** only min/max

Algorithm         | Best     | Average  | Worst    | Space
------------------|----------|----------|----------|-------
Bubble Sort       | O(n)     | O(n²)    | O(n²)    | O(1)
Merge Sort        | O(nlogn) | O(nlogn) | O(nlogn) | O(n)
Quick Sort        | O(nlogn) | O(nlogn) | O(n²)    | O(logn)
Binary Search     | O(1)     | O(logn)  | O(logn)  | O(1)
BFS / DFS         | O(V+E)   | O(V+E)   | O(V+E)   | O(V)
Dijkstra          | -        | O((V+E)logV) | -    | O(V)
```

---


