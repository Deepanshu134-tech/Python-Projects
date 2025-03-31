import re

def check_password_strength(password):
    """
    Evaluates the strength of a password based on multiple criteria.
    
    Args:
        password (str): The password to evaluate
        
    Returns:
        dict: A dictionary containing:
            - strength (str): 'Weak', 'Medium', or 'Strong'
            - feedback (list): List of suggestions for improvement
            - score (int): Numerical score (0-100)
    """
    score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password too short (minimum 8 characters)")
    elif len(password) >= 12:
        score += 25
    else:
        score += 15
    
    if re.search(r'[A-Z]', password):
        score += 15
    else:
        feedback.append("Add uppercase letters")
    
    if re.search(r'[a-z]', password):
        score += 15
    else:
        feedback.append("Add lowercase letters")
    
    if re.search(r'[0-9]', password):
        score += 15
    else:
        feedback.append("Add numbers")
    
    if re.search(r'[^A-Za-z0-9]', password):
        score += 15
    else:
        feedback.append("Add special characters")
    
    if re.search(r'(.)\1{2,}', password):
        score -= 10
        feedback.append("Avoid repeated characters")
    
    common_patterns = ['123', 'abc', 'qwerty', 'password']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 15
        feedback.append("Avoid common patterns")
    
    if score < 50:
        strength = "Weak"
    elif score < 75:
        strength = "Medium"
    else:
        strength = "Strong"
    
    if strength == "Strong" and len(feedback) == 0:
        feedback.append("Excellent password!")
    
    return {
        'strength': strength,
        'feedback': feedback,
        'score': min(max(score, 0), 100)  
    }

def main():
    print("PASSWORD STRENGTH CHECKER")
    print("-------------------------")
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        result = check_password_strength(password)
        
        print(f"\nPassword Strength: {result['strength']}")
        print(f"Security Score: {result['score']}/100")
        
        if result['feedback']:
            print("\nSuggestions for improvement:")
            for suggestion in result['feedback']:
                print(f"- {suggestion}")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    main()