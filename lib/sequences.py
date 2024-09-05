#!/usr/bin/env python3
def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    # Start with the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < length:
        # Append the sum of the last two numbers in the list
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    # If length is 1, return only the first element
    if length == 1:
        fibonacci_sequence = fibonacci_sequence[:1]
    
    print(fibonacci_sequence)

pass