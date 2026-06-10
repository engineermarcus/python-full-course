# 🐍 Python Lists — Grand Final Test
### 50 Questions | Time Limit: 1 Hour 30 Minutes
> Rules: No running code first. Write your answers, then verify. For output questions write exactly what prints. For bug questions identify the bug AND write the fix.

---

## Section 1: Output Prediction (1 point each)
*What does this code print? If it throws an error, write the error name.*

**Q1.**
```python
data = [10, 20, 30, 40, 50]
print(data[-2] + data[1])
```

**Q2.**
```python
nums = [1, 2, 3, 4, 5]
print(nums[1:4:2])
```

**Q3.**
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

**Q4.**
```python
items = [5, 3, 8, 1, 9]
items.sort()
print(items[-1])
```

**Q5.**
```python
words = ["hello", "world"]
words.insert(1, "beautiful")
print(words[2])
```

**Q6.**
```python
nums = [1, 2, 3, 4, 5]
print(nums[::- 1])
```

**Q7.**
```python
letters = ["a", "b", "c", "d", "e"]
print(letters[1:-1])
```

**Q8.**
```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
```

**Q9.**
```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(nums.count(1) + nums.index(4))
```

**Q10.**
```python
data = [[1, 2], [3, 4], [5, 6]]
print(data[1][0] + data[0][1])
```

---

## Section 2: Bug Fixing (2 points each)
*Find the bug and write the corrected code.*

**Q11.**
```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}. {fruit}")
# Expected output:
# 1. apple
# 2. banana
# 3. cherry
```

**Q12.**
```python
numbers = [5, 3, 8, 1, 9]
numbers.sort(reverse = False)
print(numbers)
# Expected: [9, 8, 5, 3, 1]
```

**Q13.**
```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)
# Expected: [1, 2, 3]  (a should be unchanged)
```

**Q14.**
```python
items = [1, 2, 3, 2, 4, 2]
while 2 in items:
    items.remove(items)
print(items)
# Expected: [1, 3, 4]
```

**Q15.**
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

**Q16.**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for num in matrix for row in matrix]
print(flat)
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Q17.**
```python
words = ["Python", "is", "great"]
sentence = words.join(" ")
print(sentence)
# Expected: "Python is great"
```

**Q18.**
```python
nums = [1, 2, 3, 4, 5]
first, last = nums
print(first, last)
# Expected: 1 5
```

---

## Section 3: Fill in the Blank (2 points each)
*Fill in the `???` to make the code work as described.*

**Q19.** Remove the first AND last item from the list using one line of slicing:
```python
nums = [0, 1, 2, 3, 4, 5, 9]
nums = nums[???]
print(nums)  # [1, 2, 3, 4, 5]
```

**Q20.** Make this produce `[1, 3, 5, 7, 9]`:
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[???])
```

**Q21.** Complete the list comprehension to get words longer than 5 characters in uppercase:
```python
words = ["hello", "hi", "python", "programming", "code"]
result = [???.upper() for ??? in words if len(???) > 5]
print(result)  # ['PYTHON', 'PROGRAMMING']
```

**Q22.** Use one built-in function to find the longest word (by length):
```python
words = ["cat", "elephant", "dog", "butterfly"]
longest = ???(words, key=len)
print(longest)  # "butterfly"
```

**Q23.** Fill in to check if ALL numbers in the list are even:
```python
nums = [2, 4, 6, 8, 10]
print(???(??? % 2 == 0 for num in nums))
```

---

## Section 4: Code Writing (3 points each)
*Write the full solution.*

**Q24.** Given `pairs = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]`, use a list comprehension to extract only the names where the score is above 88.

**Q25.** Given `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, write a single line that gives you the sum of squares of even numbers only.

**Q26.** Given two lists `keys = ["name", "age", "city"]` and `values = ["Alice", 25, "Nairobi"]`, use `zip()` to print each key-value pair like:
```
name: Alice
age: 25
city: Nairobi
```

