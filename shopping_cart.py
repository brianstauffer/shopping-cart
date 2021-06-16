
# define products
#products = [
#    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
#] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

from pandas import read_csv

import os

# import products from .csv
csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")

df = read_csv(csv_filepath)

products = df.to_dict("records")

valid_options = str([i["id"] for i in products])

# convert to USD formart
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# setup
import os
import dotenv
dotenv.load_dotenv()
import datetime

datetime = datetime.datetime.now()

# enter POS system
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

# input items for shopping cart and validate
# used https://www.programiz.com/python-programming/if-elif-else for help with if/elif/else
selected_ids = []
while True:
    selected_id = input("Please input product ID: ")
    selected_id = selected_id.strip()
    if selected_id.upper() == "DONE":
        break
    elif selected_id == "":
        print("Invalid selection, please try again")
    elif selected_id in valid_options:
        selected_ids.append(selected_id)
    else:
        print("Invalid selection, please try again")

# format and print receipt
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
print("Today you purchased: ")

# aggregate shopping list with item, price, and subtotal
subtotal = 0

for selected_id in selected_ids:
    matching_product = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_product[0]
    print(f"... {matching_product['name']}  ({(to_usd(matching_product['price']))})")
    subtotal = (matching_product["price"])+subtotal

print("----------")
print(f"Subtotal: {to_usd(subtotal)}")

# calculate tax using .env
tax_rate = float(os.getenv("tax_rate"))
tax = to_usd(subtotal*tax_rate)
print(f"Tax: {tax}")

# total up bill
total = to_usd((1+tax_rate)*subtotal)
print(f"Total: {total}")
print("----------")
print("Thank you for shopping, please come again soon!")
print("")
print("************************************************************")
print("")