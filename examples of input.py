# calc the area of a rectangle

length = float(input("enter the length of the rectangle:"))
breadth = float(input("enter the breadth of the rectangle"))

area = length * breadth
print (f"the area of the rectangle is {area}cm²")



# ex 2 shopping cart prog

item = input ("what item would you like to buy")
price = float(input("what is the price of the item"))
quantity = int(input("how many would you like to buy"))

total = price * quantity

print(f"you have bought {quantity}x{item} for ${price}")
print(f"your total is ${total}")
