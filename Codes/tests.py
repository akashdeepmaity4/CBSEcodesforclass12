n = int(input("Enter the number of terms: "))
def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    return sequence

print(f"The Fibonacci sequence up to {n} terms is: {fib(n)}")
