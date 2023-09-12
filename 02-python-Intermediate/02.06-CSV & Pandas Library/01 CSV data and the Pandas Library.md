# 01 CSV Data and the Pandas Library

## 1. csv file 
* CSV represent tabula data
* comma separate values

### 01 handle the data

```python
 with open("Dictionary/weather_data.csv") as weather_data:
    data = weather_data.readlines()
    print(data)
```

console: (\n exist)
```python
['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n']
```

### 02 Import csv

```python
import csv

with open("Dictionary/weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    for row in data:
        print(row)
```
console:
```python
['day', 'temp', 'condition']
['Monday', '12', 'Sunny']
['Tuesday', '14', 'Rain']
['Wednesday', '15', 'Rain']
['Thursday', '14', 'Cloudy']
['Friday', '21', 'Sunny']
['Saturday', '22', 'Sunny']
['Sunday', '24', 'Sunny']
```
### 03 Create a temperature list
* contents all the temperature from csv
* integer style

```python
import csv

with open("Dictionary/weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)
```
console:
```python
['12', '14', '15', '14', '21', '22', '24']
```
Note: It can not easy to change each string into integer.

## 2. Pandas
* Python data analysis library
* Perform data analysis on tabula data.
* Neet to install
* Take first row to be names of each column
* Automatically know how to find the data, so specify the namme of the column

```python
import pandas

data = pandas.read_csv("Dictionary/weather_data.csv")  # we don't need to with open the file and use csv.reader
print(data)
```
console:
```python
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
```
* if we extract temperature
```python
print(data["temp"])
```
console
```python
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp, dtype: int64
```
