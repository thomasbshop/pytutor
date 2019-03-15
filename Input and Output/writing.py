
# cities = ["Nairobi", "Dar es salaam", "Kigali", "Mombasa", "Kisumu"]
# with open("/home/thomasj/Desktop/py tutor/py/tutorialdev/Input and Output/cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

cities = []
with open("/home/thomasj/Desktop/py tutor/py/tutorialdev/Input and Output/cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))  # .strip() method

print(cities)
for city in cities:
    print(city)


# it is not good to use 'eval' to extract data from your file because the contents could change.

# appending to a text file
# causing data to be written at the end of a text file without overriding the existing contents
