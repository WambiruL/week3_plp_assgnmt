# Create a function that determines whether or not a number is divisible by ten. 
# A number is divisible by ten if the remainder of the number divided by 10 is 0.

def divisible_by_ten(num):
    if num % 10 == 0:
        print("True")
    else:
        print("False")

output = divisible_by_ten(23)
     