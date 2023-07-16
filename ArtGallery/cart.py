cart = []

def add_item():
    item = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    cart.append({'item': item, 'price': price, 'quantity': quantity})
    print("Item added to the cart!")

def remove_item():
    item_index = int(input("Enter the index of the item to remove: "))
    if 0 <= item_index < len(cart):
        removed_item = cart.pop(item_index)
        print(f"Removed item: {removed_item['item']}")
    else:
        print("Invalid index!")

def display_cart():
    if len(cart) == 0:
        print("Your cart is empty.")
    else:
        print("Cart contents:")
        for index, item in enumerate(cart):
            print(f"Index: {index}\tItem: {item['item']}\tPrice: {item['price']}\tQuantity: {item['quantity']}")

def calculate_total():
    total = sum(item['price'] * item['quantity'] for item in cart)
    print(f"Total price: {total}")

def main():
    while True:
        print("\n--- Shopping Cart ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Cart")
        print("4. Calculate Total")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            display_cart()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

main()













# cart = {}
# print("*****Welcome to the Shopping Cart Program!*****")
#
# while True:
#     print()
#     print("Please type in one of these")
#     print("1. Add item ")
#     print("2. View cart ")
#     print("3. Remove Item ")
#     print("4. compute total")
#     print("5. exit program")
#
#     select = int(input(" Type in a number to go on : "))
#
#     if select == 1:
#         item = input(" What would you like to add?:  ")
#         price = float(input(" type in the price: "))
#         cart[item] = price
#         print(f"'{item}' has been added to your cart.")
#         print(f" The price is ${price}")
#
#     if select == 2:
#         print("This is what is in your shopping cart:")
#         for item in cart:
#             print(f"  {item} - ${cart[item]}")
#
#     if select == 3:
#         takeout = input(" Type in what you would like to remove?:  ")
#         cart.pop(takeout)
#
#     if select == 4:
#         total = 0
#         for item in cart:
#             total += cart[item]
#         print(f" ${total}")
#
#     if select == 5:
#         print("comeback soon!")
#         break