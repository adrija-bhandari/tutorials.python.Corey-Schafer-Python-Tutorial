names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

#my_dict = {}
#for name, hero in zip(names, heroes):
   #my_dict[name] = hero
#print(my_dict)

my_dict = {name: hero for name, hero in zip (names, heroes) if name != 'Peter'}
print(my_dict)