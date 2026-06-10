# 🐍 Python Lists — Grand Final Test
### 50 Questions | Time Limit: 1 Hour 30 Minutes
> Rules: For bug questions identify the bug AND write the fix. For coding questions write the full solution.

---

## Section 1: Bug Fixing (2 points each)
*Find the bug and write the corrected code.*

**Q1.**
```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}. {fruit}")
# Expected output:
# 1. apple
# 2. banana
# 3. cherry
```

**Q2.**
```python
numbers = [5, 3, 8, 1, 9]
numbers.sort(reverse=False)
print(numbers)
# Expected: [9, 8, 5, 3, 1]
```

**Q3.**
```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)
# Expected: [1, 2, 3]  (a should be unchanged)
```

**Q4.**
```python
items = [1, 2, 3, 2, 4, 2]
while 2 in items:
    items.remove(items)
print(items)
# Expected: [1, 3, 4]
```

**Q5.**
```python
names = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]
for name, score in zip(names, scores):
    print(name + score)
# Expected:
# Alice 88
# Bob 92
# Charlie 75
```

**Q6.**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for num in matrix for row in matrix]
print(flat)
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Q7.**
```python
words = ["Python", "is", "great"]
sentence = words.join(" ")
print(sentence)
# Expected: Python is great
```

**Q8.**
```python
nums = [1, 2, 3, 4, 5]
first, last = nums
print(first, last)
# Expected: 1 5
```

**Q9.**
```python
numbers = [4, 7, 2, 9, 1, 5]
second_largest = sorted(numbers)[1]
print(second_largest)
# Expected: 7
```

**Q10.**
```python
data = [5, None, 3, None, 8, None, 1]
result = [x for x in data if x != None]
# Expected to also work when None appears as 0 or False
# Hint: there is a more Pythonic way to check for None
```

---

## Section 2: Fill in the Blank (2 points each)
*Fill in the `???` to make the code work as described.*

**Q11.** Remove the first AND last item using one slice:
```python
nums = [0, 1, 2, 3, 4, 5, 9]
nums = nums[???]
print(nums)  # [1, 2, 3, 4, 5]
```

**Q12.** Make this produce `[1, 3, 5, 7, 9]`:
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[???])
```

**Q13.** Complete the list comprehension to get words longer than 5 characters in uppercase:
```python
words = ["hello", "hi", "python", "programming", "code"]
result = [???.upper() for ??? in words if len(???) > 5]
print(result)  # ['PYTHON', 'PROGRAMMING']
```

**Q14.** Use one built-in function to find the longest word by length:
```python
words = ["cat", "elephant", "dog", "butterfly"]
longest = ???(words, key=len)
print(longest)  # butterfly
```

**Q15.** Fill in to check if ALL numbers in the list are even:
```python
nums = [2, 4, 6, 8, 10]
print(???(num % 2 == 0 for num in nums))
```

**Q16.** Use `enumerate()` to print items with position starting from 1, but only for items at odd positions (1, 3, 5...):
```python
items = ["a", "b", "c", "d", "e", "f"]
for i, item in enumerate(items, ???):
    if i % 2 == ???:
        print(i, item)
# Expected:
# 1 a
# 3 c
# 5 e
```

**Q17.** Complete the unpacking so `rest` contains the middle items:
```python
data = [1, 2, 3, 4, 5, 6, 7]
first, ???, last = data
print(rest)  # [2, 3, 4, 5, 6]
```

**Q18.** Make this combine the two lists in alternating order `[1, 4, 2, 5, 3, 6]`:
```python
a = [1, 2, 3]
b = [4, 5, 6]
result = [num for pair in ???(a, b) for num in ???]
print(result)
```

---

## Section 3: Code Writing (3 points each)
*Write the full solution.*

**Q19.** Given `pairs = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]`, use a list comprehension to extract only the names where the score is above 88.

**Q20.** Given `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, write a single line that gives you the sum of squares of even numbers only.

**Q21.** Given two lists `keys = ["name", "age", "city"]` and `values = ["Alice", 25, "Nairobi"]`, use `zip()` to print each key-value pair like:
```
name: Alice
age: 25
city: Nairobi
```

**Q22.** Given `sentence = "the quick brown fox"`, split it into a list of words, capitalize each word using a list comprehension, then join them back into a single string.

**Q23.** Given `numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]`, without modifying the original list, print a sorted version. Then prove the original is unchanged by printing it after.

**Q24.** Given this nested list, use a list comprehension to extract all scores above 80:
```python
students = [
    ["Alice", 90, 75],
    ["Bob", 85, 60],
    ["Charlie", 70, 95]
]
# Expected: [90, 85, 95]
```

**Q25.** Given `items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]`, return a new list of unique items in their original order without using `set()`.

**Q26.** Given `nums = [1, 2, 3, 4, 5]`, use list unpacking to swap the first and last items so the list becomes `[5, 2, 3, 4, 1]`.

**Q27.** Given `matrix = [[1,2,3],[4,5,6],[7,8,9]]`, use a list comprehension to extract the middle column (index 1 of each row): `[2, 5, 8]`.

