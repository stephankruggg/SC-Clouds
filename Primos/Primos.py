class Primos:
    def __init__(self):
        self.__first_number = 2
        self.__primes = []

    def __clearPrimes(self):
        self.__primes = []

    def recursive(self, boundary: int):
        if (boundary == self.__first_number):
            self.__primes.append(self.__first_number)
            return self.__primes
        else:
            self.recursive(boundary - 1)

        if (all(boundary % previous_prime != 0 for previous_prime in self.__primes)):
            self.__primes.append(boundary)
        
        return self.__primes

    def linear(self, boundary: int):
        self.__clearPrimes()
        self.__primes.append(self.__first_number)
        for number in range (3, boundary + 1, 2):
            if (all(number % previous_prime != 0 for previous_prime in self.__primes)):
                self.__primes.append(number)
        
        return self.__primes
