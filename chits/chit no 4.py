"""
a) Write a Python program to store roll numbers of student in array who attended training program in random order. Write function for searching whether particular student attended training program or not, using Linear search and Sentinel search.
b) Write a Python program to store roll numbers of student array who attended training program in sorted order. Write function for searching whether particular student attended training program or not, using Binary search and Fibonacci search

"""
def addAttendee(sorted_list):
    roll = int(input("\nEnter roll of attendee: "))
    sorted_list.append(roll)
    sorted_list.sort()  

def display(sorted_list):
    print("Sorted list of attendees:", sorted_list)

def binarySearch(sorted_list, roll):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == roll:
            print("Student with roll number", roll, "attended the program at index", mid)
            return
        elif sorted_list[mid] < roll:
            low = mid + 1
        else:
            high = mid - 1
    print("Student with roll number", roll, "did not attend the program")

def fibonacciSearch(sorted_list, roll):
    def min_fibonacci(m):
        fib1, fib2 = 0, 1
        while fib2 < m:
            fib1, fib2 = fib2, fib1 + fib2
        return fib1

    offset = -1
    length = len(sorted_list)
    while min_fibonacci(length) > 1:
        index = min(offset + min_fibonacci(length - 1), length - 1)
        if sorted_list[index] < roll:
            length = length - (index - offset)
            offset = index
        elif sorted_list[index] > roll:
            length = index
        else:
            print("Student with roll number", roll, "attended the program at index", index)
            return
    if (offset + 1) < length and sorted_list[offset + 1] == roll:
        print("Student with roll number", roll, "attended the program at index", offset + 1)
    else:
        print("Student with roll number", roll, "did not attend the program")

def menu():
    print("*" * 40)
    print("1. Add attendee\n2. Display\n3. Binary Search\n4. Fibonacci Search\n5. Exit")

# Main Program
sorted_attendees = []

while True:
    menu()
    choice = int(input("Enter choice: "))

    if choice == 1:
        addAttendee(sorted_attendees)
    elif choice == 2:
        display(sorted_attendees)
    elif choice == 3:
        roll_num = int(input("Enter roll number to search: "))
        binarySearch(sorted_attendees, roll_num)
    elif choice == 4:
        roll_num = int(input("Enter roll number to search: "))
        fibonacciSearch(sorted_attendees, roll_num)
    elif choice == 5:
        exit()
    else:
        print("Invalid choice! Please enter a valid option.")
