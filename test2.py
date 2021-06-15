products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49}
]

selected_ids = []
selected_id = []

while True:
    while True:
        try:
            selected_id = input("Please input product ID: ")
            selected_id = [p for p in products if str(p["id"]) == str(selected_id)]
            selected_id = selected_id[0]
            if IndexError:
                print("invalid item")
                continue                
        break
    except IndexError:
        print("Invalid item, please try again")
        continue         
    #if selected_id.upper() == "DONE":
        #break
    #else:
        #selected_ids.append(selected_id)


for selected_id in selected_ids:
    #print(selected_id)
    # look up the corresponding product
    # display the selected product's name and price

    try:
        matching_product = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_product[0]
        print("found matching product")
    except IndexError:
        print("invalid product")