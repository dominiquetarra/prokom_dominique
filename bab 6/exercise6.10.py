favorite_numbers = {
    'domi' : [7, 88] , 
    'sarah' : [5, 16] ,
    'eric' : [8] ,
    'tomi' : [24, 3] ,
    'fara' : [99, 77]
}

for name , numbers in favorite_numbers.items() :
    print(f"\n{name.title()}'s favorite numbers are :")
    for number in numbers :
        print(f"{number}")