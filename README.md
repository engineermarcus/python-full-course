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
