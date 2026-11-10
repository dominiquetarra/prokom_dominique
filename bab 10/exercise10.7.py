while True :
    print("\nEnter 'quit' to exit the program" )
    first_number = input("First number : ")
    if first_number.lower () == 'quit' :
        break
    second_number = input("Second number : ")
    if second_number.lower() == 'quit' :
        break

    try :
        result = int(first_number) + int(second_number)
    except ValueError :
        print("Please enter numerical number, not text")
    else :
        print(f"The sum is : {result}")