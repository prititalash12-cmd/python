# Menu Choice Program

print("Choose a drink from the menu:")
print("1. Tea")
print("2. Coffee")
print("3. Juice")
print("4. Water")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("You chose Tea.")
elif choice == 2:
    print("You chose Coffee.")
elif choice == 3:
    print("You chose Juice.")
elif choice == 4:
    print("You chose Water.")
else:
    print("Invalid choice!")
