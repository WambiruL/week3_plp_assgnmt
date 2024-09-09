# Create a method that tests whether the result of taking the power of one number to another 
# number provides an answer which is greater than 5000. We will use a conditional statement to 
# return True if the result is greater than 5000 or return False if it is not. 

def large_power(base, exponent):
    if base ** exponent > 5000:
        print('True')
    else:
        print('False')

power = large_power(8,3)
    