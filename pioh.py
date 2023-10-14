# Variables

variable_1 = 21
variable_2 = "John"
variable_3 = True
variable_4 = 140.2

age = 19
name = "Joe"
is_human = True
weight = 174.5

x = 10
y = 4
z = x + y  # {+, -, *, /, //, %, **}

# Input output

user_input = input("Please enter something: ")
print(user_input)

# Conditionals

conditional = 5 > 4 or 10 < 9
other_conditional = 5 > 4 and 10 < 9

boss_is_beaten = True
score = 10

player_wins = boss_is_beaten and score > 100

if player_wins:
    print("Yay you have won!")
else:
    print("Aw you lost.")

grade = 87

if grade <= 90:
    print("You got an A")
elif grade <= 80:
    print("You got a B")
elif grade <= 70:
    print("You got a C")
else:
    print("You failed")

# Loops

counter = 0

while counter < 10:
    print(counter)
    counter = counter + 1

for number in range(0, 10, 1):
    print(number)

alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    print(letter)

# Lists

shopping_list = ["eggs", "milk", "bread", "chips", "blanket"]
        # index    0       1        2        3         4
first_item = shopping_list[0]
sublist = shopping_list[0:3]

shopping_list.append("chicken")
shopping_list.insert(0, "notebook")

# Functions

def add(x, y):
    return x + y

def calculate_rectangle_area(l, w):
    return l * w

result = add(1, 3)
area = calculate_rectangle_area(10, 5)


def bark():
    print("WOOF WOOF WOOF")

def print_n_numbers(n):
    for number in range(n):
        print(number)

# OOP and Classes

class Car:
    def __init__(self, make, model, year, is_manual, gas):
        self.make = make
        self.model = model
        self.year = year
        self.is_manual = is_manual
        self.gas = gas

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print("VROOM VROOM")
        else:
            print("you are out of gas.")

    def refill_gas(self, gallons):
        self.gas += gallons

    def print_info(self):
        print(self.make, self.model, self.year)

my_car = Car("Toyta", "Camry", 2020, True, 15)
my_car.drive()

# File IO and Modules

file_object = open("fileName.txt", "r+")
file_data = file_object.readline()
file_object.close()

import math
print(math.pi)

with open("fileName.txt") as my_file:
    print(my_file.read())

