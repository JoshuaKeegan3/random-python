def solution(i):
   """The function returns a string of numbers
   finds all prime numbers starting from 2 until the sum of the characters is > i+5
   returns the last 5 characters
   """
   # Initualise variables
   primes = []                # All found primes used in calculation of next primes

   curr_number=2              # Current number to check if is prime
                              # Initalised at the first prime 

   prime_string =""           # String of all found prime numbers

   # Get all the required primes
   while len(prime_string)<i+5: # While we don't have all required indicies

      # Check if the number is prime
      for prime in primes:
         if curr_number%prime==0: # If it is go to the next number
            break
      else: 
         primes.append(curr_number) # Add the prime to the list for future calculations

         # Add the characters to the character string
         for c in str(curr_number): 
            if len(prime_string)<i+5: # Stop over flow
               prime_string+=c

      # Got to the next number
      curr_number+=1

   # Take the last 5 values
   prime_string = prime_string[-5:]
   return prime_string

