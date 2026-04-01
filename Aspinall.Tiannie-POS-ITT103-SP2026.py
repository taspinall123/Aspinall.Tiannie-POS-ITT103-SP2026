# Author: Tiannie Aspinall
# Date: March 30, 2026
# Course: ITT103
# Purpose: This program is a Point of Sale system for Best Buy Retail Store.
#          It lets cashiers add items, remove items, view the cart, and checkout.


# this is the product catalog. it stores all the products the store sells
# each product has a name, price, and how many are in stock
products = {
    "Rice (1kg)":        {"price": 350.00,  "stock": 50},
    "Flour (1kg)":       {"price": 280.00,  "stock": 40},
    "Sugar (1kg)":       {"price": 220.00,  "stock": 45},
    "Cooking Oil (1L)":  {"price": 520.00,  "stock": 30},
    "Milk (1L)":         {"price": 380.00,  "stock": 25},
    "Bread (Loaf)":      {"price": 250.00,  "stock": 60},
    "Butter (250g)":     {"price": 310.00,  "stock": 20},
    "Eggs (Dozen)":      {"price": 420.00,  "stock": 35},
    "Chicken (1kg)":     {"price": 850.00,  "stock": 15},
    "Detergent (500ml)": {"price": 430.00,  "stock": 22},
    "Juice (1L)":        {"price": 340.00,  "stock": 18},
    "Pasta (500g)":      {"price": 195.00,  "stock": 50},
}

# the cart is empty at first, items get added when the cashier adds them
cart = {}

# tax is 10 percent
TAX = 0.10

# discount is 5 percent if the bill is over 5000
DISCOUNT = 0.05


# this function just prints a line to make the output look nicer
def print_line():
    print("-" * 50)


# this function shows all the products in the catalog
def show_products():
    print_line()
    print(f"  {'No.':<5} {'Product':<22} {'Price':>9} {'Stock':>7}")
    print_line()

    # i use a counter to number the products
    count = 1
    for name in products:
        price = products[name]["price"]
        stock = products[name]["stock"]

        # check if stock is low and warn the cashier
        if stock < 5:
            stock_display = str(stock) + " (LOW STOCK!)"
        else:
            stock_display = str(stock)

        print(f"  {count:<5} {name:<22} ${price:>8.2f} {stock_display:>7}")
        count = count + 1

    print_line()


# this function shows everything currently in the cart
def show_cart():
    # if the cart is empty just say so
    if len(cart) == 0:
        print("\n  The cart is empty.\n")
        return

    print_line()
    print(f"  {'Product':<22} {'Qty':>5} {'Price':>9} {'Total':>9}")
    print_line()

    for item in cart:
        qty = cart[item]["qty"]
        price = cart[item]["price"]
        total = qty * price
        print(f"  {item:<22} {qty:>5} ${price:>8.2f} ${total:>8.2f}")

    print_line()

    # calculate and show the subtotal at the bottom
    subtotal = get_subtotal()
    print(f"  {'Subtotal':<37} ${subtotal:>8.2f}")
    print_line()


# this function calculates the subtotal of everything in the cart
def get_subtotal():
    subtotal = 0
    for item in cart:
        subtotal = subtotal + (cart[item]["qty"] * cart[item]["price"])
    return subtotal


# this function checks if any product is running low and prints a warning
def check_low_stock():
    low_items = []
    for name in products:
        if products[name]["stock"] < 5:
            low_items.append(name)

    if len(low_items) > 0:
        print("\n  *** LOW STOCK WARNING ***")
        for name in low_items:
            print(f"  - {name} only has {products[name]['stock']} left")
        print()


# this function lets the cashier add an item to the cart
def add_item():
    show_products()

    # put the product names in a list so we can find them by number
    product_names = list(products.keys())

    # ask the cashier to pick a product number
    choice = input("\n  Enter product number to add (or 0 to go back): ").strip()

    # make sure the input is actually a number
    if not choice.isdigit():
        print("  Please enter a valid number.")
        return

    choice = int(choice)

    if choice == 0:
        return

    # check if number is in range
    if choice < 1 or choice > len(product_names):
        print("  That number is not on the list.")
        return

    # get the name of the product they chose
    selected = product_names[choice - 1]
    available = products[selected]["stock"]

    # ask for quantity
    qty_input = input(f"  How many '{selected}' do you want to add? (in stock: {available}): ").strip()

    # validate quantity
    if not qty_input.isdigit() or int(qty_input) <= 0:
        print("  Quantity must be a positive whole number.")
        return

    qty = int(qty_input)

    # make sure there is enough stock
    if qty > available:
        print(f"  Sorry, only {available} unit(s) available.")
        return

    # if the item is already in the cart just update the quantity
    if selected in cart:
        new_total_qty = cart[selected]["qty"] + qty
        # make sure the combined amount doesnt exceed stock
        if new_total_qty > available:
            print(f"  Cannot add {qty} more. You already have {cart[selected]['qty']} in the cart.")
            return
        cart[selected]["qty"] = new_total_qty
    else:
        # add the item to the cart for the first time
        cart[selected] = {"qty": qty, "price": products[selected]["price"]}

    # take the quantity from the stock
    products[selected]["stock"] = products[selected]["stock"] - qty

    print(f"\n  Added {qty} x {selected} to cart.")

    # check if any items are running low after this addition
    check_low_stock()


