#factorial
import math   
def factorial(number):
    for i in range(number):

        n = int(math.factorial(i))
        if n == number:
            print("yes.")
            break
        else:
            pass
number = int(input("Enter the number: "))
factorial(number)