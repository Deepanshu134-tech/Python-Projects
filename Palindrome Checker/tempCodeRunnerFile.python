def is_palindrome(s):
    """
    Checks if a given string is a palindrome. A palindrome reads the same backward as forward.
    This function ignores case, spaces, and punctuation.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned = ''.join(c for c in s if c.isalnum()).lower()
    return cleaned == cleaned[::-1]

# Test cases
test_strings = [
    "madam",
    "racecar",
    "A man, a plan, a canal, Panama!",
    "hello",
    "12321",
    "No 'x' in Nixon",
]

print("Palindrome Test Results:")
for s in test_strings:
    print(f'"{s}": {is_palindrome(s)}')