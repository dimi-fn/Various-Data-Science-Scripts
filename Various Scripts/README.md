# Various Scripts


Contents
=======================

* [Check if a JSON file is valid](#check-if-a-json-file-is-valid)


------- 


# Check if a JSON file is valid

## 1st way

* Download the python script [here](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Various%20Scripts/JSON_validity/check_if_json_file_is_valid.py), replace the file name with your own JSON file name, navigate to the script's path and run: 

```
python check_if_json_file_is_valid.py
```

## 2nd way

* Download the python script [here](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Various%20Scripts/JSON_validity/check_json_validity_from_terminal.py)
* Have you JSON script in the same directory with the Python script above
* Navigate to the script's path and run:

```
python check_json_validity_from_terminal.py <your-JSON-file-name>.json
```

## 3rd way

* Without using the python script above, navigate to the directory where your JSON file is
* Replace your-json-file-name-here with your JSON file name, and run:

```
python -c "import json; json.load(open('<your-json-file-name-here>.json')); print('The JSON file is valid')"
```
If the file is valid then it will print 'The JSON file is valid', else the corresponding errors.
