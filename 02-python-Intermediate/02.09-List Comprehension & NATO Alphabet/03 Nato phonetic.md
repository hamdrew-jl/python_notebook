# 03 Nato phonetic
## Keyword Method with iterrows()
## {new_key:new_value for (index, row) in df.iterrows()}
```python
import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("What's your name? ").upper()

# list comprehension
output_list = [nato_dict[letter] for letter in user_name]
print(output_list)

# OR
list_letter = [letter for letter in user_name]
phonetic_code = [nato_dict[letter] for letter in list_letter if letter in nato_dict.keys()]
print(phonetic_code)

```