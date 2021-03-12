#for number in range(1,101):
#    if number % 3 == 0 and number % 5 == 0:
#        print("FizzBuzz")
#        continue
#    elif number % 3 == 0:
#        print("Fizz")
#        continue
#    elif number % 5 == 0:
#        print("Buzz")
#        continue
#    print(number)

for num in range(1,101):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)