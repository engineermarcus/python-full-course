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
# 6
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