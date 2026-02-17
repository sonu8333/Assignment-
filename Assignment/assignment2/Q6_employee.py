basic = float(input('Enter Basic Salary:'))

#calculations of  percent to number
#formula to convert
da = 10/100 * basic
ta = 12/100 * basic
hra = 15/100 * basic


#formula for calculation of total salary 

total_salary = basic + da + ta + hra

print("Basic Salary : ", basic)
print("DA (10%): ", da)
print("TA (12%): ", ta)
print("HRA (15%): ", hra)
print("Total Salary: ", total_salary)