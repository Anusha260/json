import json
data = '{"a":  1, "a":  2, "a":  3, "a": 6, "b": 3, "b": 6}'
# print("Original Python object:")
# print(python_obj)
dict = json.loads(data)
# print("\nUnique Key in a JSON object:")
print(dict)
print(data) 
