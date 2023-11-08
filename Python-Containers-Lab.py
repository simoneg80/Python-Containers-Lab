# Exercise 1
# your solution here:

students = [
    "Simone", "Jose", "Kiaya"
]    
print(students[1])
print(students[-1])


# Exercise 2
# your solution here:

foods = ("chinese", "italian", "jamaican" )
for food in foods:
    print(f"{food} is a good food")

# Exercise 3
# your solution here:
for food in foods:
    last_foods = foods[-2:]
print(last_foods) 

# Exercise 4
# your solution here:
home_town = {
    "city": "Bronx",
    "state": "NY",
    "population": 1427000

}
print(f"I was born in {home_town['city']}, {home_town['state']}- population of {home_town['population']}")

# Exercise 5
# your solution here:

for key, val in home_town.items():
    print(f"{key} = {val}")
# Exercise 6
# your solution here:

cohort = []
for i, student in enumerate(students):
    cohort.append({"student": student, "fav_foods": foods[i]})
for item in cohort:
    print(item)


# Exercise 7
# your solution here:
 
awesome_students = [f"{student} is awesome!" for student in students]
for string in awesome_students:  
    print(string)

# Exercise 8
# your solution here:

    # solution 1 

a_foods = [food for food in foods if "a" in food]
for string in a_foods: 
    print(string)

    # solution 2 

# for food in foods:
#     if "a" in food:
#         print(food)