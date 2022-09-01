#התוכנית מחפשת סכום מוגדר במערך ששני איברים ממנו נותנים את סכום המטרה
# שימוש בלולאה אחת
number_ints=[10,20,500,700,1320,1500,1870,1900,1999,2008,2018]
item_end =len(number_ints)-1
item_start=0
target_number= 2020
found = False
while item_end>=item_start and not found:
    sum_nums = number_ints[item_end]+number_ints[item_start]

    if sum_nums<target_number:
        item_start+=1
    else:
        if sum_nums==target_number:
            found = True
            print(f"first number:{number_ints[item_end]}, second number {number_ints[item_start]}")
        item_end-=1

if not found:
    print(f"numbers not found")

