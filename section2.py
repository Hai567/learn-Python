## Exercise 1: 

## Exercise 2: 

## Exercise 3: Solve The ax + b = 0  Equation
# print("Solve Equation: ax + b = 0")
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# print(f"x = {-b/a}")

## Exercise 4: Solve The ax^2 + bx + c = 0 Equation
# import math
# print("Solve Equation Of ax^2 + bx + c = 0")
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))
# if a == 0: 
#     print(f"x = {-b/a}")
# else:
#     delta = (b**2 - (4*(a*c)))
#     if delta < 0:
#         print(f"The Equation {a}x^2 + {b}x + {c} = 0 Has No Solution")
#     elif delta == 0 :
#         print(f"x = {-b/2*a}")
#     else:
#         print(f"x = {((-b - math.sqrt(delta)) / 2*a)} And x = {((-b + math.sqrt(delta)) / 2*a)}")

## Exercise 5: 
##  Viết chương trình nhập vào lương cơ bản, số năm công tác, 
## in ra tiền lương hàng tháng có tính số % phụ cấp thâm niên theo 
## công thức:
##  Lương hàng tháng = lương cơ bản + phụ cấp thâm niên
##  Nếu số năm công tác dưới 5 năm: phụ cấp thâm niên 0%
##  Nếu số năm công tác trên 5 năm, phụ cấp thâm niên được tính 
## theo % số năm công tác. Thí dụ người A có 6 năm thâm niên, vậy 
## phụ cấp thâm niên của A là 6% * lương cơ bản.

# basicSalary = float(input("Enter your basic salary (Salary when you deal with recuiter): "))
# workingYear = float(input("Enter number of years you have been working for that company: "))
# seniorAllowence = 0
# if workingYear < 5:
#     seniorAllowence = 0
# else:
#     seniorAllowence = (basicSalary / 100) * 6
# salaryPMonth = basicSalary + seniorAllowence
# print(f"Your Salary Per Month Approximately {salaryPMonth} (Money Unit)")

## Exercise 6: 
## Viết chương trình nhập vào năm sinh, in ra tuổi. Lưu ý nếu 
## năm sinh nhập vào không hợp lệ (giá trị âm, hoặc lớn hơn năm hiện 
## tại, hoặc giá trị nhập vào là chuỗi) thì hiện thị ra thông báo 
## đồng thời gán giá trị mặc định là năm hiện tại.

# from datetime import date
# currentYear = date.today().year
# try: 
#     yearBorn = int(input("Enter The Year You Was Borned: "))
#     if yearBorn > currentYear:
#         print(f"Your Birth Year Can Not Be Greater Than {currentYear}")
#     else:
#         print(f"You Are {currentYear - yearBorn} Years Old")
# except:
#     print("Please Enter Valid Value, Your Birth Year Must Be An Integer")

## Exercise 7: 
## Taxi fare is calculated according to the formula: the first 1km from the time of boarding: 13000 VND.
## Each subsequent kilometer is charged at a unit price of 12000 VND. From km 30 and above, each kilometer is counted as 9000 VND.
##  Write A Program Gets Kilometers Traveled As Input And Print The Price Of It

# kmTraveled = float(input("Enter Number Of Kilometers You Have Traveled: "))
# price = 0
# if kmTraveled <= 1:
#     price = 13000
# elif kmTraveled > 1 and kmTraveled < 30:
#     price = 13000 + (kmTraveled - 1) * 12000
# else:
#     price = kmTraveled * 9000
# print(f"You Have To Pay {price} VND for {kmTraveled} KM You Have Traveled")

## Exercise 8:
## The total number of working hours specified for an employee in a week is 40 hours,
## if the employee works more than the specified number of hours, then each hour more will be counted as 1.5 hours.
## Get the hourly wage, the number of hours worked in the week as input then print out the salary to be paid for the week.
# hourlyWage = float(input("Enter Your Hourly Wage: "))
# workingHour = float(input("Enter Number Of Hour You Work In A Week: "))
# wagePMonth = 0
# if workingHour > 40:
#     wagePMonth = (workingHour * hourlyWage) +  ((workingHour - 40) / 1.5) * hourlyWage
# else:
#     wagePMonth = hourlyWage * workingHour
# print(f"Your Wage Per Month Is {wagePMonth}")