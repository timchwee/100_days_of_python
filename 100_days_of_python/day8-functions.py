def greet():
    print("hello")
    print("how are you")
    print("have you eaten?")

greet()

# Fuctions that allow for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Hod do you do {name}")

greet_with_name("Tim")

# Functions with more thatn 1 input

def greet_with(name, country):
    print(f"Hellow {name}")
    print(f"Are you from {country}")

greet_with("Tim", "Australia")

greet_with(country="Australiaaaaaa", name="Timo")