import sys

animals = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat']

script, year = sys.argv

def print_zodiac(year): 
    print(animals[int(year)%12])

print_zodiac(year)