# this function lets the cashier remove an item from the cart
def remove_item():
    if len(cart) == 0:
        print("\n  The cart is empty, nothing to remove.\n")
        return

    # show the items in the cart with numbers
    cart_list = list(cart.keys())
    print("\n  Items in cart:")
    i = 1
    for item in cart_list:
        print(f"  {i}. {item} (qty: {cart[item]['qty']})")
        i = i + 1

    choice = input("\n  Enter the number of the item to remove (or 0 to go back): ").strip()

    if not choice.isdigit():
        print("  Please enter a valid number.")
        return

    choice = int(choice)

    if choice == 0:
        return

    if choice < 1 or choice > len(cart_list):
        print("  That number is not valid.")
        return

    # get the name of the item they want to remove
    item_to_remove = cart_list[choice - 1]
    qty_to_restore = cart[item_to_remove]["qty"]

    # put the stock back
    products[item_to_remove]["stock"] = products[item_to_remove]["stock"] + qty_to_restore

    # delete the item from the cart
    del cart[item_to_remove]

    print(f"\n  Removed '{item_to_remove}' from the cart.")


# this function handles the checkout process
def checkout():
    if len(cart) == 0:
        print("\n  Cannot checkout, the cart is empty.\n")
        return False

    subtotal = get_subtotal()

    # check if they qualify for the discount
    discount_amount = 0
    if subtotal > 5000:
        discount_amount = subtotal * DISCOUNT
        print(f"\n  Discount of 5% applied!")

    # calculate the price after discount
    after_discount = subtotal - discount_amount

    # calculate the tax
    tax_amount = after_discount * TAX

    # the total is after discount plus tax
    total = after_discount + tax_amount

    # show the summary before asking for payment
    print_line()
    print("  CHECKOUT SUMMARY")
    print_line()
    print(f"  Subtotal:        ${subtotal:.2f}")
    if discount_amount > 0:
        print(f"  Discount (5%):  -${discount_amount:.2f}")
    print(f"  Tax (10%):        ${tax_amount:.2f}")
    print_line()
    print(f"  TOTAL DUE:        ${total:.2f}")
    print_line()

    # ask cashier to enter the amount the customer is paying
    while True:
        payment_input = input("\n  Enter amount received from customer: $").strip()

        # make sure it is a valid number
        try:
            payment = float(payment_input)
        except ValueError:
            print("  Please enter a valid amount.")
            continue

        # customer cant pay less than what they owe
        if payment < total:
            print(f"  Not enough. Total is ${total:.2f}. Please enter a higher amount.")
            continue

        # if we get here the payment is good
        break

    # calculate change
    change = payment - total

    # print the receipt
    print_receipt(subtotal, discount_amount, tax_amount, total, payment, change)

    return True


# this function prints the receipt after checkout
def print_receipt(subtotal, discount_amount, tax_amount, total, payment, change):
    print()
    print("=" * 50)
    print("        BEST BUY RETAIL STORE")
    print("             Receipt")
    print("=" * 50)
    print(f"  {'Item':<22} {'Qty':>4} {'Unit':>8} {'Total':>8}")
    print("-" * 50)

    # print each item the customer bought
    for item in cart:
        qty = cart[item]["qty"]
        price = cart[item]["price"]
        line_total = qty * price
        print(f"  {item:<22} {qty:>4} ${price:>7.2f} ${line_total:>7.2f}")

    print("-" * 50)
    print(f"  {'Subtotal':<35} ${subtotal:>7.2f}")

    if discount_amount > 0:
        print(f"  {'Discount (5%)':<35}-${discount_amount:>7.2f}")

    print(f"  {'Sales Tax (10%)':<35} ${tax_amount:>7.2f}")
    print("-" * 50)
    print(f"  {'TOTAL DUE':<35} ${total:>7.2f}")
    print(f"  {'Amount Paid':<35} ${payment:>7.2f}")
    print(f"  {'Change':<35} ${change:>7.2f}")
    print("=" * 50)
    print("   Thank you for shopping at Best Buy!")
    print("           Please come again :)")
    print("=" * 50)
    print()


# this is the main function that runs the whole program
def main():
    print("=" * 50)
    print("     BEST BUY RETAIL STORE")
    print("       Point of Sale System")
    print("=" * 50)

    # keep running until the cashier exits
    while True:
        # show the menu
        print("\n  MENU")
        print_line()
        print("  1. View Products")
        print("  2. Add Item to Cart")
        print("  3. Remove Item from Cart")
        print("  4. View Cart")
        print("  5. Checkout")
        print("  6. Start New Transaction")
        print("  7. Exit")
        print_line()

        option = input("  Choose an option (1-7): ").strip()

        if option == "1":
            show_products()

        elif option == "2":
            add_item()

        elif option == "3":
            remove_item()

        elif option == "4":
            show_cart()

        elif option == "5":
            # try to checkout
            done = checkout()
            if done:
                # clear the cart after a successful transaction
                cart.clear()
                print("  Transaction complete! Cart has been cleared.\n")

        elif option == "6":
            # start a new transaction
            if len(cart) > 0:
                confirm = input("  Cart is not empty. Start over? (yes/no): ").strip().lower()
                if confirm != "yes":
                    continue
                # restore the stock for items left in cart
                for item in cart:
                    products[item]["stock"] = products[item]["stock"] + cart[item]["qty"]
            cart.clear()
            print("  New transaction started.\n")

        elif option == "7":
            # exit the program
            if len(cart) > 0:
                confirm = input("  Cart still has items. Are you sure you want to exit? (yes/no): ").strip().lower()
                if confirm != "yes":
                    continue
                # restore stock before leaving
                for item in cart:
                    products[item]["stock"] = products[item]["stock"] + cart[item]["qty"]
            print("\n  Goodbye! Have a great day.\n")
            break

        else:
            print("  Invalid option. Please choose a number from 1 to 7.")


# run the program
main()