# The Sieve of Eratosthenes

limit = int(input("Enter a limit to display all prime numbers up to it: "))
all_prime = []

for i in range(0, limit + 1):
    all_prime.append(i)
all_prime[1] = 0
p = 2
while p < limit:
    for i in range(p * 2, limit + 1, p):
        all_prime[i] = 0
    p += 1
    while p < limit and all_prime[p] == 0:
        p += 1

print("The primes up to {} are: ".format(limit))
for i in all_prime:
    if all_prime[i] != 0:
        print(i)
