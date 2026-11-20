"""
Program: Learner Marks Management System

Learner Name: Funeka Sobopha
Date: 18 November 2026

Student Number: do not have

This program shows how to use Python lists and other collections,
create and use functions, search for and sort information, and
manage learner records using an interactive menu within the management system

"""

#Starter data -use this given data to answer several questions of the assignment

learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]},
    "2024003": {"name": "Lerato", "marks": [81, 39, 77]},
    "2024004": {"name": "Dumisani", "marks": [72, 72, 48]},
    "2024005": {"name": "Naledi", "marks": [90, 55, 72]}
}

print("1.1")

marks = learners["2024001"]["marks"]

print("The marks are:", marks)
print("First mark is:", marks[0])
print("Last mark is:", marks[-1])
print("First two marks are:", marks[:2])
print("")


print("1.2")

# A tuple is appropriate because the classroom coordinate (row, seat)
# is a fixed collection of values that should not be changed.

classroom_coordinate= (5,6)

# Unpacking the tuple
row,seat = classroom_coordinate

# Displaying the values
print("Classroom cordinates:" , row,",",seat)
print("Classroom Row:", row)
print("Seat Number:", seat)
print("")

print("1.3")

# Set of module codes with a duplicates that offered 
modules = {"WSK101", "RKW101", "AWS101","RKW101" ,"WTS101" ,"WSK101"}

# Display all unique module codes
print("Module codes:", modules)

# Display the number of unique codes created
print("\nNumber of unique codes:", len(modules))

# Test membership
#  Test if WSK101 exists - return True
print("\nIs WSK101 a module offered?", "WSK101" in modules)
# Test if BOR101 exists - return False
print("\nIs BOR101 a module offered?", "BOR101" in modules)

"""
1.4
 Dictionary keyed by student number:
- Student numbers are unique identifiers(keys), which prevents duplicate entries.
- It allows instant search to find or update a student's data without going  through the entire dataset.

List of marks inside each record:
- A student can have multiple test marks, and a list allows storing multiple values under one student.
- It preserves the chronological order of the marks and makes it easy to append new grades or calculate averages.

"""

#2.1
#write function total of
def total_of(values):
    total = 0
    for v in values:
        total = total + v
    return total

#2.2
#write function mean of, calling previous function of
def mean_of(values):
    if len(values) == 0:
        return 0
    return total_of(values) / len(values)

# 2.3
# Write a function max_of(values) and min_of(values)

def max_of(values):
    if len(values) == 0:
        return None

    best = values[0]

    for val in values:
        if val > best:
            best= val
    return best

def min_of(values):
    if len(values) == 0:
        return None

    smallest = values[0]

    for val in values:
        if val < smallest:
            smallesy = val
    return smallest

#2.4
# functions range_of(values) and above_mean(values)

#uses the above function(max of() and mean of()) to calculate the range
def range_of(values):
    if len(values) == 0:
        return 0
    return max_of(values) - min_of(values)

def above_mean(values):
# Handle an empty list
    if len(values) == 0:
        return []

    average = mean_of(values)
    result = []

    for value in values:
        if value > average:
            result.append(value)

    return result

print("\n2.4")

# Test data - used the sample data given as an example at the end of the assignment document
marks = [65, 72, 48, 90, 55, 72, 48, 72]
print(marks)
print("Total:", total_of(marks))
print("Mean: - average of the marks", mean_of(marks))
print("Maximum:", max_of(marks))
print("Minimum:", min_of(marks))
print("Range - Maximun - Minimum:", range_of(marks))
print("Above Mean - marks that above the mean:", above_mean(marks))

# 3.1
# function find_first(values, target)

