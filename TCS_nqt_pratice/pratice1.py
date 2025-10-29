"""
Level 1 – Easy Scenario Problems (1–7)

1️⃣ Coffee Shop Discount

A coffee shop gives a 10% discount if the bill exceeds ₹500.
Write a program to take the bill amount as input and print the final payable amount.

2️⃣ Attendance Check

A student must have at least 75% attendance to sit for exams.
Input total classes and attended classes, then check eligibility.

3️⃣ Parcel Weight Charge

A courier service charges ₹50 for up to 5 kg and ₹10 for every extra kg.
Input the parcel weight and print the total charge.

4️⃣ Movie Ticket Booking

Each movie ticket costs ₹120. If more than 5 tickets are booked, a 20% discount applies.
Input number of tickets and print total amount.

5️⃣ Restaurant Tip Calculator

A restaurant adds 10% tip automatically if the bill exceeds ₹1000.
Input bill amount and calculate total.

6️⃣ Electricity Bill Calculator

Electricity tariff:

Up to 100 units: ₹5/unit

101–300 units: ₹7/unit

Above 300 units: ₹10/unit
Input units and display the bill amount.

7️⃣ Employee Bonus

Employees with over 5 years of experience get a 5% bonus on salary.
Input years of experience and basic salary, print final salary.

🟡 Level 2 – Moderate Scenario Problems (8–14)

8️⃣ Student Grading System

A student gets grades based on average marks:

90+: A

80–89: B

70–79: C

Below 70: Fail
Input marks in 3 subjects and print grade.

9️⃣ Bank Account Interest

A savings account gives 4% annual interest.
Input balance and time (in years), calculate simple interest.

🔟 Speed Limit Violation

If a car exceeds 80 km/h, it’s fined ₹500 plus ₹50 for every km above 80.
Input the speed and calculate fine.

11️⃣ Employee Tax Calculation

Annual salary tax rates:

≤ ₹250,000 → No tax

₹250,001–₹500,000 → 10%

₹500,001–₹1,000,000 → 20%

₹1,000,000 → 30%
Input salary and compute tax.

1⿢ Online Exam Result

Students pass if they get at least 40% in each subject and 50% overall.
Input marks of 3 subjects, check pass/fail.

1⿣ Railway Ticket Reservation

If seats are full, print “Waiting List”.
If fewer than 10 seats left, print “Hurry! Few seats left.”
Otherwise, print “Seats Available”.

1⿤ E-commerce Order Delivery

If the customer’s city is “Metro”, delivery charge = ₹50; otherwise ₹100.
Input city name and print delivery charge.

"""
bill = int(input("bill: "))
dis= 0.1
if bill>=500:
    total_bill = bill-(bill*dis)
else:
    total_bill = bill
print(total_bill)
print("-------------------------------------------------")
tot_class = int(input("tot class: "))
present_class = int(input("present class: "))
per = (present_class/tot_class)*100
if per>=75:
    print("eligible")
else:
    print("not eligible")

print("-------------------------------------------------")

parcel_wei = int(input("weight: "))
cost =50
if parcel_wei <=5:
    cost = 50
elif parcel_wei >5:
    weight = parcel_wei-5
    extra = weight*10
    cost+=extra
print(f" parcel: {parcel_wei}, cost: {cost}")
print("-------------------------------------------------")
movie_ticket_price = 120
no_of_tick= int(input("tick enter: "))
tot_price=0
if no_of_tick >5:
    dis=no_of_tick*movie_ticket_price*0.2
    tot_price= (movie_ticket_price*no_of_tick)-dis
    
else:
    tot_price= movie_ticket_price*no_of_tick
print(tot_price)
print("-------------------------------------------------")

print("resturant tip calculator")
bill = int(input("enter resturant bill: "))
tot_bill = 0
if bill>=1000:
    dis = bill*0.1
    tot_bill = bill- dis
else:
    tot_bill = bill
print(tot_bill)
print("-------------------------------------------------")
print("electricity bill")
units = int(input("enter units: "))
charg_per_unit=0
tot_charg=0
if units<=100:
    charg_per_unit= 5
    tot_bill = units*charg_per_unit
