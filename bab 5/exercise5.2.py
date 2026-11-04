car = 'Audi'
print("Is car == 'Audi'? I predict True")
print(car =='Audi')
print("Is car != 'Audi'? I predict False")
print(car != 'Audi')

#Lower method
print("Is car.lower() == 'audi'? I predict True")
print(car.lower () == 'audi')
print("Is car.lower() == 'Audi'? I predict False")
print(car.lower () == 'Audi')

#Numerical test
age = 21
print("Is age == 21? I predict True")
print(age == 21)
print("Is age != 21? I predict False")
print(age != 21)
print("Is age > 18? I predict True")
print(age > 18)
print("Is age < 18? I predict False")
print(age < 18)
print("Is age >= 21? I predict True")
print(age >= 21)
print("Is age <= 18? I predict False")
print(age <= 18)

#Test using the and keyword and the or keyword
age_0 = 15
age_1 = 20
print("Is age_0 >= 15 and age_1 <=25? I predict True")
print(age_0 >= 15 and age_1 <= 25)
print("Is age_0 >15 and age_1 <= 25? I predict False")
print(age_0 > 15 and age_1 <= 25)
print("Is age > 20 or age_1 <= 25? I predict True")
print(age_0 > 20 or age_1 <= 25)
print("Is age > 20 or age_1 < 18? I predict False")
print(age_0 > 20 or age_1 < 18)

#Test item is in a list
fruits = ['apple' , 'banana']
print("Is 'apple' in fruits? I predict True")
print('apple' in fruits)
print("Is 'grape' in fruits? I predict False")
print('grape' in fruits)

#Test item is not in a list
foods = ['rice' , 'noodle']
print("Is 'soup' not in food? I predict True")
print('soup' not in foods)
print("Is 'rice' not in food? I predict False")
print('rice' not in foods)