"""
Last Editted October 10, 2023
Branigan McPeters

File Purpose:
To practice exercising the fibonacci iterative algorithm in Python

Recursive Algoirthm:
    int fib(int n)
    {
        if (n <= 2) return 1
        else return fib(n-1) + fib(n-2)
    }

Iterative Algorithm:
    int fib(int n)
    {
        int f[n+1];
        f[1] = f[2] = 1;
        for (int i = 3; i <= n; i++)
            f[i] = f[i-1] + f[i-2];
        return f[n];
    }

Notes:
A fibonacci  number is only a fibonacci number if it satisfies either or both:
5(n^2)+4
and/or
5(n^2)-4

"""
# Import tools
import math


def is_perfect_square(num):
    """
    Description: Function to determine if a given number is a perfect square
    Params:
        number: The number to check as a perfect square
    Returns:
        bool: returns true if the number is a perfect square, return false otherwise
    """

    # Get the square root of the number
    squareroot = int(math.sqrt(num))
    # return a bool if the square root squared is the same number
    return (pow(squareroot, 2) == num)


def fibonacci_validation(number):
    """
    Description: Function that validates the fibonacci number (should not be negative or decimal)
    Params:
        number: The fibonacci number to validate
    Returns:
        int: return 0 if value less than or equal to zero, -1 if non-positive, and the fib number if valid
    """

    if (number <= 0):
        print("Value is less than or equal to zero. \n My result for non-positive integers will always be zero.")
        return 0
    elif (int(number) is not number):
        print("Value is not an integer number. I will only perform calculations on integer values.")
        return -1
    else:
        return number


def fibonacci_iterative(number):
    """
    Description: Function that computes the fibonacci number based on a number of iterations
    Params:
        number: A value to represent the number of iterations through the algorithm
    Returns:
        value2: The resulting fibonacci number

    Big O: 
    Time complexity: O(n)
    """

    if (number <= 0):
        return 0
    else:
        # Initial values starting with 0 and 1
        # These are the first numbers in the sequence so if number is 1,
        # The fibonacci sequence will still be 1
        value1, value2 = 0, 1
        for i in range(number):
            value1, value2 = value2, value1 + value2
        return value2


def is_fibonacci(number):
    """
    Description: Function to determine if a given number is a fibonacci number
    Params:
        number: The number to check as a fibonacci number
    Returns:
        bool: returns true if the number is a fibonacci number, return false otherwise

    Big O: 
    Time Complexity: O(log n)
    """

    fib = 0
    for i in range(number):
        fib = fibonacci_iterative(i)
    # return if fib is 0 or if the number is a perfect square meeting the requirement
    return fib == number or is_perfect_square(5 * pow(number, 2) + 4) or is_perfect_square(5 * pow(number, 2) - 4)


def main():
    # Driver Function
    test_iterative = 15
    print("\nResults from Iterative Fibonacci: ")
    for i in range(test_iterative):
        print(fibonacci_iterative(i))

    test_is_fib = 10
    print("\nResults from Is_Fibonacci: ")
    for i in range(test_is_fib):
        print(is_fibonacci(i))


if __name__ == "__main__":
    main()