elif units>100 and units <=300:
    charg_per_unit = 7
    tot_bill = units*charg_per_unit
elif units>300:
    charg_per_unit = 10
    tot_bill = units*charg_per_unit
print(f"units: {units} bill: {tot_bill}")
print("-------------------------------------------------")
emp_exp = int(input("enter exp: "))
salary = int(input("enter salary: "))
tot_salary=0
if emp_exp >=5:
    bonus = salary*(0.05)
    tot_salary = salary+bonus
else:
    tot_salary = salary
print(tot_salary)
print("-------------------------------------------------")
print("student Grading system")
s1=int(input("s1:"))
s2=int(input("s2:"))
s3 = int(input("s3:"))
marks = (s1+s2+s3)/3
grade = ""
if marks>=90:
    grade = "A"
elif marks>=80 and marks<=89:
    grade="B"
elif marks>=70 and marks<=79:
    grade="C"
else:
    grade = "fail"
print(grade)
print("-------------------------------------------------")
print("Bank account Interset")
balance = int(input("enter balance: "))
time = int(input("enter years: "))
interest = balance*0.4
tot_balance = balance+(time*interest)
print(tot_balance)
print("-------------------------------------------------")
print("speed limit violation")
car_speed_km = int(input("enter km: "))
fine = 0
if car_speed_km==80:
    fine =500
elif car_speed_km>80:
    extra = car_speed_km - 80
    fine= 500 + (50*extra)
print(f"car speed: {car_speed_km} fine : {fine}")
print("-------------------------------------------------")
print("employee tax calculation")
annual_salary = int(input("enter salary: "))
tax=0
if annual_salary<=250000:
    tax=0
elif annual_salary>250000 and annual_salary<=500000:
    tax = annual_salary*0.1
elif annual_salary>500000 and annual_salary<1000000:
    tax = annual_salary*0.2
elif annual_salary >=1000000:
    tax = annual_salary*0.3
print(f"LPA: {annual_salary} tax: {tax} ")

print("-------------------------------------------------")

print("Online Exam Result")
s1 = int(input("s1: "))
s2 = int(input("s2: "))
s3 = int(input("s3: "))
avg= (s1+s2+s3)/3
if s1 >=40 and s2>=40 and s3>40 and avg>=50:
    print("pass")
else:
    print("fail")
print("-------------------------------------------------")
print("Railway Ticket Reservation")
n = int(input("enter no.seats reserved: "))
if n==50:
    print("Waiting List")
elif n>=40 and n<50:
    print("Hurry Few seats left")
else:
    print("Seats available.")
print("-------------------------------------------------")

print("E-commerce order Delivery")
city = input("enter city: ")
charge = 0
if city=='Metro':
    charge = 50
else:
    charge = 100
print(f"city: {city} delivery charge: {charge}")

"""
bill: 666
599.4
-------------------------------------------------
tot class: 66
present class: 50
eligible
-------------------------------------------------
weight: 8
 parcel: 8, cost: 80
-------------------------------------------------
tick enter: 6
576.0
-------------------------------------------------
resturant tip calculator
enter resturant bill: 1001
900.9
-------------------------------------------------
electricity bill
enter units: 500
units: 500 bill: 5000
-------------------------------------------------
enter exp: 7
enter salary: 60000
63000.0
-------------------------------------------------
student Grading system
s1:88
s2:78
s3:90
B
-------------------------------------------------
Bank account Interset
enter balance: 9000
enter years: 1
12600.0
-------------------------------------------------
speed limit violation
enter km: 88
car speed: 88 fine : 900
-------------------------------------------------
employee tax calculation
enter salary: 700000
LPA: 700000 tax: 140000.0 
-------------------------------------------------
Online Exam Result
s1: 99
s2: 88
s3: 35
fail
-------------------------------------------------
Railway Ticket Reservation
enter no.seats reserved: 11
Seats available.
-------------------------------------------------
E-commerce order Delivery
enter city: Metro
city: Metro delivery charge: 50

"""

