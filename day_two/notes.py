# list comprehension
even_numbers = [num for num in range(1,101) if num % 2 == 0]


# dictionary comprehension
cities = ["mumbai", "new york", "paris", "tokyo"]
countries = ["india", "usa", "france", "japan"]

city_country_dict = {city: country for city, country in zip(cities, countries)}

# decorators
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles on top! 🍬")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge sauce! 🍫")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here's your {flavor} ice cream! 🍨")


# context managers
class HandleFile:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        
with HandleFile('example.txt', 'w') as file:
    file.write("Hello, this is a test file created using a context manager!")

# print(file.closed)


# iterators
name = "Fedrick"

name_iterator = iter(name)

# print(next(name_iterator))  # F


# generators

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)


