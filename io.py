#open text file 
file = open ('test.txt', 'r')

#Print text file
print(file.read())

#Write text file
#file.write ('Hello, World Again!')

#Close text file
#file.close()

with open ('test.txt', 'r') as file:
    print(file.read())


