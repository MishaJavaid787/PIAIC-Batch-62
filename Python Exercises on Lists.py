# Exercise 3-1: Names
names= ["Javaria", "Anum", "Mehtab", "Amazia"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Exercise 3-2: Greetings
for name in names: 
    print ('Hi '+ name+', it has been a long time since we last met.')
# Loop through the list and print individual message for each name

# Exercise 3-3: Your Own List
fave_cars= ["Audi V6", "MG5 EV", "Changan Alsvin", "Civic Type R"]
for vehicle in fave_cars:
    print ('I would love to own ' +vehicle+', because it is my dream car.')

# Exercise 3-4: Guest List
    guests_list= ["Sahar", "Mannan", "Nour", "Dannial"]
# Loop through the guest_list and print invite to each guest
for guest in guests_list:
    print ('Hello, ' + guest +'! I hope you will attend my birthday party on Sunday.')

# Exercise 3-5: changing Guest printList, 
print ("Nour is unable to come due to her other commitments, so I will invite Momina now.")
guests_list[2]= "Momina" 
print (guests_list) 
for guest in guests_list:
    print ('Hello, ' + guest +'! I hope you will attend my birthday party on Sunday.')

# Exercise 3-6: More Guests
print ("Hello, I have booked a bigger table in a nice Cafe to invite more people to celebrate my birthday.")
guests_list.insert (0, "Mehwish") #add one new guest to the beginning.
guests_list.insert (3, "Rubeena") #add one new guest in the middle.
guests_list.append ("Sana") #add one new guest to the end.
print(guests_list)
for guest in guests_list:
    print ('Hello, ' + guest +'! I hope you will attend my birthday party in Arcadian Cafe on Sunday.')

# Exercise 3-7: Shrinking Guest List
guests_list1 = ["Mehwish", "Sahar", "Mannan", "Rubeena", "Momina", "Dannial", "Sana"]
print ("I will invite only Mannan and Momina at my home for a small dinner party tonight.")
guests_list1.pop(0)
print (guests_list1) 
print ("Sorry Mehwish, I will cancel my birthday party in Arcadian cafe this sunday due to personal reasons.")
guests_list1.pop(0)
print (guests_list1) 
print ("Sorry, Sahar,  I will cancel my birthday party in Arcadian cafe this Sunday due to personal reasons.")
guests_list1.pop(1)
print (guests_list1) 
print ("Sorry, Rubeena, I will cancel my birthday party in Arcadian cafe this Sunday due to personal reasons.")
guests_list1.pop(2)
print (guests_list1) 
print ("Sorry, Dannial, I will cancel my birthday party in Arcadian cafe this Sunday due to personal reasons.")
guests_list1.pop()
print (guests_list1) 
print ("Sorry, Sana, ' I will cancel my birthday party in Arcadian cafe this Sunday due to personal reasons.")
for guest in guests_list1:
    print ('Hello, ' + guest +'! I hope you will attend my small birthday party tonight at my home.')
del guests_list1
# print (guests_list1)

# Exercise 3-8: Seeing the World
fave_places = ["Japan", "Thailand", "Paris", "Italy", "Pakistan"]
fave_places.sort()
print(fave_places)
fave_places.sort(reverse = True)
print(fave_places)
fave_places.reverse() 
print(fave_places)
fave_places.reverse() 
print(fave_places)
fave_places.sort()
print(fave_places)
fave_places.sort(reverse = True)
print(fave_places)

# Exercise 3-9: Every Function

languages = ["French", "Irish", "Japnese", "Arabic", "Korean"]
for language in languages: 
    print ('Hi '+ language+' is my favourite language.')
    print ('I will love to visit the country where '+ language+' language is spoken.')
print ("I have recently started learning Chinese Language.")
languages. append ("Chinese")
print (languages)
for language in languages: 
    print ('I want to learn ' + language +' to enjoy my trip to this country.')
print ("I should rather learn to speak English more fluently than Irish Language.")
languages.insert (1, "English")
print (languages)
languages.pop(2)
print (languages)
del languages[(3)]
print (languages)

# sorting lists
languages.sort()
print(languages)
languages.sort(reverse = True)
print(languages)
languages.reverse()
print(languages)
languages.sort(reverse = True)
print(languages) 
languages.sort()
print(languages)

# Exercise 3-10: Intentional Error
guests_list1 = ["Mehwish", "Sahar", "Mannan", "Rubeena", "Momina", "Dannial", "Sana"]
# guests_list1.pop(7)
guests_list1.pop(6)
print (guests_list1) 


























    










