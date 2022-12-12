class Number:
    def __init__(self, value):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        if self.value % 2 == 1:
            return True
        else:
            return False

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        if self.value % 2 == 0:
            return True
        else:
            return False

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        count = 0
        n = self.value
        for i in range(1,n+1):
            if n % i == 0:
                count += 1
        if count == 2:
            return True
        else:
            return False

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors = []
        n = self.value
        for i in range(1,n+1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        n = self.value
        count = 0
        i = 0
        while n >= i:
            count += 1
            n //= 10
            i += 1
        return count

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        n = self.value
        s = 0
        i = 0
        while n >= i:
            s += n%10
            n //= 10
            i+=1
        return s

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        n = self.value
        return int(str(n)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        n = self.value
        if n == (str(n)[::-1]):
            return True
        else:
            return False

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        n = self.value
        digits = []
        i = 0
        s = 0
        while n >= i:
            s = n % 10
            digits.append(s)
            n //= 10
            i += 1
        digits.reverse()
        return digits

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        pass

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        pass

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        pass

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(13)
print(number.get_number())
print(number.is_odd())
print(number.is_even())
print(number.is_prime())
print(number.get_divisors())
print(number.get_length())
print(number.get_sum())
print(number.get_reverse())
print(number.is_palindrome())
print(number.get_digits())
print(number.get_max())
print(number.get_min())
print(number.get_average())
print(number.get_median())
print(number.get_range())
print(number.get_frequency())