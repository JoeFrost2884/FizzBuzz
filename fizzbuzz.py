for num in range(1,101): # for loop to go through number range 1 - 101
    if num % 5 == 0 and num % 3 == 0: # if statement to check if number is  divisible by 3 and 5
        print("FizzBuzz") # print FizzBuzz if statement is true
    elif num % 3 == 0:   # else if statement to check if number is divisible by 3 with a remainder of 0
        print("Fizz")   # print Fizz if statement is true
    elif num % 5 == 0:   # else if statement to check if number is divisible by 5 with a remainder of 0
        print("Buzz")   # print Buzz if statement is true
    else:
        print(num)# print after all statements are false