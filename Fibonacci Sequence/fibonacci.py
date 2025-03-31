def generate_fibonacci(n):
    """
    Generates the Fibonacci sequence up to 'n' terms.
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        list: Fibonacci sequence up to n terms
    """
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

def main():
    print("FIBONACCI SEQUENCE GENERATOR")
    print("---------------------------")
    
    while True:
        try:
            num_terms = int(input("\nEnter number of terms (or 0 to quit): "))
            
            if num_terms == 0:
                print("Goodbye!")
                break
            elif num_terms < 1:
                print("Please enter a positive integer.")
                continue
                
            fib_sequence = generate_fibonacci(num_terms)
            
            print(f"\nFibonacci sequence with {num_terms} terms:")
            print(", ".join(map(str, fib_sequence)))
            
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()