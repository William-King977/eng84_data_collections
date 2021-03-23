#### DICTIONARIES ####
# They use KEY VALUE pairs to save the data
# The data can be retrieved by its key
# Data is ordered (Python 3.7)
# Syntax {}
# Within a dict, we can also have a list declared (more dynamic with datatypes)

# Create a dictionary
dev_ops_student = {
    "key": "value",
    "name": "William",
    "stream": "DevOps",
    "completed_lessons": 3,
    "completed_lessons_names": ["variables", "data types", "collections"]

}
# print(dev_ops_student)
# print(type(dev_ops_student))

# print(dev_ops_student["name"])
# print(dev_ops_student["completed_lessons"])
# print(dev_ops_student["completed_lessons_names"][1]) # outputs "data types"

# Adding "operators" as a value in completed lessons names
# Also update completed lesson from 3 to 4
dev_ops_student["completed_lessons_names"].append("operators")
dev_ops_student["completed_lessons"] = 4
print(dev_ops_student)

# Removing "data types" from completed lessons names
dev_ops_student["completed_lessons_names"].remove("data types")
print(dev_ops_student["completed_lessons_names"])

# Show keys and values
print(dev_ops_student.keys())
print(dev_ops_student.values())


#### SETS ####
# Syntax {}
# Mutable, but only for addition and deletion
# Unordered data (not in the order of initialisation)
# NOTE: randomised everytime it is modified.

# Creating a set
car_parts = {"wheels", "windows", "doors"}
print(car_parts)
print(type(car_parts))

# Add items
car_parts.add("seats")
print(car_parts)

# Remove items
car_parts.discard("seats")
print(car_parts)

# Frozen sets
# These prevent the sets from being modified.
car_parts = frozenset(car_parts)
print(car_parts)

