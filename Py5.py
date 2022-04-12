#Task 5: Program to Display Multiplication Table of 5(Format 5 * 1 = 5)

table_num=int(input("Enter the table number which you want to get the multiplication table:"))
for i in range(1,11):
    print(table_num, 'x', i, '=', table_num*i)
