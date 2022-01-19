"""Write a program that asks the user to enter a length. The program should ask them what unit the length is in and what unit they would like to convert it to. The possible units are inches, yards, miles, millimeters, centimeters, meters, and kilometers. While this can be done with 25 if statements, it is shorter and easier to add on to if you use a two-dimensional list of conversions, so please use lists for this problem."""
#we consider default length in feet
feet = int(input("Enter a length in feet: "))
print(""" Choose 1 to convert into inches,
          choose 2 to convert into yards,
          choose 3 to convert into miles,
          choose 4 to convert into mm,
          choose 5 to convert into cm,
          choose 6 to convert into meters,
          choose 7 to convert into km""")
value = int(input("->"))

inches = feet * 12
yards = feet * 0.333
miles = feet * 0.000189
mm = feet * 304.8
cm = feet * 30.4
meters = feet * 0.3048
kms = feet * 0.0003048

conversion = [
               feet,
               inches,
               yards,
               miles,
               mm,
               cm,
               meters,
               kms
          ]

print(conversion[value])
