----------------------------------------------------------- Prime Numbers and Factorization Project ----------------------------------------------------------------------------

This repository contains the implementation and investigation of two prominent algorithms for finding large prime numbers and integer factorization. The project is divided into two parts:
Part 1: Probabilistic Primality Testing

    Algorithm: Implemented and tested the Miller-Rabin algorithm for probabilistic primality testing.
    Primes: Found two 512-bit primes, denoted as p1 and p2.
    Primality Testing: Applied the Miller-Rabin algorithm to test the primality of each found prime.
    Comparison: Compared the testing time for both primes.

Part 2: Factoring

    Algorithm: Implemented and tested the Pollard Rho Algorithm for integer factorization.
    Factorization: For each prime p1 and p2 found in Part 1, factorized (pi - 1)/2 (if possible) and provided non-trivial factors.
    Handling: Explained the handling of cases where factorization of a prime number is not possible to avoid indefinite algorithm runtime.
    Timing: Provided the time required for finding both primes p1 and p2, as well as the factoring time for both cases

Some changes has been made and modified, such as Pollard rho algorithm runs til it finds a non-trivial factor, while most standard cases it tast and stops when it does not find a non-trival factor.