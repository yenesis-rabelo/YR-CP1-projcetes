# This function should return the sum of all even numbers in the list, but it returns the wrong value. Find the bug.

def sum_even_numbers(numbers):

     sum = 0

     for num in numbers:

          if num % 2 == 0:

               sum += num

     return sum

print(sum_even_numbers([1, 2, 3, 4, 5]))