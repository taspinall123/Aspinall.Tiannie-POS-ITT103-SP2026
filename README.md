# Aspinall.Tiannie-POS-ITT103-SP2026
Point of Sale System
Authors: Tiannie Aspinall
Date Created: March 30, 2026
Course: ITT103
GitHub Public URL to Code: https://github.com/taspinall123/Aspinall.Tiannie-POS-ITT103-SP2026

--------------------------------------------------
Program Description
--------------------------------------------------

This program is a Point of Sale (POS) system for a store called Best Buy Retail Store.
The store sells everyday items like groceries and household products. The program
was made to help cashiers process sales faster and reduce manual errors.

The cashier can use the menu to add items to a cart, remove them, see what is in
the cart, and then checkout when the customer is ready to pay. After payment the
program prints a receipt.

--------------------------------------------------
How to Run the Program
--------------------------------------------------

1. Make sure Python 3 is installed on your computer.
2. Save the file called POS-ITT103-SP2026.py somewhere on your computer.
3. Open a terminal or command prompt.
4. Type: python POS-ITT103-SP2026.py and press Enter.
5. The menu will appear, and you can start using the system.

Note: You do not need to install anything extra. The program only uses built-in Python features.

--------------------------------------------------
How the Program Works
--------------------------------------------------

When you run the program, a menu shows up with 7 options:

1. View Products - shows the full list of products, their prices and stock
2. Add Item to Cart - lets you pick a product and quantity to add
3. Remove Item from Cart - lets you take an item out of the cart
4. View Cart - shows everything in the cart with a subtotal
5. Checkout - calculates the total, takes payment and prints a receipt
6. Start New Transaction - clears the cart to start fresh
7. Exit - closes the program

--------------------------------------------------
Features
--------------------------------------------------

- The catalog has 12 products. Each one has a name, price, and stock amount.

- When you add an item, it checks if there is enough stock. If not, it tells you.

- If a product has less than 5 units left a low stock warning is printed.

- At checkout the program adds 10% sales tax to the total.

- If the subtotal is over $5000 a 5% discount is applied before the tax.

- The cashier enters how much the customer paid and the program calculates
  the change. It will not accept a payment that is less than the total.

- A receipt is printed at the end showing all the items, the subtotal,
  any discount, the tax, the total, the amount paid, and the change.

- The program keeps running after a transaction so multiple customer
  can be served in one session.

- If you try to exit or start over with items still in the cart it will
  ask you to confirm first.

--------------------------------------------------
Assumptions and Limitations
--------------------------------------------------

- The prices are in Jamaican dollars (JMD).
- The product list is fixed. You cannot add new products while the program is running.
- The stock resets every time you restart the program because it is not saved to a file.
- The receipt only prints on screen; it does not save to a file or send to a printer.
- The discount only applies if the subtotal (before tax) is above $5000.

