# lists - veranderbaar
lade = ['pen', 'potlood', 'gum', 'papier']
lade.append("fineliner")
lade.sort()

#tuples - niet veranderbaar
temperaturen = (24.5, 18.4, 19.2, 21.5)
print(temperaturen[1])

#sets - geen dubbele waardes (niet sorteren)
numbers = {1, 2, 3, 4, 5, 6, 7, 8}
print(numbers)
numbers.add(9)

#dictionaries - key-value pairs
user= {
    "name": "Bimal",
    "age": 22,
    "password" :"123456789"

}
print(user)
print(user.keys())
print(user.values())
print (user ['password']())

user['hobbies'] = "programmeren"



