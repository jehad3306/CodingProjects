import random
import time
import secrets
 

# Generate a random 512-bit number excluding even numbers.
def generateRandomNumber():
    
    random_number = secrets.randbits(512)

    while((random_number % 2) == 0):
        random_number = secrets.randbits(512)
    
    return random_number


#Each function under is code that represents the three main steps to achieve the process of Miller-Rabin probabilistic test.
def stepOne(testNumber):
    k = 0
    m = testNumber

    # Iterate until m is an odd number, updating k and dividing m by 2
    # k isn't necessary for further calculations, however it was used to check if things were working.
    while(m % 2 == 0):
        k += 1
        m //= 2
    
    return m

# Step Two: Generate a list of random integers from the interval [2, 5000] that is going to represent 'a'. 
def stepTwo():

    amountOfIterations = 100

    # Use random.sample to ensure unique integers in the list
    list_of_a = random.sample(range(2, 5000), amountOfIterations)

    return list_of_a


# Step Three: Perform the Miller-Rabin probabilistic test
def stepThree(a, m, testNumber):
    
    iterations = 0

    # calculating first for b_0
    b_zero = pow(a, m, testNumber)  

    # Loop til you find a condition that fulfilles the number to be possibily prime composite   
    while(b_zero != 1) and (iterations < 100):

        # If b_zero is congruent to -1 (mod testNumber), the number is possibly prime
        if(b_zero == testNumber - 1):
            return True
        
        b_zero = (pow(b_zero, 2, testNumber))
        iterations += 1

    # If the loop completes without finding -1 mod n, the number is composite
    return False

# Recording how long it takes to go through til we find everything
start_time = time.time()

# Global variable
n = 0
generateANumber = 0

# Values that after certian amount of calculations represent how many time result are either prime or composite 
prime = 0
composite = 0

# A loop that iterates til it has found a random 512-bit number which has achieved a Miller-Rabin probabilistic primality test above a sample range of 80 from the range of [0, 100]
while(prime < 80):

    
    n = generateRandomNumber()
    generateANumber += 1        

    # Nullify the variables so the variables start at 0 when we try a new 512-bit number
    if(prime , composite > 0):
        prime = 0
        composite = 0

    #Preparing the number before sending them into step one
    n_minus = n - 1


    # Acquiring the value of m from step one
    n_m = stepOne(n_minus)

    # Step Two returns a list of unique integers based on an interval [2, 5000]
    list_a_unique_integers = stepTwo()

  

    # Under we create a loops that go through StepThree based on the number {n}.
    # The loop goes through 100 different values of {a}, which each {a} is unique and depending on the result, we can be more certain if something is a prime or composite.

    # Perform Miller-Rabin test for the number {n} 
    for a in list_a_unique_integers:

        result = stepThree(a, n_m, n)

        if(result == True):
            prime += 1
            
        elif(result == False):
            composite += 1


# Closing the recording
end_time_prime = time.time()

 # Calculate the testing time
testing_time = end_time_prime - start_time

# Display the testing times for the prime that was found
print(f"Testing time: {testing_time:.4f} seconds")

# Display the results
print(f"How many 512-bit number we tested: {generateANumber}")
print(f"The number we tested is: {n}")
print(f"Based on Miller-Rabin primality test we get: (Prime: {prime} , Composite:{composite})")



       