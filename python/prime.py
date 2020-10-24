class Prime():
    
    def __factorial(self,n: int) -> int:
        if n == 1:
            return n
        else:
            return n * self.__factorial(n - 1)


    @staticmethod
    def isPrime(n: int) -> bool: 
        
        if n <= 1:        
            return False
        else:
            for i in range(2,n):
                if (n % i == 0):
                    return False
            return True
    
    @staticmethod
    def addFirstFiftyPrimes() -> int:
        
        sum = 0
        for i in range(0,49):
            if (Prime.isPrime(i)):
                sum += i
            
        return sum

    def addFirstNprimes(self,n: int) -> int:

        num = 0;
        counter = 0
        total = 0;
        while counter < n: 
            if Prime.isPrime(num):
                total += num
                num+=1
                counter+=1
            else: 
                num+=1
        
        return total 
    
    
    def isPrimeWilsonTheorem(self,p: int) -> bool:
        """ 
        Any number n is a prime number if, and only if, (n − 1)! + 1 is divisible by n
        """ 
        if p > 1:  
            return (self.__factorial(p - 1) + 1)  % p == 0
        return False

if __name__ == "__main__":
   
    myPrime = Prime()

    print(f"Add the first primes on range [0- 50]: {myPrime.addFirstNprimes(50)}")
    print(f"Add first 50's primes: {Prime.addFirstFiftyPrimes()}")
    print(f"[Bonus: Wilson's theorem ] Is prime 7: {myPrime.isPrimeWilsonTheorem(7)}")





