#Yenesis Rabelo Multiplication Table

# asking the user for the number they would like multiples of
number = int(input("Enter a number to see its multiplication table (0-12): "))

# looping through numbers 0 to 12 and print the multiplication results
for i in range(13):
    # Print each multiple, formatted in a readable way
    print(f"{number} x {i} = {number * i}")