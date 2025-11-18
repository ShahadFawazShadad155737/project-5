while True:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    choice = input("choose [*, -, +, /]: ")

    
    if choice == '*':
        print('multiplying =', num1 * num2)

    elif choice == '-':
        print('minus =', num1 - num2)

    elif choice == '+':
        print('plus =', num1 + num2)

    elif choice == '/':
        print('divide =', num1 / num2)

    else:
        print("you have chosen something I don't know")

    
    if num1 > num2: 
        print(num1, "is greater than", num2)

    elif num1 < num2: 
        print(num1, "is smaller than", num2)

    else:
        print(num1, "is equal to", num2)

    
   