# 01 List Comprehension

## 1.new_list = [new_item for item in list] 
```python
num = [1, 2, 3]
new_num = [2 * n for n in num]
```
### Python Sequences
* list
* range
* string
* tuple

```python
name = "Jack"
letter_list = [letter for letter in name]

-> ['J', 'a', 'c', 'k']
```

```python
range(1, 5)
range_list = [2*n for n in range(1, 5)]

-> [2, 4, 6, 8]
```

## 2.new_list = [new_item for item in list if test] 
### 2.1 Under four letter
```python
name = ['Alex', 'Beth', 'Dace', 'Eleanor', 'Freddie']
short_names = [short_name for short_name in name if len(short_name) < 5]

-> ['Alex', 'Beth', 'Dace']
```
### 2.2 More than four letter and upper each letter
```python
long_cap_name = [long.upper() for long in name if len(long) > 4]
long_cap_name

-> ['ELEANOR', 'FREDDIE']
```

## 3. Exercise
* Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

* You are going to create a list called result which contains the numbers that are common in both files.
* IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.
#### Example Output
```python
[3, 6, 5, 33, 12, 7, 42, 13]
```
### file1.txt
```python
3
6
5
8
33
12
7
4
72
2
42
13

```
### file2.txt
```python
3
6
13
5
7
89
12
3
33
34
1
344
42

```
#### Solution
```python
result = [int(num) for num in open("file1.txt").readlines() if num in open("file2.txt").readlines()]


print(result)
```