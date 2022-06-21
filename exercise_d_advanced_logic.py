# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_int = []
for number in numbers:
    if number % 2 == 0 and isinstance(number, int):
        even_int.append(number)
print(even_int)

# 2. Print the difference between the largest and smallest value:

# numbers.sort()
# number_gap = numbers[-1] - numbers[0]
# print(number_gap)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
last = None
for number in numbers:
    if number == 2 and last == 2:
        print(True)
    else: 
        last = number
       



# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

    



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#    So [5, 13, 2] would have sum of 5. 





total_numbers = 0

for i, number in enumerate(numbers): # lets i repesent the index
    if number == 13: #checks if number is 13 
        remove = i +1 # sets remove to the index of number after 13 
        while numbers[remove] == 13: #checks the list to make sure their is not another 13 after current 13
            remove += 1 #add another +1 to the index to remove number after second 13
        del numbers[i : remove + 1] # del splices from current index to the next one after a 13 resulting in the 13 and next number being removed
for number in numbers:    #finds total on new array
    total_numbers +=number
print(total_numbers)









