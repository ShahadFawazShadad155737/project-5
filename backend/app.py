products = [
    ["Ceremonial Grade Matcha", 170],
    ["Premium Grade Matcha", 150],
    ["Latte Grade Matcha", 130],
    ["Culinary Grade Matcha", 120],
    ["Ingredient Grade Matcha", 100]
]

while True:
    print("\nProduct List:")
    for i in range(len(products)):
        print(f"{i+1} - {products[i][0]} : {products[i][1]} SAR")

    choice = input("Enter product number: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(products):
            price = products[choice - 1][1]
            total_price = price * 1.15
            print(f"Price with VAT: {total_price} SAR")
        else:
            print("Error: Product number not found")
    else:
        print("Error: Please enter a valid number")

    again = input("Do you want to buy another product? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for shopping!")
        break