def find_first(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1
# 3.2
# function find_all(values, target)

def find_all(values, target):
    positions = []

    for index in range(len(values)):
        if values[index] == target:
            positions.append(index)
    return positions

# 3.3
# function count_of(values, target)

def count_of(values, target):
    count = 0

    for value in values:
        if value == target:
            count = count + 1
    return count

# 3.4
# function mode_of(values)
def mode_of(values):

    if len(values) == 0:
        return []

    frequency = {}

    for value in values:
        if value in frequency:
            frequency[value] = frequency[value] + 1
        else:
            frequency[value] = 1

    best = 0
    for value in frequency:
        if frequency[value]> best:
            best = frequency[value]

    modes = []
    
    for value in frequency:
        if frequency[value] == best:
            modes.append(value)
    return modes

print("\n3.4  data showing a modes tie")
# Test data showing a tie
numbers = [5, 12, 9, 5,8, 9, 14, 3, 4, 21]
print("List is ", numbers)
print("Modes:", mode_of(numbers))
print("")

# ====================================================================================================================
# Question 4.1
# Bubble sort(values)

def bubble_sort(values):
    items = values[:]   # make a copy - do not lose original content

    n = len(items)
    for i in range(n-1):
        swapped = False
        for j in range (n-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
                break
    return items

#4.2
# function Selection sort(values)

def selection_sort(values):
    sorted_list = values[:]   # make a copy

    n = len(sorted_list)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j

        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
    return sorted_list
    

#4.3
# Testing bubble and selection sorts
print("4.3")
test_data = [65, 72, 48, 90, 55, 72, 48, 72]

print("Original Test Data:		", test_data)

print("Test Data afteer Bubble Sort:	", bubble_sort(test_data))

print("Test Data after Selection Sort:	", selection_sort(test_data))

print("The Original Data:		", test_data)

# 5.1
def menu():
    while True:

        print("\n===== LEARNER MANAGEMENT SYSTEM =====")
        print("1. Add Learner")
        print("2. Search Learner")
        print("3. Update Learner")
        print("4. Delete Learner")
        print("5. Display Ranking")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_learner()

        elif choice == "2":
            search_learner()

        elif choice == "3":
            update_learner()

        elif choice == "4":
            delete_learner()

        elif choice == "5":
            display_ranking()

        elif choice == "6":
            print("Program Ended.")
            break

        else:
            print("Invalid choice. Please try again.")

#Question 5.2 Add function

def add_learner():
    student_number = input("Student Number: ")

    if student_number in learners:
        print("Student number already exists.")
        return

    name = input("Learner Name: ")

    marks_input = input("Enter marks separated by spaces: ")

    marks = []

    for mark in marks_input.split():
        mark = int(mark)

        if 0 <= mark <= 100:
            marks.append(mark)

    learners[student_number] = {
        "name": name,
        "marks": marks
    }

    print("Learner added successfully.")
    
# 5.3 lookup function
def search_learner():
    student_number = input("Enter student number: ")

    if student_number in learners:
        print("Name:", learners[student_number]["name"])
        print("Marks:", learners[student_number]["marks"])
    else:
        print("Learner not found.")
# 5.4 Update & Delete

def update_learner():
    student_number = input("Student Number: ")

    if student_number not in learners:
        print("Learner not found.")
        return

    print("1. Update Name")
    print("2. Add Mark")

    choice = input("Choice: ")

    if choice == "1":
        new_name = input("New Name: ")
        learners[student_number]["name"] = new_name
        print("Name updated.")

    elif choice == "2":
        mark = int(input("New Mark: "))

        if 0 <= mark <= 100:
            learners[student_number]["marks"].append(mark)
            print("Mark added.")
        else:
            print("Invalid mark.")

def delete_learner():
    student_number = input("Student Number: ")

    if student_number in learners:
        confirm = input("Delete learner? (Y/N): ")

        if confirm.upper() == "Y":
            del learners[student_number]
            print("Learner deleted.")
    else:
        print("Learner not found.")
        
def display_ranking():
    ranking = []

    for student_number, details in learners.items():
        average = mean_of(details["marks"])
        ranking.append((average, student_number))

    ranking = bubble_sort(ranking)

    print("\nLEARNER RANKING")

    for average, student_number in ranking:
        print(
            student_number,
            learners[student_number]["name"],
            round(average, 2)
        )
#Start the menu
menu()
