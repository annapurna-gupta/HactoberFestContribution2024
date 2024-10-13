# Function to calculate sum and count of even numbers
def sum_and_count_even(numbers):
    even_sum = 0
    even_count = 0
    
    # Iterate through each number in the list
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
            even_count += 1
            
    return even_sum, even_count

# Input: List of numbers from user
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

# Get the sum and count of even numbers
even_sum, even_count = sum_and_count_even(numbers)

# Output the result
print(f"Sum of even numbers: {even_sum}")
print(f"Count of even numbers: {even_count}")
