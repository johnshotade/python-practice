dog = {}

dog['name'] = 'aruno'
dog['breed'] = 'astasian'
dog['legs'] = '4'
dog['age'] = '7'

print(dog)

student = {
    'first_name': 'mike',
    'last_name': 'maslow',
    'gender':'male',
    'marital_status':'single',
    'skills':['python','javascript','typescript'],
    'country':'england',
    'city':'london',
    'address': '83 maple place, e121 2y'

}
print(student)

stud_len = len(student)
print(stud_len)

stud_skill = student['skills']
print(type(stud_skill))
print(stud_skill)

student['skills'].append(['database','sql'])
print(student)

dog_keys = dog.keys()
print(dog_keys)
stud_keys = student.keys()
print(stud_keys)


dog_values = dog.values()
print(dog_values)
stud_values = student.values()
print(stud_values)


dog_tup = dog.items()
print(dog_tup)

stud_tup = student.items()
print(stud_tup)

del dog['legs']
del student['marital_status']

del dog

print (dog)


