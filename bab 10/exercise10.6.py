first_number = input("First number : ")
second_number = input("Second number : ")

try :
    result = int(first_number) + int(second_number)
except ValueError :
    print("Please enter numerical number, not text")
else :
    print(f"The sum is : {result}")