# Prime numbers

def is_prime (num):
    for i in range(2,num):
        if num%i ==0:
            return False
    return True

# test = [3,6,11,31]

# for num in test:
#     print(f"{num} is a prime number {is_prime(num)}")

def nth_prime(x):
    num = 3
    prime = 2
    if x == 1:
        return 2
    while prime < x:
        num += 2
        if is_prime(num):
            prime += 1
    return num

x = 10

print("The ", x, "th prime number is ", nth_prime (x),)

primes = [i for i in range (2,200) if is_prime(i)]
print(primes)

