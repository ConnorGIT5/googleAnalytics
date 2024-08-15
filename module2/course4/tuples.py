def to_dollars_cents(price):

    # split price (float) into dollars and cents
    
    dollars = int(price // 1)
    cents = round(price % 1 * 100)
    
    return dollars, cents

dollars, cents = to_dollars_cents(6.55)

print("Dollars: " + str(dollars))
print("Cents: " + str(cents))

team = [
    ("Lebron James", 39, "Point Guard"),
    ("Anthony Davis", 35, "Center"),
    ("Stephan Curry", 34, "Shooting Guard"),
    ("Kevin Durant", 38, "Power Forward"),
    ("Joel Embiied", 41, "Small Forward")
]

for name, age, position in team:
    print("Name: " + name + "\n" + "Age: " + str(age) + "\n" + "Position: " + position + "\n\n")

my_string = str()
my_string += "Hello!"
print(my_string)

def player_position(players):
    result = []
