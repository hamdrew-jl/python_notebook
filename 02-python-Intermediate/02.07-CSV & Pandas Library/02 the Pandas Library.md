# 02 the Pandas Library
* Data frame and Series 
* whole table is basically a Data frame 
* every single column is a series

## 0. Resources: weather_data.csv
```python
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny
```


### Import pandas, .read_csv
```python
import pandas

# we don't need to with open the file and use csv.reader
data = pandas.read_csv("Dictionary/weather_data.csv")  
```
### Dictionary (.to_dict   .iterrows()
#### Figure the difference
```python
# make dictionary (column)
data_dict = data.to_dict()
print(data_dict)

# dictionary comprehension
dict_new = {row.day:row.temp for (index, row) in data.iterrows()}
print(dict_new)
```
console
```python
{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

{'Monday': 12, 'Tuesday': 14, 'Wednesday': 15, 'Thursday': 14, 'Friday': 21, 'Saturday': 22, 'Sunday': 24}
```
### List (.to_list() , len() )
```python
temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))
```
console:
```python
[12, 14, 15, 14, 21, 22, 24]
7
```
## 1. Average Temperature Value
### 1.1 for loop
```python
total = 0
for i in range(0, len(temp_list)):
    total += temp_list[i]

aver_temp = total / len(temp_list)
print(aver_temp)
```
### 1.2 python sum()
```python
aver_temp = sum(temp_list) / len(temp_list)
print(aver_temp)
```
### 1.3 Pandas 
```python
print(data["temp"].mean())
```
console:
```python
17.428571428571427
```
## 2. Max Temperature Value
```python
max_temp = max(temp_list)
print(max_temp)

print(data["temp"].max())
```
console:
```python
24
24
```

## 3. Get data in Columns

```python
# method 1. like a dictionary
print(data["condition"])  # the string has to match the name of the column.

# method 2. like a object method
print(data.condition)
```
console:
```python
0     Sunny
1      Rain
2      Rain
3    Cloudy
4     Sunny
5     Sunny
6     Sunny
Name: condition, dtype: object
```
Note: if column name has a capital,
the key and attribute have to change to be capital.
## 4. Get Data in Row
[name of column (day or temp or condition) == content], we can get the entire row
The table could be filtered more than once.
```python
row = data[data.condition == "Sunny"]
print(row)

current_row = row[row.day == "Monday"]
print(current_row)
```
console
```python
        day  temp condition
0    Monday    12     Sunny
4    Friday    21     Sunny
5  Saturday    22     Sunny
6    Sunday    24     Sunny


      day  temp condition
0  Monday    12     Sunny
```

```python
print(data[data.day == "Monday"])
```
console:
```python
      day  temp condition
0  Monday    12     Sunny
```
### 4.1. Filter the row
#### Challenge: print the row of data which had the highest temp
* filter: [particular column == particular value]
```python
highest_temp = data["temp"].max()
print(data[data.temp == highest_temp])
```
console:
```python
      day  temp condition
6  Sunday    24     Sunny
```
### 4.2. Convert Monday's temperature to Fahrenheit
```python
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
mon_temp_F = (monday_temp * 9/5) + 32
print(mon_temp_F)
```
## 5. Create a dataframe from scratch (.DataFrame   .to_csv)

```python
data_dict = {"student": ["Amy", "James", "Tom"],
             "scores": [75, 86, 64]
             }
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")  # Create a csv file and restore the data in that file
```
A new csv file 'new_data' :
```python
  student  scores
0     Amy      75
1   James      86
2     Tom      64
```
