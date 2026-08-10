#List
'''Inside the editor, complete the following steps:
Create a list called colors with the values "red", "green", "blue"
Print the first item in the list
Change the second item to "yellow"
Add "purple" to the end of the list using append()
Remove "red" from the list using remove()
Print the list'''
# Create a list
colors=["red", "green", "blue"]

# Print the first item
print(colors[0])

# Change the second item to "yellow"
colors[1]='yellow'

# Add "purple" to the end
colors.append('purple')

# Remove "red"
colors.remove('red')

# Print the list
print(colors)
########
#Tuple
'''Inside the editor, complete the following steps:
Create a tuple called fruits with the values "apple", "banana", "cherry"
Print the second item in the tuple
Print the number of items using len()
Unpack the tuple into three variables a, b, c
Print the variable b'''
# Create the tuple
fruits=("apple", "banana", "cherry")
# Print the second item
print(fruits[1])

# Print the number of items
print(len(fruits))

# Unpack the tuple
a,b,c=fruits

# Print b
print(b)


#####
#set
'''Inside the editor, complete the following steps:
Create a set called colors with the values "red", "green", "blue"
Print the set
Add "yellow" to the set using add()
Remove "green" from the set using discard()
Print the number of items using len()'''
# Create the set
colors={"red", "green", "blue"}

# Print the set
print(colors)

# Add "yellow"
colors.add('yellow')

# Remove "green"
colors.discard('green')

# Print the number of items
print(len(colors))
######
#Dict
'''Inside the editor, complete the following steps:
Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
Print the value of the "model" key
Add a new key "color" with the value "red"
Remove the "brand" key using pop()
Print the dictionary'''
# Create the dictionary
car={'brand':'Ford', 'model':'Mustang', 'year':2024}

# Print the model
print(car['model'])

# Add a color key
car['color']='red'

# Remove the brand key
car.pop('brand')

# Print the dictionary
print(car)