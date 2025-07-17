import random, math
import time

class PrivateKey:
    def __init__(self, private_key = None,
                bit_size = 256):
        self.__bit_size = bit_size
        self.__private_key = self.__public_key = None
        if private_key is None:
            self.__generate_private_key()
        else:
            self.__private_key = private_key
            self.__check_passed_primary_key()
        self.__generate_public_key()

    def __is_non_zero_division(self, divisor):
        # print(f'Key: {self.__private_key}\nDivisor: {divisor}')
        return self.__private_key % divisor != 0

    def __check_prime(self):
        if self.__private_key is None:
            return False
        square_root_int = int(math.sqrt(self.__private_key)) + 1
        if not self.__is_non_zero_division(2):
            return False
        for divisor in range(3, square_root_int, 2):
            if not self.__is_non_zero_division(divisor):
                return False
        return True

    def __generate_private_key(self):
        while not self.__check_prime():
            self.__private_key = int(random.randrange(pow(2, self.__bit_size)))
    
    def __check_passed_primary_key(self):
        if not self.__check_prime():
            raise ValueError('Key is not a prime number!')
        if pow(2, self.__bit_size) <= self.__private_key:
            raise ValueError('Key is too big!')

    def __generate_public_key(self):
        pass

    def get_private_key(self):
        return self.__private_key