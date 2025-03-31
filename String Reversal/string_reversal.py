def reverse_string(input_string):
    """Return the reverse of the input string."""
    return input_string[::-1]

if __name__ == "__main__":
    test_string = "hello"
    reversed_string = reverse_string(test_string)
    print(f"Reversed string: {reversed_string}")
