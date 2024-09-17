import json

# -------------------------- #

# PYTHON STRINGS

string = "James is Handsome"
print(string.upper())
print(string.lower())
print(string.replace("James", "Ashley"))
print(string.split(" "))

# REFERENCES
original = [1, 2, 3, 4]
reference = original
copy = original[:]

original.remove(4)
print(f"Original: {original}")
print(f"Reference: {reference}")
print(f"Copy: {copy}")

# TUPLES
tup = 1, 2, 3
x, y, z = tup
print(f"{x}, {y}, {z}")

# DICTIONARY
dict = {
    'A': 1,
    'B': 'ABC',
    'C': [1, 2, 3],
    'D': {
        'subkey1': 100,
        'subkey2': 300
    }
}

print(dict)
print(dict['A'])
print(dict.get('D'))  # safer; gives 'none' by default if key not exists
print(dict.get('E', 'N/A'))

person = {
    "first_name": "Uriel",
    "last_name": "Parantar",
    "age": 21,
    "favorite_color": "Phenk",
    "is_present": False
}
# print with nice formating thru json package
print(json.dumps(person, indent=4))

# add data
person['hobbies'] = {
    'favorite': 'codechum',
    'least_fave': 'chumcode'
}

print(json.dumps(person, indent=4))

for item in person.items():
    print(item)

new_dict = {key: value*value for key, value in person.items()}
print(json.dumps(new_dict, indent=4))
