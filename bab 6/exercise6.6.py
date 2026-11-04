favorite_languages = {
    'jen' : 'python' , 
    'sarah' : 'c' , 
    'edward"' : 'rust' ,
    'phil' : 'python'
}

name_poll = ["jen" , "sarah" , "edward" , "phil" , "dominique" , "fara" , "michelle"]

for person in name_poll :
    if person in favorite_languages :
        print(f"Thank you, {person.title()}, for taking the poll")
    else :
        print(f"Hi {person.title()}, please take our poll")