# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


companies_length = len(it_companies)
print(companies_length)

it_companies.add('Twitter')
print(it_companies)

it_companies.update({'Instagram', 'Whatsapp', 'TikTok'})
print(it_companies)

it_companies.pop()
print(it_companies)

joint_a_b = A.union(B)
print(joint_a_b)
intersect_a_b = A.intersection(B)
print(intersect_a_b)

disjoint_a_b = A.isdisjoint(B)
print(disjoint_a_b)

join = A.union(B) and B.union(A)
print(join)


symmetric_difference = A.symmetric_difference(B)
print(symmetric_difference)

del A
del B

age_set = set(age)
print(age_set)


length_list = len(age)
print(length_list)
length_set = len(age_set)
print(length_set)


A = {'i','am','a','teacher','and'}
B = {'i','love','to','inspire'}
C = {'and','teach','people'}

intersect = A.intersection(B)

print(intersect)