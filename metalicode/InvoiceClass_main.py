from InvoiceClass import invoice
from InvoicefruitClass import fruit

invoice01 = invoice()
#check
invoice01.addItem(fruit("banana", 1.5, 9.99))
invoice01.addItem(fruit("apple", 3.0, 5.60))
invoice01.addItem(fruit("egoz", 2.0, 8.90))
invoice01.addItem(fruit("tamar", 5.0, 14.0))
invoice01.addItem(fruit("limon", 2.0, 3.0))


invoice02 = invoice()

invoice02.addItem(fruit("shezif", 1.3, 6.0))
invoice02.addItem(fruit("sabres", 1.0, 2.5))
invoice02.addItem(fruit("melon", 2.0, 9.5))

print(invoice01)
print(invoice02)
print('\nTotal for all invocies:',invoice01+invoice02)