**Q28.** Given `words = ["banana", "Apple", "cherry", "Mango"]`, sort them alphabetically ignoring case so uppercase and lowercase words are not separated.

**Q29.** Given `data = [1, "two", 3, "four", 5, "six"]`, use list comprehensions to separate it into two lists — one with only integers and one with only strings.

**Q30.** Given `scores = [55, 82, 90, 47, 73, 88, 61, 95]`, use a list comprehension to replace any score below 60 with the string `"fail"` and keep the rest unchanged.

---

## Section 4: Tricky & Combined Concepts (3 points each)

**Q31.** You have a list of numbers. Write code that splits it into two lists — one with numbers at even indexes and one with numbers at odd indexes:
```python
nums = [10, 20, 30, 40, 50, 60, 70, 80]
# even_indexes = [10, 30, 50, 70]
# odd_indexes =  [20, 40, 60, 80]
```

**Q32.** Given `rows = [[1,2,3],[4,5,6],[7,8,9]]`, use a list comprehension with `enumerate()` to get the diagonal elements `[1, 5, 9]`.

**Q33.** Given:
```python
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
```
Write a list comprehension that returns items that appear in both lists: `[4, 5]`.

**Q34.** Given `names = ["alice", "bob", "charlie", "david", "eve"]`, use `enumerate()` and a list comprehension to return only the names at even indexes (0, 2, 4).

**Q35.** Given:
```python
prices = [100, 250, 75, 300, 150]
```
Use a list comprehension to apply a 10% discount to any price above 200 and keep the rest unchanged.

**Q36.** Given `words = ["the", "quick", "brown", "fox"]`, use `zip()` to pair each word with the next word in the list like:
```
the - quick
quick - brown
brown - fox
```
Hint: think about how to use the same list twice with different starting points.

**Q37.** Given `nums = [1, 2, 3, 4, 5]`, without using `reverse()` or `[::-1]`, use a list comprehension with `range()` to reverse the list.

**Q38.** Given:
```python
students = [
    ["Alice", [85, 90, 78]],
    ["Bob", [70, 65, 80]],
    ["Charlie", [95, 88, 92]]
]
```
Use a list comprehension to return a list of names where the student's average score is above 80.

**Q39.** You have a list of sentences. Use a list comprehension to return a flat list of all individual words:
```python
sentences = ["hello world", "python is great", "lists are fun"]
# Expected: ["hello", "world", "python", "is", "great", "lists", "are", "fun"]
```

**Q40.** Given `stack = [1, 2, 3, 4, 5]`, simulate a queue — remove from the front and add to the back. Process these operations in order:
- Remove the first item and print it
- Add 6 to the end
- Remove the first item and print it
- Print the final list

**Q41.** Given two lists of equal length, use `zip()` and a list comprehension to return a new list where each item is the **sum** of the corresponding items:
```python
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
# Expected: [11, 22, 33, 44]
```

**Q42.** Given `nums = [4, 7, 2, 9, 1, 5]`, find the second largest number using only list methods and built-in functions — no sorting allowed.

**Q43.** Given a list of words, use `enumerate()` and `zip()` together to print each word alongside its reverse:
```python
words = ["hello", "world", "python"]
# Expected:
# 1. hello - olleh
# 2. world - dlrow
# 3. python - nohtyp
```

**Q44.** Given `data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, use a nested list comprehension to transpose it (swap rows and columns):
```python
# Expected:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
```

**Q45.** Given:
```python
inventory = [
    ["apples", 50],
    ["bananas", 10],
    ["oranges", 35],
    ["grapes", 5]
]
```
Use a list comprehension to return only the names of items where quantity is below 20, then use `join()` to print them as a comma separated string like: `bananas, grapes`

**Q46.** Given `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, use a list comprehension to group numbers into pairs: `[[1,2], [3,4], [5,6], [7,8], [9,10]]`. Hint: use `range()` with a step.

**Q47.** Given a list that may contain duplicates, write code that returns a dictionary showing how many times each item appears — using only list methods you have learned:
```python
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# Expected: {"apple": 3, "banana": 2, "cherry": 1}
```

**Q48.** Given `scores = [72, 85, 90, 61, 78, 95, 55, 88]`, use list comprehensions and `zip()` with `enumerate()` to print only the scores that are above the average, along with their position:
```
Position 2: 85
Position 3: 90
...
```

**Q49.** Given:
```python
teams = [["Alice", "Bob"], ["Charlie", "David"], ["Eve", "Frank"]]
```
Use a list comprehension to flatten this into a single list, then use `enumerate()` starting from 1 to print each person with their overall rank:
```
1. Alice
2. Bob
3. Charlie
...
```

**Q50.** Given `nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`, using only what you have learned, write code that:
1. Removes all duplicates while keeping original order
2. Sorts the result in descending order
3. Keeps only numbers greater than 3
4. Prints the final result

---

## Grading Scale
| Score | Grade |
|---|---|
| 135 - 150 pts | A+ 🏆 |
| 120 - 134 pts | A 🥇 |
| 105 - 119 pts | B 🥈 |
| 90 - 104 pts | C 🥉 |
| Below 90 pts | Need more practice 📚 |

---
*Total Points: 150 | Time: 1hr 30min | Good luck! 🚀*