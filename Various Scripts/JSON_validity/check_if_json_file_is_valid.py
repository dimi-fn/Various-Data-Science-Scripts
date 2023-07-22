import json
import os

# Check JSON validity
def is_valid_json_file(file_name):
    try:
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        with open(file_path, 'r') as file:
            json.load(file)
            return True
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except ValueError as value_err:
        print(f"Error while reading the JSON file '{file_name}': {value_err}")
    return False

# Check a particular JSON file
# This will work if the JSON file is in the same directory path with this Python script, else adjust the path
# replace the value of file_name with your actual JSON file name
file_name = "json_test_file_not_uploaded.json"
if is_valid_json_file(file_name):
     print(f"The function returned {is_valid_json_file(file_name)} so the provided JSON file is valid!")
else:
     print(f"The function returned {is_valid_json_file(file_name)} so the provided JSON file is not valid!")
