"""Problem 59: Phone directory (add / search / delete / list)."""
def main():
    directory = {}
    while True:
        print("\n1. Add  2. Search  3. Delete  4. List  5. Exit")
        ch = input("Choice: ")
        if   ch == '1': directory[input("Name: ")] = input("Phone: ")
        elif ch == '2':
            name = input("Search: ")
            print(directory.get(name, "Not found"))
        elif ch == '3': directory.pop(input("Delete: "), None)
        elif ch == '4':
            for k, v in directory.items():
                print(f"{k}: {v}")
        elif ch == '5': break

if __name__ == "__main__":
    main()
