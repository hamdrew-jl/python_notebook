# 02 Dictionary Comprehension

## 1.new_dict = {new_key:new_value for item in list} 
```python
name = ['Alex', 'Beth', 'Dace', 'Eleanor', 'Freddie']
import random
```
original score dictionary
```python
student_score = {
    "Alex": 89,
    "Beth":45,
    "Dace":68,
    "Eleanor":77,
    "Freddie":94
}
```
```python
students_score = {student:random.randint(50, 100) for student in name}

-> {'Alex': 89, 'Beth': 45, 'Dace': 68, 'Eleanor': 77, 'Freddie': 94}
```

## 2.new_dict = {new_key:new_value for (key,value) in dict.items()}


## 3.new_dict = {new_key:new_value for (key,value) in dict.items() if test}
```python
passed_students = {student:score for (student, score) in student_score.items() if score > 70}

-> {'Alex': 89, 'Eleanor': 77, 'Freddie': 94}
```

## 4. Exercise
### 4.1 Takes each word in the given sentence and calculates the number of letters in each word.

```python
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# DON'T CHANGE CODE ABOVE

word_list = sentence.split(" ")
result = {word:len(word) for word in word_list}

# DON'T CHANGE CODE BELOW
print(result)
```
console:
```python
{'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
```
Note: can be shorter in
```python
result = {word:len(word) for word in sentence.split()}
```
### 4.2 Degrees Celsius and converts it into degrees Fahrenheit
```python
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# DON'T CHANGE CODE ABOVE


weather_f = {day:((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}

print(weather_f)

```
Output:
```python
{'Monday': 53.6, 
 'Tuesday': 57.2, 
 'Wednesday': 59.0, 
 'Thursday': 57.2, 
 'Friday': 69.8, 
 'Saturday': 71.6, 
 'Sunday': 75.2}
```
## 5.Pandas iterrows()
### Keyword Method with iterrows()
### {new_key:new_value for (index, row) in df.iterrows()}
```python
student_dict = {
    "student": ["Jack", "Peter", "Lily"],
    "score": [87, 84, 76]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
```
console
```python
0
1
2


student    Jack
score        87
Name: 0, dtype: object
student    Peter
score         84
Name: 1, dtype: object
student    Lily
score        76
Name: 2, dtype: object


Jack
Peter
Lily


87
84
76
```