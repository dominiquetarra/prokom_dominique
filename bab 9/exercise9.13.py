from random import randint

class Die :
    def __init__(self, sides=6) :
        self.sides = sides
    def roll_die (self) :
        return randint(1, self.sides)

#6 sides die and 10 times rolled
six_sided = Die()
results = []
for roll_number in range(10) :
    result = six_sided.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die : ")
print(results)

#10 sides die and 10 times rolled
ten_sided = Die(sides=10)
results = []
for roll_number in range (10) :
    result = ten_sided.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die : ")
print(results)

#20 sided die and 10 times rolled
twenty_sided = Die(sides=20)
results = []
for roll_number in range(10) :
    result = twenty_sided.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die : ")
print(results)