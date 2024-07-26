''' Implement a Python module named string_utils.py containing functions for string manipulation, such as
reversing and capitalizing strings.'''


def reverse_string(s):
    """
    Return the reversed version of the input string.
    """
    return s[::-1]

def capitalize_string(s):
    """
    Return the input string with the first character capitalized and the rest lowercased.
    """
    return s.capitalize()