**Q27.** Given `sentence = "the quick brown fox"`, split it into a list of words, capitalize each word using a list comprehension, then join them back into a string.

**Q28.** Given `numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]`, without sorting the original list, print a sorted version of it. Then prove the original is unchanged by printing it after.

**Q29.** Given this nested list, use a list comprehension to extract all scores above 80:
```python
students = [
    ["Alice", 90, 75],
    ["Bob", 85, 60],
    ["Charlie", 70, 95]
]
# Expected: [90, 85, 95]
```

**Q30.** Given `items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]`, return a new list of unique items in their **original order** without using `set()`.

**Q31.** Given `nums = [1, 2, 3, 4, 5]`, use list unpacking to swap the first and last items so the list becomes `[5, 2, 3, 4, 1]`.

**Q32.** Given `matrix = [[1,2,3],[4,5,6],[7,8,9]]`, use a list comprehension to extract the **middle column** (index 1 of each row): `[2, 5, 8]`.

**Q33.** Given `words = ["banana", "Apple", "cherry", "Mango"]`, sort them alphabetically **ignoring case** so uppercase and lowercase words aren't separated.

**Q34.** Given `data = [1, "two", 3, "four", 5, "six"]`, use a list comprehension to separate it into two lists — one with only integers and one with only strings.

**Q35.** Given `scores = [55, 82, 90, 47, 73, 88, 61, 95]`, use a list comprehension to replace any score below 60 with the string `"fail"` and keep the rest as they are.

---

## Section 5: Tricky & Combined Concepts (3 points each)

**Q36.** What is the output?
```python
nums = [1, 2, 3, 4, 5]
nums[1:3] = [20, 30, 40]
print(nums)
```

**Q37.** What is the output?
```python
a = [1, 2, 3]
b = a.copy()
a.append(4)
print(len(a) == len(b))
```

**Q38.** What is the output?
```python
first, *rest = [10, 20, 30, 40, 50]
print(sum(rest))
```

**Q39.** What is the output?
```python
words = ["hi", "hello", "hey"]
print(sorted(words, key=len))
```

**Q40.** What is the output?
```python
nums = [1, 2, 3, 4, 5]
print(nums[::-1][1:3])
```

**Q41.** Write a single line of code that takes this list and returns the second largest number **without sorting**:
```python
nums = [4, 7, 2, 9, 1, 5]
```

**Q42.** Given `rows = [[1,2,3],[4,5,6],[7,8,9]]`, use a list comprehension to get the **diagonal** elements `[1, 5, 9]`. Hint: think about `enumerate()`.

**Q43.** Given two lists:
```python
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
```
Write a list comprehension that returns items that appear in **both** lists: `[4, 5]`.

**Q44.** What is the output and why?
```python
nums = [1, 2, 3, 4, 5]
result = [nums.pop() for _ in range(3)]
print(result)
print(nums)
```

**Q45.** Given `data = [5, None, 3, None, 8, None, 1]`, use a list comprehension to remove all `None` values.

**Q46.** Given `names = ["alice", "bob", "charlie", "david", "eve"]`, use `enumerate()` and a list comprehension to return only the names at **even indexes** (0, 2, 4):

**Q47.** Given:
```python
prices = [100, 250, 75, 300, 150]
```
Use a list comprehension to apply a 10% discount to any price above 200, and keep the rest unchanged.

**Q48.** Given `words = ["the", "quick", "brown", "fox"]`, use `zip()` to pair each word with the **next** word in the list like:
```
the - quick
quick - brown
brown - fox
```

**Q49.** Given `nums = [1, 2, 3, 4, 5]`, without using `reverse()` or `[::-1]`, use a list comprehension with `range()` to reverse the list.

**Q50.** Given:
```python
students = [
    ["Alice", [85, 90, 78]],
    ["Bob", [70, 65, 80]],
    ["Charlie", [95, 88, 92]]
]
```
Use a list comprehension to return a list of names where the student's **average score** is above 80.

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