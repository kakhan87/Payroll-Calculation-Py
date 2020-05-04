"""
Created on Wed Feb  5 17:12:12 2020

@author: Karim Khan

Project: Major Assignment 1 - Payroll Calculation

"""
# Define a placeholder to aid the below conditional if statement
# to properly split Regular pay and Overtime pay 
haveAllData = False

# Step 1 - Input Variables

## Enter Employee's name
employeeName = str(input("Enter Employee's Name: "))

## Enter actual number of hours worked
actualNumberOfHours = float(input("Enter number of hours worked by Employee over the week: "))

## Enter employee's hourly rate
hourlyRate = float(input("Enter hourly rate (in $): "))

## Enter a Yes/No response to whether employee is subject for deductions
deductions = input("Should employee have deductions? [Y/N]: ")

if deductions == 'Y':
## If deductions are applicable, enter % of deduction in integer format, 
## otherwise set it to zero
    percentDeduction = int(input("Enter percentage of Gross Pay to be deducted: "))
else:
    percentDeduction = 0

# Step 2 - Calculate Required Variables
    
## If-else statement to accurately calculate Regular pay and Overtime pay 
if actualNumberOfHours <= 40 :
    regularPay = actualNumberOfHours * hourlyRate
    overtimePay = 0
    
elif actualNumberOfHours > 40 :
    regularPay = 40 * hourlyRate
    overtimePay = (actualNumberOfHours - 40) * hourlyRate * 1.5
    
else:
    haveAllData = True

## Calculate Gross Pay
grossPay = regularPay + overtimePay

## Calculate total deductions as a percentage of Gross Pay (if applicable) 
deductions = (percentDeduction / 100) * grossPay

## Calculate Net Pay
netPay = grossPay - deductions

# Step 3 - Print Output
print("Employee's Name:", employeeName)

print("Total hours worked:", actualNumberOfHours)

if actualNumberOfHours > 40 :
    print("Total Overtime hours worked:", (actualNumberOfHours - 40))

else :
    print("Total Overtime hours worked: 0.00")

print("Hourly pay rate: ${:,.2f}".format(hourlyRate))

print("Gross Pay: ${:,.2f}".format(grossPay))

print("Deductions (if applicable): ${:,.2f}".format(deductions))

print("Net Pay: ${:,.2f}".format(netPay))
