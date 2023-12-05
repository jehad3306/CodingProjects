import random
import time

# Imported two primes tested from Miller-rabin probabilistic primality test.
n = 11013888543066435209057090280839754899299637386764014766215941433624305950558622083305907511404822937056326394138070357345801060613983232088516655700601889
v = 10800538986411537743559544087635394695614047558805008718035317163941558248339534897313601258017160540110586608264159239197415408840383139418496768740378041 
prime_test_n = int((n - 1) / 2)
prime_test_v = int((v - 1) / 2)

# Recording how long it takes to go through til we find everything
start_time = time.time()

#Find the greatest common divisor between two variables
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
# Pollard rho algorithm: Finding a non-trivial factor of a composite number.
def pollardRho(n):

    # Generating random values, 
    x_0 = random.randint(2, 5000)
    a = random.randint(1, 5000)

    # functions for cycle detection and iteration.
    tortoise = pow(x_0**2 + a, 1, n)
    hare = pow(tortoise**2 + a ,1 , n)

    # This variable is to check how many steps we have taken into the function with the same values for 'n' and 'a'.
    iterations = 0
    max_iterations = 1000

    # Creating variables to check if it is possible a prime number we are testing at not composie
    possiblePrime = 0
    possiblePrime_max_Iteration = 500000

    # Resets the values and try out new values for 'a' and 'n'
    def newPath():
        nonlocal a
        nonlocal x_0
        nonlocal iterations
        nonlocal tortoise
        nonlocal hare
        a = random.randint(1, 5000)
        x_0 = random.randint(2, 5000)

        iterations = 0
        tortoise = pow(x_0**2 + a, 1, n)
        hare = pow(tortoise**2 + a ,1 , n)
        
    # Iterate to the next value
    def nextValue():
        nonlocal iterations
        nonlocal tortoise
        nonlocal hare
        iterations += 1
        tortoise = pow(tortoise**2 + a, 1, n)
        hare = pow(pow(hare, 2) + a, 1, n)


    #Loop til you find a non-trival factor of the composite number 'n'
    while True:

        d = gcd(abs(tortoise - hare), n)

        if(d == 1):
            
            nextValue()
            possiblePrime += 1

            if iterations == max_iterations:
                newPath()
            
            if(possiblePrime == possiblePrime_max_Iteration):
                return None
                 
        
        # Aslong as GCD is not 1 or 'n', we have found a non-trivial factor
        if( d > 1 and d < n):
            return d

        

        # when GCD == n it means that we found a factor of itself. Which is useless and therefore we try out a new path
        # when tortoise == hare it means we have detected a cycle, which could have runned endlessly. Instead we try out a new path.
        if(d == n or tortoise == hare):
                newPath()


#Display result
print(f"prime value: {n}")
print(f"modified prime ((n-1) / 2): {prime_test_n}")
print(f"The non-trivial factor:  {pollardRho(n)}")
       
# Closing the recording
end_time_prime = time.time()

 # Calculate the testing time
testing_time = end_time_prime - start_time

# Display the testing times for prime factor that was found
print(f"Testing time: {testing_time:.7f} seconds")


    