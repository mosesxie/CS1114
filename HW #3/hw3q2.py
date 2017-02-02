firstPrice = float(input("Please enter the price of the first item: "))

secondPrice = float(input("Please enter the price of the second item: "))

clubCard = input("Do you have a club card (y for yes and n for no): ")

taxRate = float(input("What is the tax rate: "))

basePrice = firstPrice + secondPrice

if (clubCard == "y" or clubCard == "Y"):
    clubDiscount = 0.9

else:
    clubDiscount = 1

if (firstPrice > secondPrice):
    discountedPrice = (firstPrice + (secondPrice / 2)) * clubDiscount

else:
    discountedPrice = (secondPrice + (firstPrice / 2)) * clubDiscount


totalPrice = (discountedPrice * (taxRate/100)) + discountedPrice

roundedbasePrice = round(basePrice, 2)

roundeddiscountedPrice = round(discountedPrice, 2)

roundedtotalPrice = round(totalPrice, 2)
print("Base Price:", roundedbasePrice )

print("Discounted Price:", roundeddiscountedPrice)

print("Total Price:", roundedtotalPrice)
