'''15. Write a Python module named file_operations.py with functions for reading, writing, and appending
data to a file.'''

def read_file(file_path):
    """
    Read the contents of a file and return it as a string.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."

def write_file(file_path, data):
    """
    Write the given data to a file, overwriting any existing content.
    """
    with open(file_path, 'w') as file:
        file.write(data)

def append_file(file_path, data):
    """
    Append the given data to the end of a file.
    """
    with open(file_path, 'a') as file:
        file.write(data)