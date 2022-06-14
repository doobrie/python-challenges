def is_palindrome(value: str) -> bool:
    """Calculate whether a given string is a palindrome or not.
    Only alpha characters are compared.  Which space and pther characters are ignored.
    The case of the input string is ignored.

    Args:
        value (str): The input string to validate

    Returns:
        bool: Returns True if the string is a palindrome, False otherwise.
    """
    parsed_string = value.lower()
    parsed_string = ''.join(filter(str.isalpha, parsed_string))
    reversed_string = parsed_string[::-1]
    return parsed_string == reversed_string


print(is_palindrome('hello'))
print(is_palindrome('race CAR!!'))
