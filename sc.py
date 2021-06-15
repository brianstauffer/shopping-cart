products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#print(len(products))

import datetime

datetime = datetime.datetime.now()

print("")
print("")
print("")
print("************************************************************")
print("")
print("Welcome to Hoboken Grocer's Point of Sale Program!")

print(datetime.strftime("%a %d %b")+(" ")+datetime.strftime("%H")+(":")+datetime.strftime("%M"))
print("")
print("Please select / scan a valid product ID. When complete, enter 'Done'")
print("")
print("-----")

valid_options = str([i["id"] for i in products])

# 1) capture product IDs until we're done
    # use infinite while loop

selected_ids = []

# used https://www.programiz.com/python-programming/if-elif-else for help with if/elif/else

while True:
    selected_id = input("Please input product ID: ")
    if selected_id.upper() == "DONE":
        break
    elif selected_id in valid_options:
        selected_ids.append(selected_id)
    else:
        print("Invalid selection, please try again")

class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print("")
print("************************************************************")
print("---------")
print('|' + color.BOLD + 'RECEIPT' + color.END + '|')
print("---------")
print("Hoboken Grocer")
print(color.UNDERLINE + 'www.HobokenGrocer.com' + color.END)
print("----------")
print(f"Checkout at: {datetime.strftime('%a %d %b')} {datetime.strftime('%H')}:{datetime.strftime('%M')}")
print("----------")

#print("Shopping cart list includes items: ",selected_ids)

#selected_ids = [1,2,3,2,1]

# 2) perform product look ups to determine what the product's name and price are

print("Today you purchased: ")
subtotal = 0

for selected_id in selected_ids:
    #print(selected_id)
    # look up the corresponding product
    # display the selected product's name and price

    matching_product = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_product[0]
    print(f"... {matching_product['name']}  ({(to_usd(matching_product['price']))})")
    subtotal = (matching_product["price"])+subtotal

print("----------")
#print("Subtotal: ",to_usd(subtotal))
print(f"Subtotal: {to_usd(subtotal)}")

taxrate = .0875
tax = to_usd(subtotal*taxrate)
print(f"Tax: {tax}")

total = to_usd((1+taxrate)*subtotal)
print(f"Total: {total}")
print("----------")
print("Thank you for shopping, please come again soon!")
print("")
print("************************************************************")
print("")
    # use list comprehension to print