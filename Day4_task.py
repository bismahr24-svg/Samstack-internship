# Task 1: Create a division function using try-except to handle ZeroDivisionError and ValueError without crashing the program.

print("----Task 1 ----")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    def divide(num1, num2):
        return num1 / num2
    result = divide(num1, num2)
    print(result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
  
# Task 2: Extract ID and Email from the given string using string methods and store the data in a dictionary format.

print("----Task 2 ----")
raw_data = "Name: Bisma | ID: 1024 | Status: Active | Email: bisma@example.com"
parts = raw_data.split("|")
id_value = parts[1].split(":")[1].strip()
email_value = parts[3].split(":")[1].strip()
data = {
    "ID": id_value,
    "Email": email_value
}
print(data)
  
# Task 3: Create a custom InvalidSemesterError exception to validate student semester (1-8) and handle the error using try-except.

print("----Task 3 ----")
class InvalidSemesterError(Exception):
    pass
def check_semester():
    semester = int(input("Enter your semester: "))
    if semester < 1 or semester > 8:
        raise InvalidSemesterError( "Invalid semester: Please enter a value between 1 and 8."
        )
    print("Valid semester:", semester)
try:
    check_semester()
except InvalidSemesterError as error:
    print(error)
except ValueError:
    print("Please enter a valid number.")
  

