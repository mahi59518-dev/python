#arithmetic operations

a =10
b =3
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("remainder:",a%b)
print("power:",a**b)


#simple calculation
a = int(input("enter first number:"))
b = int(input("enter second number:"))
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)

#students marks calculation
name = input("enter student name:")
m1 = int(input("enter python marks:"))
m2 = int(input("enter java marks:"))
m3 = int(input("enter SQL marks:"))

total =m1+m2+m3
average = total/3
print("total marks:",total)
print("average marks:",average)

print("\n------student report ------")

#shopping bill calculation
price1 = float(input("enter product 1 price:"))
price2 = float(input("enter product 2 price:"))
price3 = float(input("enter product 3 price:"))

total = price1 + price2 + price3

discount = total * 0.10
final_amount = total - discount
print("total bill:", total)
print("discount:", discount)
print("final bill:", total - discount)

#salary calculation
basic = float(input("enter basic salary:"))
hra = basic *0.20
da = basic *0.10
gross_salary =basic + hra + da

print ("basic salary:',basic")
print ("HRA:',hra")
print("DA:",da)
print ("gross_salary:",gross_salary)
