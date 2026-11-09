import random

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A' , 'B' , 'C' , 'D' ,'E']
winner = random.sample(lottery , 4)

print(f"The winning lottery is : {winner}")
print("Any ticket maching these 4 numbers or letters wins a prize!")