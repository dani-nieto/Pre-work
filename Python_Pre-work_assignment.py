#Danyella Nieto

#Question 1:
#create function hello_name
def hello_name(user_name): 
    user_name = user_name.upper()
    return ("hello_{}!".format(user_name))

#create opportunity for user input
user_name = input("Enter Your Username: ").upper()
#print and call function
print(hello_name(user_name))



#Question 2

#create a function to print out odd numbers from 1-100 and return nothing
def first_odds():
    for x in range(0,100):
        if x%2 != 0:
            print(x)
        else:
            pass
    return

print(first_odds())



#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max

print(max_num_in_list([10,5,73,0,16]))


#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if(a_year % 400 == 0): 
        print("Given Year is a leap Year")
    elif (a_year % 100 != 0) and (a_year % 4 == 0):
        print("Given Year is a leap Year")
    else:
        print("Given year is not a leap year")
print(is_leap_year(2024))


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    range_list = list(range(min(a_list), max(a_list)+1))
    if range_list == sorted_list:
        return True
    else:
        return False
     

list_test = [2, 3, 1, 4, 5]
print(is_consecutive(list_test))


