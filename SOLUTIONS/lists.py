# q1 

fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

# q2 

numbers = [5, 3, 8, 1, 9]
numbers.sort(reverse=True)
print(numbers)

# q3 

a = [1, 2, 3]
b = a.copy()
b[0] = 99
print(a)
# q4

items = [1, 2, 3, 2, 4, 2]
while 2 in items:
    items.remove(2)
print(items)
# q5

names = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]
for name, score in zip(names, scores):
    print(f"{name} {score}")

# q6 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)

# q7

words = ["Python", "is", "great"]
sentence = " ".join(words)
print(sentence)

# q8 

nums = [1, 2, 3, 4, 5]
first, *middle ,last = nums
print(first, last)

# q9 

numbers = [4, 7, 2, 9, 1, 5]
numbers.sort()
second_largest = numbers[4]
print(second_largest)

# q10 

data = [5, None, 3, None, 8, None, 1]
result = [x for x in data if x != None]
print(result)

# q11


nums = [0, 1, 2, 3, 4, 5, 9]
nums = nums[1:6]
print(nums)  # [1, 2, 3, 4, 5]
# q12

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# q13

words = ["hello", "hi", "python", "programming", "code"]
result = [word.upper() for word in words if len(word) > 5]
print(result)  # ['PYTHON', 'PROGRAMMING']

# q14 

words = ["cat", "elephant", "dog", "butterfly"]
longest = max(words, key=len)
print(longest)  # butterfly

# q15 

nums = [2, 4, 6, 8, 10]
print(all(num % 2 == 0 for num in nums))

# q16 

items = ["a", "b", "c", "d", "e", "f"]
for i, item in enumerate(items, 1):
    if i % 2 == 1:
        print(i, item)
# Expected:
# 1 a
# 3 c
# 5 e

# q17

data = [1, 2, 3, 4, 5, 6, 7]
first, *rest, last = data
print(rest)  # [2, 3, 4, 5, 6]

# q18 
"""
a = [1, 2, 3]
b = [4, 5, 6]
result = [num for pair in ???(a, b) for num in ???]
print(result)

"""

# q19

pairs = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]

print([score[0] for score in pairs if score[1] > 88])

# q20 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([num * num  for num in nums if num % 2 == 0])

# 21

keys = ["name", "age", "city"]
values = ["Alice", 25, "Nairobi"]

for key, value in zip(keys, values):
    print(f"{key}: {value}")

# q22

sentence = "the quick brown fox"
ls = sentence.split()
capital = [word.upper() for word in ls]
s = " ".join(capital)
print(s)

# q23

numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]
numbers.sort()
b = numbers.copy()
b[0] = 99
print(numbers)
print(b)

# q24 

students = [
    ["Alice", 90, 75],
    ["Bob", 85, 60],
    ["Charlie", 70, 95]
]
scores = []

for ls in students:
    new_list = ls[1:3]
    for score in new_list:
        if score > 80:
            scores.append(score)
print(scores)

# 25 

items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
while i not in items:
    items.pop(i) 
print(items)

# 26 


nums = [1, 2, 3, 4, 5]

first, *mid, last = nums

mid.append(first)
mid.insert(0, last)
print(mid)

# 27 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
new_list = []
for row in matrix:
    new_list.append(row[1])
print(new_list)

# q28

words = ["banana", "Apple", "cherry", "Mango"]
low = []
for word in words:
    low.append(word.lower())
result = sorted(low)
print(result)

# q29 


data = [1, "two", 3, "four", 5, "six"]

integers = []
strings = []

for i in data:
    if type(i) == int:
        integers.append(i)
    elif type(i) == str:
        strings.append(i)
print(integers)
print(strings)

# q30

scores = [55, 82, 90, 47, 73, 88, 61, 95]
low_scores = []
total_scores = []
for score in scores:
    if score < 60:
        scores.remove(score)
        low_scores.append("fail")
high_scores = scores
matrix = [high_scores,low_scores]
for row in matrix:
    for col in row:
        total_scores.append(col)

print(total_scores)

# q31 

nums = [10, 20, 30, 40, 50, 60, 70, 80]
even_indexes  = []
odd_indexes = []
for i, num in enumerate(nums):
    if i % 2 == 0:
        even_indexes.append(num)
    elif i % 2 == 1:
        odd_indexes.append(num)
print(even_indexes)
print(odd_indexes)


# q32

rows = [[1,2,3],[4,5,6],[7,8,9]]
elements = []
for k, row in enumerate(rows):
    if k == 0:
        for i, col in enumerate(row):
            if i == 0:
                elements.append(col)
    elif k == 1:
         for i, col in enumerate(row):
            if i == 1:
                elements.append(col)
    elif k == 2:
         for i, col in enumerate(row):
            if i == 2:
                elements.append(col)

print(elements)

