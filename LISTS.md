# 🐍 Python List Challenges — 100 Problems

A comprehensive collection of 100 Python list-based coding challenges ranging from beginner to advanced. Each problem includes starter data and a clear problem statement.

---

## Table of Contents

1. [Data Parsing & Sorting](#1-data-parsing--sorting)
2. [Algorithms & Search](#2-algorithms--search)
3. [Data Transformation](#3-data-transformation)
4. [Real-World Simulations](#4-real-world-simulations)

---

## Q1. Mixed-Format Timestamp Parsing

Parse and sort timestamps that arrive in mixed formats chronologically.

```python
logs = ["Jan 15 2024 10:23:45", "2024-01-15 10:23:45", "15/01/2024 10:23"]
```

> **Task:** Parse all three formats and return them sorted from earliest to latest.

---

## Q2. Pair Sum — O(n) Solution

Given a list of 10,000 integers, find all pairs that sum to a target value **without using nested loops**.

```python
numbers = [3, 7, 1, 9, 4, 11, 2, 8, 6, 5]
target = 10
```

> **Task:** Find all pairs summing to `target` in O(n) time.

---

## Q3. Multi-Key User Sort

Sort a list of user dictionaries first by `score` descending, then `age` ascending, then `name` alphabetically.

```python
users = [
    {"name": "Zara", "age": 25, "score": 90},
    {"name": "Ali",  "age": 25, "score": 90},
    {"name": "Bob",  "age": 22, "score": 95},
    {"name": "Mia",  "age": 30, "score": 90}
]
```

---

## Q4. Deep List Flattening

Flatten a nested list of arbitrary depth into a single list **without any imports**.

```python
nested = [1, [2, [3, [4, [5, [6, [7]]]]]]], 8, [9, [10]]]
```

> **Expected output:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

---

## Q5. Resilient JSON Parser

Parse a list of JSON strings where some are malformed. Extract the `data` field from valid ones and deduplicate by `id`.

```python
responses = [
    '{"id": 1, "data": "alpha"}',
    '{"id": 2, "data": "beta"}',
    'NOT JSON',
    '{"id": 1, "data": "alpha_duplicate"}',
    '{"id": 3}'
]
```

> **Task:** Return valid, deduplicated records that have a `data` field.

---

## Q6. Maximum Stock Profit

Given 30 days of stock prices, find the maximum profit from a single buy-sell transaction. You must buy before you sell.

```python
prices = [120, 130, 115, 145, 110, 160, 105, 175, 130, 150,
          140, 155, 100, 170, 125, 135, 165, 108, 180, 112,
          190, 145, 160, 115, 175, 130, 155, 125, 140, 200]
```

---

## Q7. File Grouping by Extension

Group file paths by extension, then sort each group by file size (embedded in the filename like `file_1024.txt`). Return a dict.

```python
files = ["report_2048.pdf", "image_512.png", "doc_1024.txt", "photo_2048.png",
         "readme_256.txt", "data_4096.csv", "chart_1024.pdf", "notes_512.txt"]
```

---

## Q8. Inverted Index Builder

Given a list of sentences, build an inverted index — a dict mapping each unique word to the list of sentence indices it appears in.

```python
sentences = [
    "the cat sat on the mat",
    "the dog ate the cat",
    "the mat was on the floor",
    "a cat and a dog"
]
```

---

## Q9. In-Place List Rotation

Rotate a list of integers to the right by `k` positions **in-place**, without using slicing or a second list.

```python
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

> **Expected output:** `[5, 6, 7, 1, 2, 3, 4]`

---

## Q10. Top 3 Earners Per Department

Find the top 3 earners per department from a list of employee tuples **without using pandas**.

```python
employees = [
    ("Alice", "Eng",   90000), ("Bob",   "Eng",   85000),
    ("Carol", "Eng",   95000), ("Dave",  "Eng",   80000),
    ("Eve",   "HR",    70000), ("Frank", "HR",    75000),
    ("Grace", "HR",    65000), ("Hank",  "Sales", 60000),
    ("Iris",  "Sales", 72000)
]
```

---

## Q11. Longest Zero-Sum Subarray

Find the longest subarray whose elements sum to exactly zero.

```python
arr = [3, -1, -2, 4, -3, 1, 2, -3, 3]
```

---

## Q12. Exact Page Sequence Detection

Find users who visited pages in the exact sequence `["home", "product", "checkout"]`.

```python
events = [
    (1, "home", 1), (1, "product", 2), (1, "checkout", 3),
    (2, "home", 1), (2, "checkout", 2),
    (3, "home", 1), (3, "product", 2), (3, "cart", 3), (3, "checkout", 4)
]
```

---

## Q13. Three-Way Partition

Partition a list into three sublists — negatives, zeros, positives — **in one pass**, maintaining original relative order.

```python
arr = [-3, 0, 5, -1, 0, 8, -2, 3, 0, -7, 4]
```

---

## Q14. Net Balance Sheet

Given raw transaction strings, build a net balance sheet for all parties.

```python
transactions = [
    "Alice->Bob:250", "Bob->Carol:100", "Carol->Alice:75",
    "Alice->Dave:300", "Dave->Bob:50",  "Carol->Dave:125"
]
```

---

## Q15. 90° Clockwise Matrix Rotation

Rotate a 2D list (matrix) 90 degrees clockwise **in-place**.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

> **Expected output:**
> ```
> [[7, 4, 1],
>  [8, 5, 2],
>  [9, 6, 3]]
> ```

---

## Q16. Anagram Grouping

Find all groups of anagrams within a list of words.

```python
words = ["eat", "tea", "tan", "ate", "nat", "bat", "tab",
         "arc", "car", "race", "care", "acre"]
```

---

## Q17. Merge Overlapping Intervals

Merge all overlapping intervals from a list of `[start, end]` pairs.

```python
intervals = [[1, 3], [2, 6], [8, 10], [7, 12], [15, 18], [16, 20]]
```

> **Expected output:** `[[1, 6], [7, 12], [15, 20]]`

---

## Q18. Minimum Moves to Equalize

Find the minimum number of moves to make all elements equal, where one move increments or decrements one element by 1.

```python
arr = [1, 10, 2, 9, 3]
```

> **Hint:** The optimal target is the median.

---

## Q19. Missing Number via XOR

Given a list of `n` integers from 1 to `n+1` with exactly one number missing, find the missing number **using bitwise XOR only**.

```python
arr = [1, 2, 4, 5, 6, 7, 8, 9, 10]  # missing 3, n+1 = 10
```

---

## Q20. Longest Two-User Chat Streak

Find the longest conversation streak between exactly two users — consecutive messages alternating between them.

```python
messages = [
    ("A", "hi",         1), ("B", "hey",  2),
    ("A", "how are you",3), ("B", "good", 4),
    ("C", "yo",         5), ("A", "cool", 6),
    ("B", "nice",       7), ("A", "bye",  8)
]
```

---

## Q21. Maximum Subarray — Return Actual Subarray

Find the contiguous subarray with the maximum sum (Kadane's algorithm), but **return the actual subarray**, not just the sum.

```python
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

> **Expected output:** `[4, -1, 2, 1]` (sum = 6)

---

## Q22. 7-Day Rolling Average with Spike Detection

Given 365 daily sales values, find the 7-day rolling average and flag days where actual sales exceeded the rolling average by more than 20%.

```python
import random
sales = [random.randint(100, 500) for _ in range(365)]
```

---

## Q23. Intersection & Union Without Sets

Find the intersection and union of two lists **without using sets**, preserving duplicates in the intersection.

```python
a = [1, 2, 2, 3, 4, 4, 5]
b = [2, 2, 3, 3, 4, 6]
```

---

## Q24. Run-Length Encoding & Decoding

Implement run-length encoding and decoding.

```python
s = list("aaabbbccddddeefffggggh")
# Encode: [(3,'a'), (3,'b'), (2,'c'), (4,'d'), (2,'e'), ...]
# Decode: back to original string
```

---

## Q25. Longest Increasing Subsequence (LIS)

Find the length of the longest increasing subsequence.

```python
arr = [10, 9, 2, 5, 3, 7, 101, 18, 4, 6, 8]
```

> **Expected output:** `6` → `[2, 3, 4, 6, 8, 18]` or similar

---

## Q26. TTL Expiry Simulator

Simulate a DNS TTL expiry system — after each second, decrement TTL and remove expired entries.

```python
dns_cache = [
    ("google.com", "142.250.0.1",  5),
    ("github.com", "140.82.121.4", 3),
    ("reddit.com", "151.101.1.140",7),
    ("twitter.com","104.244.42.1", 2)
]
```

---

## Q27. Consecutive Sequence Split Check

Check if a list can be split into consecutive sequences of length ≥ 3 (e.g. `[1,2,3]` or `[4,5,6,7]`).

```python
arr = [1, 2, 3, 3, 4, 5]
```

> **Expected output:** `True` → splits into `[1,2,3]` and `[3,4,5]`

---

## Q28. K Nearest Points to Origin

Find the K nearest points to the origin **without using any math library** (implement distance yourself).

```python
points = [(3, 3), (5, -1), (-2, 4), (1, 1), (4, 2), (-3, -3)]
k = 3
```

---

## Q29. Duplicates to End — One Pass

Return the list with duplicates moved to the end while maintaining relative order of unique elements — **one pass only**.

```python
arr = [1, 3, 2, 1, 5, 3, 4, 2, 6, 5]
```

> **Expected output:** `[1, 3, 2, 5, 4, 6, 1, 3, 2, 5]`

---

## Q30. Topological Sort with Earliest Start Times

Perform a topological sort on tasks with dependencies and compute the earliest start time for each task.

```python
tasks = [
    (1, 3, []),       # (task_id, duration, dependencies)
    (2, 2, [1]),
    (3, 5, [1]),
    (4, 1, [2, 3]),
    (5, 2, [4])
]
```

---

## Q31. Longest Common Prefix

Find the longest common prefix among all strings in a list.

```python
words = ["flightplan", "flight", "flightless", "flightrisk", "flighty"]
```

> **Expected output:** `"flight"`

---

## Q32. Sensor Error Correction

Replace erroneous temperature readings (values > 100 or < -50) with the average of their nearest valid neighbors.

```python
temps = [22, 24, 999, 23, 25, -99, 26, 24, 22, 888, 21]
```

---

## Q33. Zero-Sum Triplets

Find all triplets that sum to zero (no duplicate triplets).

```python
arr = [-4, -1, -1, 0, 1, 2, -2, 3, -3, 0, 1]
```

---

## Q34. Above-Average Students by Std Dev

Find students whose average grade is above the class average, then sort them by standard deviation ascending.

```python
import math
students = [
    ("Alice", [90, 85, 92, 88]),
    ("Bob",   [70, 75, 80, 65]),
    ("Carol", [95, 98, 92, 97]),
    ("Dave",  [88, 82, 85, 90]),
    ("Eve",   [60, 55, 70, 65])
]
```

---

## Q35. One-Bit-Flip Grouping

Group binary strings such that strings in the same group differ by exactly one bit flip from at least one other string in the group.

```python
binary_strings = ["1100", "1000", "0100", "1010", "1110", "0000", "1001"]
```

---

## Q36. Highest Request Density Window

Find the API rate limit window with the highest request density (requests per second).

```python
windows = [(0, 10, 50), (10, 25, 90), (25, 30, 45), (30, 60, 120), (60, 65, 40)]
#           start  end   requests
```

---

## Q37. Sliding Window Maximum — O(n)

Find the maximum value in every sliding window of size `k` in **O(n)** time.

```python
arr = [1, 3, -1, -3, 5, 3, 6, 7, 2, 4]
k = 3
```

> **Expected output:** `[3, 3, 5, 5, 6, 7, 7, 7]`

---

## Q38. Bayesian Average Rating

Compute a Bayesian average rating per `product_id` given a prior of **3.5** with weight **10**.

```python
reviews = [(1, 5, 10), (1, 4, 8), (1, 3, 2),
           (2, 2, 5),  (2, 1, 3),
           (3, 5, 20), (3, 4, 15)]
# (product_id, rating, helpful_votes)
```

> **Formula:** `(prior_weight * prior + sum(ratings)) / (prior_weight + count)`

---

## Q39. Smallest Subarray with Sum ≥ S

Find the smallest subarray length whose sum is greater than or equal to target `S`.

```python
arr = [2, 3, 1, 2, 4, 3, 7, 1]
S = 7
```

---

## Q40. Port Scan Detector

Detect port scan behavior: any source that contacts more than 5 unique destinations within 1 second.

```python
packets = [
    ("A","h1",64,0.1), ("A","h2",64,0.3), ("A","h3",64,0.5),
    ("A","h4",64,0.7), ("A","h5",64,0.9), ("A","h6",64,1.0),
    ("B","h1",128,0.2),("B","h2",128,1.5)
]
# (src, dst, size, timestamp)
```

---

## Q41. Minimum Window Substring

Find the minimum window substring that contains all characters of a target string.

```python
s = list("ADOBECODEBANC")
t = "ABC"
```

> **Expected output:** `"BANC"`

---

## Q42. Consecutive Monthly Orders

Find customers who placed orders in at least **3 consecutive months**.

```python
orders = [
    (1, 101, 500, "2024-01-15"), (2, 101, 300, "2024-02-20"),
    (3, 101, 200, "2024-03-10"), (4, 102, 400, "2024-01-05"),
    (5, 102, 350, "2024-03-15"), (6, 103, 600, "2024-01-01"),
    (7, 103, 700, "2024-02-14"), (8, 103, 800, "2024-03-22"),
    (9, 103, 900, "2024-04-01")
]
# (order_id, customer_id, amount, timestamp)
```

---

## Q43. Inversion Count via Merge Sort

Count inversions (pairs where `i < j` but `arr[i] > arr[j]`) using merge sort.

```python
arr = [8, 4, 2, 1, 3, 7, 5, 6]
```

---

## Q44. Log Parser with Most Frequent Message

Parse log entries, group by level, then find the most frequent error message per level.

```python
logs = [
    "[ERROR] 10:01: disk full",    "[WARN]  10:02: high memory",
    "[ERROR] 10:03: disk full",    "[INFO]  10:04: started",
    "[ERROR] 10:05: timeout",      "[WARN]  10:06: high memory",
    "[ERROR] 10:07: disk full",    "[INFO]  10:08: ready"
]
```

---

## Q45. Positive-Negative Alternation

Rearrange a list so positive and negative numbers alternate, starting with positive. Extra numbers go to the end.

```python
arr = [3, -2, 1, -4, 5, -6, 7, 8, -9, 10, -11]
```

---

## Q46. Cosine Similarity Between Documents

Compute cosine similarity between two documents represented as `(word, frequency)` tuples.

```python
doc1 = [("cat", 3), ("dog", 2), ("fish", 1), ("bird", 4)]
doc2 = [("cat", 1), ("dog", 4), ("fish", 2), ("snake", 3)]
```

---

## Q47. Maximum Product of Three Numbers

Find the maximum product of any three numbers in a list.

```python
arr = [-10, -3, 5, 6, -2, 7, 4, -8]
```

> **Hint:** Consider both the three largest and two smallest + largest.

---

## Q48. Top 2 Cities Per Country by Population

Find the top 2 most populous cities per country and compute what percentage of that country's total listed population they represent.

```python
cities = [
    ("Lagos",  15000000, "NG"), ("Abuja", 3600000, "NG"), ("Kano",  4000000, "NG"),
    ("Nairobi", 4400000, "KE"), ("Mombasa",1300000,"KE"), ("Kisumu", 600000, "KE"),
    ("Cairo",  21000000, "EG"), ("Alex",  5200000, "EG"), ("Giza",  3600000, "EG")
]
```

---

## Q49. Circular Buffer Running Median

Implement a circular buffer of size `k`. After each insertion, return the running median.

```python
stream = [5, 2, 8, 1, 9, 3, 7, 4, 6, 10]
k = 5
```

---

## Q50. Co-Commit Author Detection

Find authors who **always** commit together (their commits always share at least one file) and list the shared files.

```python
commits = [
    ("a1", "Alice", 1000, ["main.py",  "utils.py"]),
    ("b2", "Bob",   1001, ["main.py",  "tests.py"]),
    ("c3", "Alice", 1002, ["utils.py", "config.py"]),
    ("d4", "Bob",   1003, ["utils.py", "tests.py"]),
    ("e5", "Carol", 1004, ["readme.md"])
]
```

---

## Q51. Longest Subarray with Equal 0s and 1s

Find the length of the longest subarray with equal numbers of `0`s and `1`s.

```python
arr = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
```

---

## Q52. Score Matrix Pivot

Pivot a list of `(student_id, subject, score)` tuples into a 2D matrix with students as rows and subjects as columns. Fill missing scores with `None`.

```python
scores = [
    (1,"Math",90),(1,"Sci",85),(1,"Eng",88),
    (2,"Math",75),(2,"Eng",80),
    (3,"Sci",92), (3,"Math",88),(3,"Eng",76),(3,"Art",95)
]
```

---

## Q53. Valid BST Preorder Traversal

Check whether a list represents a valid preorder traversal of a Binary Search Tree.

```python
arr = [40, 30, 20, 10, 25, 35, 80, 70, 90]
```

---

## Q54. 0/1 Knapsack via Dynamic Programming

Solve the 0/1 Knapsack problem using dynamic programming with lists only (no numpy).

```python
items = [
    ("gold",     10, 60),   # (name, weight, value)
    ("silver",   20, 100),
    ("bronze",   30, 120),
    ("platinum",  5, 50),
    ("diamond",  15, 90)
]
capacity = 50
```

---

## Q55. Excel Column Label to Number

Convert spreadsheet column labels (like Excel: A, B, ... Z, AA, AB...) to their column number.

```python
cols = ["A", "Z", "AA", "AZ", "BA", "ZZ", "AAA"]
```

> **Expected:** `[1, 26, 27, 52, 53, 702, 703]`

---

## Q56. Rolling Anomaly Detection

Detect sensor reading anomalies: values more than 2 standard deviations from that sensor's rolling mean (window = 5).

```python
readings = [
    (1,20,1),(1,21,2),(1,19,3),(1,100,4),(1,20,5),(1,22,6),
    (2,50,1),(2,52,2),(2,49,3),(2,51,4),(2,200,5),(2,50,6)
]
# (sensor_id, value, timestamp)
```

---

## Q57. Unique Combination Sum

Find all unique combinations from the list that sum to a target. Each number can only be used once.

```python
arr = [10, 1, 2, 7, 6, 1, 5]
target = 8
```

---

## Q58. Response Time Percentiles

Compute p50, p95, and p99 percentile response times per HTTP status code from a load test.

```python
results = [(f"url{i%5}", [200,200,200,404,500][i%5], (i*37)%800+10) for i in range(100)]
# (url, status_code, response_time_ms)
```

---

## Q59. Maximum Sum Rectangle in 2D Matrix

Find the maximum sum rectangle in a 2D matrix.

```python
matrix = [
    [ 1, -2, -1,  4],
    [-8, -3,  4,  2],
    [ 3,  8, 10, -8],
    [-4, -1,  1,  7]
]
```

---

## Q60. Phone Number Normalization to E.164

Normalize phone numbers to E.164 format (`+254XXXXXXXXX` for Kenya, `+1XXXXXXXXXX` for US).

```python
phones = [
    "+254 712 345 678",
    "0712345678",
    "(254) 712-345-678",
    "+1 (800) 555-0199",
    "18005550199",
    "800-555-0199"
]
```

---

## Q61. Valid Mountain Array

Determine if a list represents a valid mountain array — strictly increases then strictly decreases, minimum length 3.

```python
arr = [0, 2, 3, 4, 5, 2, 1, 0]
```

---

## Q62. Ad Auction Ranker

Rank ads by effective CPM = `bid * quality_score`, return top 5 with their effective CPM.

```python
ads = [
    ("ai tools",       2.5, 8), ("python course",  1.8, 10),
    ("web hosting",    3.0, 6), ("cloud storage",  2.2,  9),
    ("vpn service",    1.5, 7), ("coding bootcamp",4.0,  5),
    ("linux server",   2.0, 8), ("data science",   3.5,  9)
]
# (keyword, bid_price, quality_score)
```

---

## Q63. Median via Quickselect

Find the median of a list **without sorting** — implement the Quickselect algorithm.

```python
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
```

---

## Q64. Top 5 Paths Per HTTP Method

Find the top 5 most requested paths per HTTP method from request logs.

```python
logs = [
    "GET /home HTTP/1.1",       "POST /login HTTP/1.1",
    "GET /home HTTP/1.1",       "GET /api/users HTTP/1.1",
    "POST /login HTTP/1.1",     "GET /home HTTP/1.1",
    "DELETE /api/user/1 HTTP/1.1","GET /api/users HTTP/1.1",
    "POST /api/post HTTP/1.1",  "GET /home HTTP/1.1"
]
```

---

## Q65. Find Duplicate and Missing Number

Given a list from 1 to n with **one duplicate** and **one missing**, find both in **O(n) time and O(1) space**.

```python
arr = [1, 2, 3, 4, 4, 6, 7, 8]  # 5 missing, 4 duplicate
```

---

## Q66. Top GDP Per Capita Countries

Find the top 3 countries by GDP per capita, but only among countries with population > 10 million.

```python
countries = [
    ("Kenya",     110e9,  55e6), ("US",      25e12,  330e6),
    ("Seychelles",  2e9, 100000),("Germany",  4e12,   83e6),
    ("Nauru",     0.1e9,  10000),("UK",       3e12,   67e6),
    ("Nigeria",   440e9, 220e6), ("Iceland",  25e9,  370000)
]
# (country, gdp, population)
```

---

## Q67. Smallest Missing Positive Integer

Find the smallest positive integer missing from a list.

```python
arr = [3, 4, -1, 1, 5, 2, 7, 9]
```

> **Expected output:** `6`

---

## Q68. Org Chart Subtree Traversal (Non-Recursive)

Find all employees under a given manager (entire subtree) **non-recursively**.

```python
org = [(2,1),(3,1),(4,2),(5,2),(6,3),(7,3),(8,4),(9,4),(10,5)]
# (employee_id, manager_id)
root_manager = 1
```

---

## Q69. Bucket Sort

Implement bucket sort for floats between 0 and 1.

```python
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.788, 0.432, 0.21, 0.0987]
```

---

## Q70. Connected Flight Itineraries with Layover Constraint

Find itineraries (chains of connected flights) with total layover under 2 hours.

```python
flights = [
    ("F1","NBO","DXB","08:00","14:00"),
    ("F2","DXB","LHR","15:00","19:00"),
    ("F3","DXB","LHR","20:00","00:00"),
    ("F4","NBO","JFK","10:00","20:00"),
    ("F5","LHR","JFK","21:00","03:00")
]
# (flight_id, origin, destination, departure, arrival)
```

---

## Q71. Dutch National Flag Sort

Sort an array of `0`s, `1`s, and `2`s **in one pass without counting**.

```python
arr = [2, 0, 1, 2, 1, 0, 0, 2, 1, 0, 2, 1]
```

---

## Q72. E-Commerce Conversion Funnel

Compute drop-off rates for a `view → cart → purchase` conversion funnel.

```python
events = [
    (1,"view",1),(1,"cart",2),(1,"purchase",3),
    (2,"view",4),(2,"cart",5),
    (3,"view",6),(4,"view",7),(4,"purchase",8),
    (5,"view",9),(5,"cart",10)
]
# (user_id, event, timestamp)
```

---

## Q73. Palindrome Permutation Check

Determine if any permutation of a list of integers can form a palindrome.

```python
arr = [1, 2, 3, 2, 1, 3, 4, 4]
```

---

## Q74. Round Robin CPU Scheduler

Simulate Round Robin scheduling with `quantum=3` and return the execution timeline.

```python
tasks = [
    ("P1", 8, 0),   # (task_name, cpu_burst, arrival_time)
    ("P2", 4, 1),
    ("P3", 9, 2),
    ("P4", 5, 3)
]
```

---

## Q75. Maximum T9 Keypad Presses

Find the word that requires the most key presses on a T9 phone keypad.

```
2 = abc, 3 = def, 4 = ghi, 5 = jkl
6 = mno, 7 = pqrs, 8 = tuv, 9 = wxyz
```

```python
words = ["hello", "world", "python", "zoo", "it", "yes", "six", "swim"]
```

---

## Q76. Price Range Exceeds Category Average

Find categories where the price range (max - min) exceeds the category average price.

```python
products = [
    (1,"A",10),(2,"A",20),(3,"A",100),
    (4,"B",50),(5,"B",55),(6,"B",60),
    (7,"C",5), (8,"C",500),(9,"C",250)
]
```

---

## Q77. Maximum XOR of Two Elements

Find the maximum XOR of any two elements in a list.

```python
arr = [3, 10, 5, 25, 2, 8]
```

---

## Q78. Sustained High-Load Host Detection

Find hosts that have been above 80% on **all three** metrics (CPU, memory, disk) for more than **3 consecutive snapshots**.

```python
snapshots = [
    ("web1",85,82,81),("web1",90,88,85),("web1",87,83,82),("web1",91,89,86),
    ("web2",70,85,82),("web2",88,91,88),
    ("db1",95,90,85), ("db1",92,88,83)
]
# (hostname, cpu%, mem%, disk%)
```

---

## Q79. Longest Consecutive Sequence — O(n)

Find the longest consecutive integer sequence in **O(n)** time.

```python
arr = [100, 4, 200, 1, 3, 2, 5, 6, 7, 8]
```

> **Expected output:** `8` → sequence `[1,2,3,4,5,6,7,8]`

---

## Q80. Trie-Like Prefix Search

Build a trie-like nested list structure from `(word, definition)` pairs and implement prefix search.

```python
words = [
    ("apple","a fruit"),    ("app","an application"),
    ("application","software"), ("apply","to request"),
    ("apt","suitable"),     ("bat","flying mammal"),
    ("ball","round object")
]
```

---

## Q81. Power Set in Lexicographic Order

Return all subsets (power set) in lexicographic order.

```python
arr = [1, 2, 3]
```

> **Expected output:** `[[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]`

---

## Q82. Shortest Path via Dijkstra (Lists Only)

Find the shortest path between two cities using Dijkstra's algorithm — **lists only, no sets or heaps**.

```python
roads = [
    ("Nairobi","Nakuru",160), ("Nairobi","Mombasa",480),
    ("Nakuru","Kisumu",120),  ("Nakuru","Eldoret",90),
    ("Mombasa","Malindi",120),("Kisumu","Eldoret",80),
    ("Eldoret","Iten",50),    ("Malindi","Lamu",200)
]
```

---

## Q83. Maximum Sum of Non-Adjacent Elements

Find the maximum sum of non-adjacent elements in a list.

```python
arr = [3, 7, 4, 6, 5, 9, 1, 2, 8]
```

---

## Q84. Hashtag Engagement Ranker

Find hashtags that appear in at least 3 tweets and rank by total engagement (`likes + retweets`).

```python
tweets = [
    ("A","Love #python and #ai",        100, 50),
    ("B","#python is great",             80, 40),
    ("C","#ai #ml changing the world",  200,100),
    ("D","#python #ml tutorial",         60, 30),
    ("E","#ai revolution #deeplearning",150, 80),
    ("F","#python #ai forever",          90, 45)
]
# (user, text, likes, retweets)
```

---

## Q85. Heapsort (No `heapq` Import)

Implement Heapsort using only lists — no `heapq` module.

```python
arr = [12, 11, 13, 5, 6, 7, 3, 1, 9, 15]
```

---

## Q86. Monthly P&L and Quarterly Profitability

Find months where the business was profitable and compute quarterly P&L.

```python
records = [
    ("2024-01",50000,45000), ("2024-02",60000,55000), ("2024-03",40000,48000),
    ("2024-04",70000,60000), ("2024-05",80000,75000), ("2024-06",90000,85000),
    ("2024-07",100000,90000),("2024-08",55000,60000), ("2024-09",75000,70000),
    ("2024-10",85000,80000), ("2024-11",95000,88000), ("2024-12",110000,95000)
]
# (date_str, revenue, expense)
```

---

## Q87. Counting Sort

Implement counting sort. Assume values are in range `[0, 100]`.

```python
arr = [64, 25, 12, 22, 11, 90, 45, 33, 67, 89, 12, 45, 78]
```

---

## Q88. Peak Concurrent User Sessions

Find the peak concurrent user count and the time it occurred.

```python
sessions = [(1,0,5),(2,1,4),(3,2,8),(4,3,6),(5,4,10),(6,5,7),(7,6,9),(8,7,11)]
# (user_id, login_time, logout_time)
```

---

## Q89. Minimum Jumps to Last Index

Find the minimum number of jumps to reach the last index, where each element is the maximum jump length from that position.

```python
arr = [2, 3, 1, 1, 4, 2, 3, 1, 1, 2]
```

---

## Q90. Competition Ranking with Tie Handling

Assign ranks with ties handled: tied students get the same rank, and the next rank skips accordingly (e.g., 1, 2, 2, 4).

```python
results = [
    ("Alice",95),("Bob",87),("Carol",92),
    ("Dave",87),("Eve",95),("Frank",78),("Grace",92)
]
```

---

## Q91. Sieve of Eratosthenes

Find all prime numbers up to a limit using the Sieve of Eratosthenes.

```python
limit = 100
```

---

## Q92. Network Traffic Matrix

Build a traffic matrix from network flows and find top talker pairs by bytes.

```python
flows = [
    ("10.0.0.1","10.0.0.2",500), ("10.0.0.1","10.0.0.3",200),
    ("10.0.0.2","10.0.0.1",300), ("10.0.0.3","10.0.0.1",100),
    ("10.0.0.2","10.0.0.3",400), ("10.0.0.1","10.0.0.2",600)
]
# (src_ip, dst_ip, bytes)
```

---

## Q93. String Shift Groups

Find the largest group of strings that are all cyclic shifts of each other (e.g., `"abc" → "bcd" → "cde"`).

```python
words = ["abc","bcd","acef","xyz","az","ba","a","z","cde","def"]
```

---

## Q94. Multi-Event Record Holders

Find athletes who hold the record (fastest time) in more than one event.

```python
results = [
    ("Alice","100m",11.2), ("Bob",  "100m",10.8),
    ("Alice","200m",22.1), ("Carol","200m",21.9),
    ("Bob",  "400m",48.5), ("Carol","400m",47.2),
    ("Alice","long_jump",6.5),("Bob","long_jump",7.1)
]
# (athlete, event, time_seconds)
```

---

## Q95. Coin Change — Number of Ways

Find the number of ways to make change for a target amount using dynamic programming.

```python
coins = [1, 5, 10, 25]
amount = 41
```

---

## Q96. GitHub Repo Scorer

Score repos and filter by language, returning the top 5.

```
Score = stars*0.4 + forks*0.3 + (1/max(last_commit_days_ago, 1))*100*0.3
```

```python
repos = [
    ("repoA",1200,300,"Python",5),  ("repoB",800,400,"JS",2),
    ("repoC",950,250,"Python",30),  ("repoD",1500,100,"Python",1),
    ("repoE",600,600,"Python",10),  ("repoF",2000,50,"Python",90),
    ("repoG",1100,350,"Python",3)
]
# (name, stars, forks, language, last_commit_days_ago)
lang = "Python"
```

---

## Q97. Sparse Table for Range Minimum Query

Implement a sparse table for Range Minimum Query (RMQ) with **O(n log n)** preprocessing and **O(1)** query.

```python
arr = [2, 4, 3, 1, 6, 7, 8, 9, 1, 7]
queries = [(0, 4), (2, 7), (1, 9), (3, 6)]
```

---

## Q98. Best-Fit Bin Packing for Container Orchestration

Implement a best-fit bin packing algorithm to assign containers to hosts with **16 GB RAM** and **8 CPU cores**.

```python
containers = [
    (f"c{i}", [512,1024,2048,256,768][i%5], [0.5,1,2,0.25,1.5][i%5], "pending")
    for i in range(15)
]
# (container_id, memory_mb, cpu_cores, status)
```

---

## Q99. Subarrays with XOR Equal to K

Find the number of subarrays with XOR equal to a target value `k`.

```python
arr = [4, 2, 2, 6, 4]
k = 6
```

---

## Q100. Noun Phrase Extraction (NLP)

Extract all noun phrases defined as: optional determiner (DT) + optional adjectives (JJ) + noun (NN).

```python
tokens = [
    ("The","DT"), ("quick","JJ"), ("brown","JJ"), ("fox","NN"),
    ("jumps","VBZ"),("over","IN"),("the","DT"),  ("lazy","JJ"),
    ("dog","NN"),  ("near","IN"), ("a","DT"),    ("big","JJ"),
    ("tree","NN")
]
# (word, pos_tag)
```

> **Expected NPs:** `"The quick brown fox"`, `"the lazy dog"`, `"a big tree"`

---

## Stats

| Category | Count |
|---|---|
| Sorting & Searching | 15 |
| Dynamic Programming | 10 |
| String Manipulation | 12 |
| Graph & Tree Algorithms | 8 |
| Data Aggregation & Analytics | 20 |
| System Simulations | 10 |
| Math & Bit Manipulation | 8 |
| NLP & Pattern Matching | 7 |
| **Total** | **100** |

---

> 💡 **Challenge yourself:** Try to solve each problem before checking any hints. Most solutions fit in under 20 lines of clean Python.