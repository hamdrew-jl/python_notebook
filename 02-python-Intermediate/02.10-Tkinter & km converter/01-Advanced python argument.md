# 01 Advanced python argument


## 1.1 Keyword argument 
```python
def my_function(a, b,c):
# Do this with a
# Then do this with b
# Finally c

my_function(c=1, b=2, a=1)
```

## 1.2 Arguments with default values

```python
def my_function(a=1, b=2, c=3):
# Do this with a
# Then do this with b
# Finally c

my_function(b=5)
```
## 1.3  Unlimited Position Argument. *args
```python
# [Problem]
def add(n1, n2):
    return n1 + n2

add(n1 = 5, n2 = 3)


# [Solution]
def add(*args):
    for n in args:
        print(n)

add(3, 53, 7, 8)
```
* *arges tells in this function can accept any number of arguments.
```python
def add(*args):

    sum_num = 0
    for n in args:
        sum_num += n
    return sum_num


print(add(2, 4, 3, 8, 9, 7, 3, 2))

```
Note: could also access above number by index
```python
def add(*args):

    # could also access number by index
    print(args[4])

    sum_num = 0
    for n in args:
        sum_num += n
    return sum_num


print(add(2, 4, 3, 8, 9, 7, 3, 2))

->9
->38
```

## 1.4  **kwargs Keyward Arguments
```python
def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))

calculate(add=3, multiply=5)

```
console
```python
{'add': 3, 'multiply': 5}
<class 'dict'>
```
### 1.4.1 Get value and key
```python
def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])

calculate(add=3, multiply=5)
```
console
```python
{'add': 3, 'multiply': 5}
add
3
multiply
5
3
```
### 1.4.2 mostly use
```python
def calculate(n, **kwargs):

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
```
console
```python
25
```

## 1.5 use **kwargs when create class
```python
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="GT-R")
```
Note:here we don't use self.make = kwargs["make"]
it will return error
self.model = kwargs.get("model")
 if the key doen't exist in the dictionary, it just returns none