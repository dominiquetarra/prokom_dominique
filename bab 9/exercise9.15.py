import random
def draw_ticket(pool) :
    return random.sample(pool, 4 )

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A' , 'B' , 'C' , 'D' ,'E']
my_ticket = [3, 'C' , 7 , 'D']

attempts = 0
won = False

while not won :
    attempts += 1
    drawn =  draw_ticket(lottery)
    if set(drawn) == set (my_ticket) :
        won = True

print(f"Your ticket : {my_ticket}")
print(f"It tooks {attempts} times to get a winning ticket")