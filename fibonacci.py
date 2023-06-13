
def fibonacci(number):
    fibonacci_numbers = [0, 1]
    total = 1
    print("number " + str(number))
    for index in range(2, number+1):
        total = (
            fibonacci_numbers[-2] +
            fibonacci_numbers[-1]
        )
        fibonacci_numbers.append(total)
        print( "nro fibonacci "+ str(fibonacci_numbers))
        print("resultado " + str(total))
    return total

def fibonacci_1(number):
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


import unittest

class TestFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, fibonacci(1))

    def test_2(self):
        self.assertEqual(1, fibonacci(2))
    
    def test_3(self):
        self.assertEqual(2, fibonacci(3))

    def test_4(self):
        self.assertEqual(3, fibonacci(4))

    def test_5(self):
        self.assertEqual(5, fibonacci(5))

    def test_6(self):
        self.assertEqual(8, fibonacci(6))


if __name__ == '__main__':
    unittest.main()