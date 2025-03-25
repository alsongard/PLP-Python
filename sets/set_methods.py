# update() method
# the update() method is used to add values from another collection data structure(list) to the tuple.
tech_companies=("apple","microsoft","google")
new_tech_companies={"linux","tesla"}
new_tech_companies.update(tech_companies)
print(new_tech_companies)


# discard() method
# the discard() method is used to remove an elemnent from a list
new_tech_companies.discard("microsoft")
print(f"Using discard() to remove microsoft from set {new_tech_companies}")


# the ``enumerate()`` function is used to return a counter value/index value together with an item/value of iterable data type(list, dictionary)
my_new_dictionary={1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus'}
for index,(item_index, item_value) in enumerate(my_new_dictionary.items()):
    print(index,item_value)


# union | Union()
myset_a={1,2,3,5}
myset_b={2,4,5,11}
print(myset_b | myset_a)
new_union_set = myset_a.union(myset_b)
print(new_union_set)

# intersection  only contains common values between the sets
print(myset_a & myset_b)
print(myset_a.intersection(myset_b))


# difference: use - or difference() to get the different values between 2 sets| values are not common in both

new_set_a = {1,3,5,9}
new_set_b = {1,10,2,9}

# difference
print(new_set_a - new_set_b)


print('\n')
value={12,20,24,30}
value.add(34)
print(value)