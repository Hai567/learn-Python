## Exercise 1: Print Hello World
#print("Hello World!")

## Exercise 2: Convert Fahrenheit Unit To Celcius
# f = int(input("Enter Fahrenheit Unit: "))
# c = round((5*(f - 32) / 9), 4)
# print(f"{f} fahrenheit degree is {c} celcius degree")

## Exercise 3: Print Sum Of Square Of 2 Integer Input
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# sumOfSqr = (num1**2) + (num2**2)
# print(f"Sum Of Square Of {num1} and {num2} Is {sumOfSqr}")

## Exercise 4: Print Subtraction Of Square Of 2 Integer Input
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# subOfSqr = (num1**2) - (num2**2)
# print(f"The Subtraction Of {num1} Power 2 And {num2} Power 2 Is {subOfSqr}")

## Exercise 5: Get A Number With 2 Numbers Then Print Its Units And Tens
# num = input("Enter A Number With 2 Numbers: ")
# print(f"The Units Of {num} Is {num[1]} And The Tens Is {num[0]}")

## Exercise 6: Get A Number And Print The Reverse Of Its
# num = input("Enter A Number With 2 Numbers: ")
# print(f"{num[1]}{num[0]} Is The Reverse Of {num}")

## Exercise 7: Get Any Input Then Print It And Its Type Of Value
# randomInput = input("Enter Anything: ")
# from ast import literal_eval
# def get_type(input_data):
#     try:
#         return type(literal_eval(input_data))
#     except (ValueError, SyntaxError):
#         # A string, so return str
#         return str
# dataType = get_type(randomInput)
# print(dataType)

## Exercise 8: Write a program to input the main salary(salary per day), allowance and number of working days in the month, print out the salary per month received according to the formula: 
## salary-per-month = ((main-salary + allowance) / 22) x working-day
# pDaySalary = float(input("Enter Your Salary Per Day: "))
# allowance = float(input("Enter Your Allowence (IF HAVE): "))
# workingDay = float(input("Enter Number Of Day You Work Each Month: "))
# salaryPMonth = ((pDaySalary + allowance) / 22) * workingDay
# print(f"Your Salary Per Month Is {round(salaryPMonth, 3)} (Money Unit)")