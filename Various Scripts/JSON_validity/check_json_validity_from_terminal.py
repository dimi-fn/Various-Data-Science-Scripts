import json
import os
import sys

# Check JSON validity
def is_valid_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            json.load(file)
            return True
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except ValueError as value_err:
        print(f"Error while reading the JSON file '{file_name}': {value_err}")
    return False

if __name__ == "__main__":
    # if user hasn't given 2 arguments
    if len(sys.argv) != 2:
        print("You didn't enter the right command. Run: python check_json_validity.py <your-json-filename>.json")
        sys.exit(1)

    # the file_name is the second comand line argument
    file_name = sys.argv[1]

    if is_valid_json_file(file_name):
        print(f"The provided JSON file '{file_name}' is valid!")
    else:
        print(f"The provided JSON file '{file_name}' is not valid!")
