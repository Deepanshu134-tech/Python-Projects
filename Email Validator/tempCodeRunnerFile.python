import re

def is_valid_email(email):
    """
    Validates whether the given string is a properly formatted email address.
    
    Checks:
    - Contains exactly one "@" symbol
    - Local part (before "@") is not empty
    - Domain part (after "@") has at least one dot "."
    - No invalid characters (uses regex for standard email validation)
    
    Returns:
    - True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, email))

if __name__ == "__main__":
    test_emails = [
        "user@example.com",       
        "firstname.lastname@domain.co",  
        "user@sub.domain.com",   
        "invalid@domain",       
        "user@.com",             
        "@domain.com",           
        "user@domain..com",     
        "user@domain.com.",     
        "user@-domain.com",     
    ]
    
    for email in test_emails:
        print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")