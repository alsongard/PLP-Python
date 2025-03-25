actor_details = {"name": ["Tony Stalk", "Thor Odinson", "Banner Bruce", "Fury Jackson", "Natasha Raminon", "Steve Rodgers", "Sam Wilson"],
                    "age" : [45,38,35,59,35,49,40],
                    "movie" : ["iron_man", "thor_1&2&3","Hulk", "Avengers", "Black Widow", "Captain America", "Winter Soldier & Falcon"]
                }

print(actor_details)

print("\n")
# print keys
print(actor_details.keys())


# print values
print("\n")
print(actor_details.values())


# check if empty
print("\n")

print(all(actor_details)) # all returns true only if all keys evaluate to True otherwise false

print(any(actor_details)) # atleast one key value evaluates to True, otherwise False


print("\n")
# length() : returns the number of keys in a dictionary
print(len(actor_details))

print("\n")
# sorted(): returns a list of the sorted key values in a dictionary
print(sorted(actor_details))

print("\n")
# clear(): this is an method that removes everything inside a dictionary(key,values)
# print(actor_details.clear())
# print(actor_details)

# to test for key in a dictionary we use:
print("age" in actor_details)


# itrating in a dictionary
for key in actor_details:
    print(f"Key : {key} || Value: {actor_details[key]}")


my_planet_dictionary={1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus'}


# using items() method
"""
the item method returns a key, value pair of the dictionary
"""
for planet_number, planet_name in my_planet_dictionary.items():
    print(f"The planet {planet_name} is number {planet_number} in the solar system.")
# for index, planet in enumerate(my_planet_dictionary):
#     print(planet)

# using enumerate() in dictionaries
for count_value, (planet_number, planet_name)in enumerate(my_planet_dictionary.items(), start=1):
    print(f"the index is {count_value} and value is {planet_name}")