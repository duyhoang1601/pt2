import csv
import os

# Function to add a new employee to the file
def add_employee(code, name, salary, allowance):
    with open('input.txt', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([code, name, salary, allowance])

# Function to perform binary search on employee data based on name
def search_employee(name):
    with open('input.txt', 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        data.sort(key=lambda x: x[1])  # Sorting data by name
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid][1] == name:
                return data[mid]
            elif data[mid][1] < name:
                left = mid + 1
            else:
                right = mid - 1
        return None

# Function to remove an employee based on code
def remove_employee(code):
    with open('input.txt', 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
    with open('input.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            if row[0] != code:
                writer.writerow(row)

# Function to print the list in descending order based on salary + allowance
def print_sorted_list():
    with open('input.txt', 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        data.sort(key=lambda x: int(x[2]) + int(x[3]), reverse=True)
    with open('result.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

def main():
    while True:
        print("\nOptions:")
        print("1. Add a new employee")
        print("2. Find data about an employee using name (Binary Search)")
        print("3. Remove an employee based on code")
        print("4. Print the list in descending order based on salary + allowance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            code = input("Enter employee code: ")
            name = input("Enter employee name: ")
            salary = input("Enter employee salary: ")
            allowance = input("Enter employee allowance: ")
            add_employee(code, name, salary, allowance)
            print("Employee added successfully.")
        elif choice == '2':
            name = input("Enter employee name to search: ")
            result = search_employee(name)
            if result:
                print("Employee found:", result)
            else:
                print("Employee not found.")
        elif choice == '3':
            code = input("Enter employee code to remove: ")
            remove_employee(code)
            print("Employee removed successfully.")
        elif choice == '4':
            print_sorted_list()
            print("List printed and saved to result.txt")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

