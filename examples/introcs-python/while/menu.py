def show_menu() -> None:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Quit")


if __name__ == '__main__':
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            a = float(input("a: "))
            b = float(input("b: "))
            print(f"Result: {a + b}")
        elif choice == "2":
            a = float(input("a: "))
            b = float(input("b: "))
            print(f"Result: {a - b}")
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")
