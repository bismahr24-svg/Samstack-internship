# Task 1 :

name= str(input("Enter your name: "))
semester= int(input("Enter your current semester: "))
gpa= float(input("Enter your GPA: "))
print(f"Hello {name}, you are in semester {semester} with a GPA of {gpa}.")
print("Data type of name:", type(name))
print("Data type of semester:", type(semester))
print("Data type of GPA:", type(gpa))

# Task 2 :

numbers = [5, 12, 7, 18, 21, 30, 9, 44, 11, 2]
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Original List:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

# Task 3 :
def is_prime(num):
  if num<=1 :
    return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a Prime Number.")
else:
    print(number, "is not a Prime Number.")
  
