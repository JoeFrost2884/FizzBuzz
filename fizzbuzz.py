for num in range(1,101): # for loop to go through number range 1 - 101
    containerStr = ""  # empty container string
    if num % 3 == 0:   # if statement to check if number is divisible by 3 with a remainder of 0
        containerStr = containerStr + "Fizz"   # put Fizz into string if statement is true
    if num % 5 == 0:   # if statement to check if number is divisible by 5 with a remainder of 0
        containerStr = containerStr + "Buzz"   # put Buzz into string if statement is true
    if num % 5 != 0 and num % 3 != 0: # if statement to check if number is not divisible by 3 and 5
        containerStr = containerStr + str(num) # print number into string if statement is true
    print(containerStr) # print string after after a statement is true