import math
def is_strong_number(num):
  
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in str(num))
    return sum_of_factorials == num

# Print all strong numbers between 1 and 5000
print("Strong numbers between 1 and 5000 are:")
for number in range(1, 5001):
    if is_strong_number(number):
        print(number)