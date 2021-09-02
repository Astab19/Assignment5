max_int = 0
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
while num_int > 0:
    for number in range(1,num_int+1):
        if number > max_int:
            max_int = number
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)    
