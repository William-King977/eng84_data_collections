# Data Collections in Python
## Types of collections
* Lists 
* Tuples
* Dictionaries
* Sets

## Lists
Lists are used to store multiple items in a single variable. 
They are mutable meaning that they can be changed after it has 
been created.

Creating a list using `[]`
```python
shopping_list = ["bread", "chocolate", "avocado", "milk"]
print(shopping_list) # ['bread', 'chocolate', 'avocado', 'milk']
print(shopping_list[0]) # bread
print(shopping_list[-2]) # avocado
```

Modifying a list value
```python
# Replace "bread" with "orange"
shopping_list[0] = "orange"

# Outputs ['orange', 'chocolate', 'avocado', 'milk']
print(shopping_list)
```

Adding values to a list
```python
# Adds "ice cream" to the end of the list
shopping_list.append("ice cream")

# Outputs ['orange', 'chocolate', 'avocado', 'milk', 'ice cream']
print(shopping_list)
```

Removing an item from a list
```python
# Remove a specified item
shopping_list.remove("orange")

# ['chocolate', 'avocado', 'milk', 'ice cream']
print(shopping_list)
```

It's possible to have a list with multiple data types
```python
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list[1:3]) # outputs [2, 3]
```

## Tuples
Tuples are used to store multiple items in a single variable. 
However, they are immutable meaning that they cannot be changed 
after it has been created.

Create a tuple using `()`
```python
essential = ("medicine", "tooth paste", "tea bags")
print(essential) # outputs ('medicine', 'tooth paste', 'tea bags')
essential[0] = "cereal" # this will fail
```

## Dictionaries
Dictionaries are used to store data values in key:value pairs.
The value can be retrieved by using the key. It's dynamic with
its data types, and they are mutable. However, it does not allow 
values with the same key.

Creating a dictionary
```python
dev_ops_student = {
    # key : value
    "name": "William",
    "stream": "DevOps",
    "completed_lessons": 3,
    "completed_lessons_names": ["variables", "data types", "collections"]
}
```

Accessing values
```python
# Values are accessed by a key.
print(dev_ops_student["name"]) # outputs "William"
print(dev_ops_student["completed_lessons"]) # outputs 3
print(dev_ops_student["completed_lessons_names"][1]) # outputs "data types"
```

Adding and changing values
```python
# Adds "operators" as a value in completed_lessons_names
dev_ops_student["completed_lessons_names"].append("operators")

# Updates completed_lessons from 3 to 4
dev_ops_student["completed_lessons"] = 4
```

Removing values
```python
# Removes "data types" from from completed_lessons_names
dev_ops_student["completed_lessons_names"].remove("data types")
```

Adding another key:value pair
```python
dev_ops_student["week"] = 3 
```

Removing a key:value pair
```python
dev_ops_student.pop("name") # removes the key:pair using the key
del dev_ops_student["name"] # does the same
```

## Sets
Sets are used to store multiple values in the same variable.
They are mutable, so it can be modified. However, its contents
are always in a randomised order when they are created or 
modified.

Creating a set
```python
car_parts = {"wheels", "windows", "doors"}
print(car_parts) # outputs {'doors', 'wheels', 'windows'}
```

Adding items
```python
car_parts.add("seats")
print(car_parts) # outputs {'doors', 'seats', 'wheels', 'windows'}
```

Removing items
```python
car_parts.discard("seats")
print(car_parts) # outputs {'doors', 'wheels', 'windows'}
```

Frozen sets
```python
# Frozen sets cannot be modified.
car_parts = frozenset(car_parts)
car_parts.add("engine") # this will fail
```
