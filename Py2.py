#Task 2: Program to check Leap Year

year = int(input("Enter a year:"))
if(year %400==0) and (year % 100 == 0):
   print("{0} is Leap Year".format(Year))
elif(year %4 ==0) and (year % 100!=0):
    print("{0} is Leap Year".format(Year))
else:
    print("{0} is Not a Leap Year".format(year))
