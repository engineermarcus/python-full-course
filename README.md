# python-full-course

## Lists 

### append 

```python
nums = [1,2,3,4,5]
nums.append(6)
print(nums)
# [1,2,3,4,5,6]
```
### insert 

```python
nums = [1,2,3,4,5]
nums.insert(0,0)
print(nums)
# [0,1,2,3,4,5]
```
### index

```python
nums = [1,2,3,4,5]
nums.index(3)
# 2
```
### count 

```python
nums = [3,5,7,6,8,6,7,8]
nums.count(6)
# 2
```
### pop 

```python
num = [1,2,3,4,5]
num.pop()
print(num)
# [1,2,3,4]

nums = [1,2,3,4,5]
nums.pop(0)
print(num)
# [2,3,4,5]
```
### remove 

```python 
nums = [1,2,3,4,5]
nums.remove(3)
print(nums)
# [1,2,4,5]
```
### reverse 

```python 
nums = [1,2,3,4,5]
nums.reverse()
print(nums)
# [5,4,3,2,1]

num = [1,2,3,4,5]
num[::-1]
# [5,4,3,2,1]
```
### slice 

```python
nums = [1,2,3,4,5]
nums[0:4]
# [1,2,3,4]
```
### sort 

```python
nums = [1,4,5,2,3]
nums.sort()
sorted(nums)
# [1,2,3,4,5]
```

## Mutable Default Arguments 

```python
# wrong 

def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart 

alice = add_to_cart("shoes")
bob = add_to_cart("mango")
print(alice) # ['shoes','mango'] alice only added shoe to cart

# right 

def add(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
alice = add("shoes")
bob = add("mango")

print(alice) # returns only the item added to cart 
```

## Tuples 

```python 
point = (3,7)
x,y = point

print(x)
print(y)
# 3
# 7

t = (1,)   # tuple
t = (1)    # just the number 1, NOT a tuple

locations = {
    (0, 0) : "origin",
    (6, 7) : "Nairobi"

}

print(locations[(6, 7)])
# Nairobi
```
## Sets

```python 
s = {1, 2, 3, 3, 3,2}
print(s)  # {1, 2, 3} — duplicates removed automatically
```
###  Deduplication — removing duplicates from a list

```python
names = ["james", "john", "anna", "greg", "greg", "james", "james"]

list_to_set = set(names)
set_to_list = list(list_to_set)
print(list_to_set)
print(set_to_list)
```
### membership testing 

```python
admins = {"alice", "bob", "charlie"}

if "alice" in admins:
    print("access granted")

```