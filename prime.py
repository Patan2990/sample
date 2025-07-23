def is_prime(num):
   
    if num <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True  # If no divisors found, it's prime

print("Prime numbers between 1 and 100 are:")
for number in range(1, 101):
    if is_prime(number):
        print(number)