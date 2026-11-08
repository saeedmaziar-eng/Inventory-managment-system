products = {}

def add_product():
    name = input("Enter product name: ")
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a number")
        return
    if quantity <= 0:
        print("Invalid quantity")
        return
    if name in products:
        print("Product already exists")
        products[name] += quantity
        print("SuccessFull")
    else:
        products[name] = quantity
        print("Product added")

def show_products():
    if not products:
        print("Inventory is empty")
        return
    else:
        for name, quantity in products.items():
            print(f"{name} --> {quantity}")

def sell_product():
    name = input("Enter product name: ")
    if name not in products:
        print("product not found")
        return
    else:
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a number")
            return
        if quantity <= 0:
            print("Invalid quantity")
        elif quantity > products[name]:
            print("Invalid quantity")
        else:
            products[name] -= quantity
            print("SuccessFull")



def search_product():
    name = input("Enter product name: ")
    if name not in products:
        print("product not found")
        return
    else:
            print(f"{name} --> {products[name]}")


def low_stock():
    found = False
    for name, quantity in products.items():
        if quantity < 5:
            print(f"{name} --> {quantity}")
            found = True
    if not found:
        print("No low stock products")

def main():
    while True:
        print("=== Inventory management system ===")
        print("1. Add product")
        print("2. Show products")
        print("3. Sell product")
        print("4. Search product")
        print("5. Low stock")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number")
            continue

        if choice == 1:
            add_product()

        elif choice == 2:
            show_products()

        elif choice == 3:
            sell_product()

        elif choice == 4:
            search_product()

        elif choice == 5:
            low_stock()

        elif choice == 6:
            print("Exit")
            break

        else:
            print("Invalid choice")

main()