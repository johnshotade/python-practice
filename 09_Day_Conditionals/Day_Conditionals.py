# age = int(input("Enter your age: "))



# if age >= 18:
#     print("You are old enough to learn to drive.")
# else:

#     diff = 18 - age
#     print("You need" + " " + str(diff) + " " + "more years to learn to drive.")

# my_age = int(input("Enter my age: "))

# your_age = int(input("Enter your age: "))

# age_diff = your_age - my_age

# if age_diff == 1:
#     print("You are" + " " + str(age_diff) + " " + "year older than me.")
# elif age_diff > 1:
#     print("You are" + " " + str(age_diff) + " " + "years older than me.")
# else:
#     print("invalid input")


# one = int(input("Enter number one: "))
# two = int(input("Enter number two: "))

# if one > two:
#     print(str(one) + " is greater than " + str(two))
# elif one < two:
#     print(str(one) + " is smaller than " + str(two))
# else:
#     print(str(one) + " is equal to " + str(two))




# score = int(input("Enter your score: "))

# if score >= 90 and score <= 100 :
#     print("A")
# elif score >= 80 and score <= 89 :
#     print("B")
# elif score >= 70 and score <= 79 :
#     print("C")
# elif score >= 60 and score <= 69 :
#     print("D")
# elif score >= 0 and score <= 59 :
#     print("F")
# else:
#     print("Invalid score")



# month = input("Enter month: ").capitalize()


# if month == "September" or month == "October" or month == "November":
#     print("Autumn")
# elif month == "December" or month == "January" or month == "February":
#     print("Winter")
# elif month == "March" or month == "April" or month == "May":
#     print("Spring")
# else:
#     print("Summer")



# fruits = ['banana', 'orange', 'mango', 'lemon']


# fruit = input("Enter Fruit: ")


# if fruit not in fruits:
#     fruits.append(fruit)
#     print(fruits)
# else:
#     print('That fruit already exist in the list')


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

keys = person.keys()

print(keys)

if 'skills' in keys:
    print(person['skills'][2])
    if 'Python' in person['skills']:
        print(person['skills'])
        if person['skills'] == 'JavaScript' and person['skills'] == 'React':
            print('He is a front end developer')
        elif person['skills'] == 'Node' and person['skills'] == 'Python' and person['skills'] == 'MongoDB':
            print('He is a backend developer')
        elif person['skills'] == 'React' and person['skills'] == 'Node' and person['skills'] == 'MongoDB':
            print('He is a fullstack developer')
        else:
            print('unknown title')
    else:
        print('no')
    
else:
    print('invalid')

if person['is_married'] == True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')
else:
    print(False)









