size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print asterisks in the row
    for _ in range(size):
        print("*", end="")
    
    # Move to the next line after each row
    print()
    
    # Increment row counter
    row += 1