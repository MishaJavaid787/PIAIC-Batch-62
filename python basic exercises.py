# 1. Simple Message
print("Hello, Students!")
# 2. Simple Messagse
print("Python is a fun course.")
print ("You will enjoy learning python.")
# 3. Personal Message
name= "Mehwish"
print ("Welcome, "+name+" to the first class of python programming." )
# 4. Name Cases
Name = "Mannan" " Javaid"
lower_Name = Name.lower() # Convert to lower case
print(lower_Name)
upper_Name = Name.upper() # Convert to Upper case
print(upper_Name)
title_Name = Name.title() # Convert to title case
print(title_Name)
# 5. Famous Quote
print ("Bruce Lee once said,""Do not pray for an easy life. Pray for the strength to endure a difficult one.")
# 6. Famous Quote (2)
famous_person = "John Quincy Adams"
message = "If your actions inspire others to dream more, learn more, do more and become more, you are a leader."
print(f"'{message}'- {famous_person}")
# 7. Stripping Names
text = "  Welcome, \nMomina\tShuja!  "
print (text)
stripped_text = text.strip("") # strip() text
print(f"'{stripped_text}'")
left_stripped_text = text.lstrip() # lstrip() text
print(f"'{left_stripped_text}'")
right_stripped_text = text.rstrip() # rstrip() text
print(f"'{right_stripped_text}'")
# 8. Variable Sum
x,y,z = 5,10,15
sum = x+y+z
print ('the sum is:',sum)
# 9. Variable Swap
a=10
b=20
print ('a=',a)
print ('b=',b)
a,b = b,a # swap the values
print ('after swapping:')
print("a =", a)
print("b =", b)
# 10. Favorite Color
Fave_colour = "Purple"
print ("I love wearing " + Fave_colour+ " colour dresses, shoes and accessories.")
least_fave_colour = "Grey"
print ("The different shades of " +least_fave_colour+ " are although quite functional but they are very boring colours.")
pet_name = "Buddy"
print(pet_name)
# 11. change the pet name
pet_name = "Max"
print (pet_name)
# 12. Observing Name Error
weather_forecast = "Sunshine"
print (weather_forecast)
# print (weather-forecast) (Name Error)
# 13. Reassigning Score
score = 100
print ("Initial score :", score)
if score >= 90:
    score +=20 # Add 20 points if the score is above and equal to 90
print("Reassigned_score:", score)
# 14. City Name
city_name = '"Lahore"'
print (city_name)
# 15. Title Case Text
Text = "Python programming"
title_Text = Text.title()
print(title_Text)
# 16. Lowercase Conversion
str = "mehwish is learning Python in PIAIC batch 62."
lower_str = str.lower()
print (lower_str)
# 17. Uppercase Conversion
Str = "Zeina is 30 Years old and 5.9 feet tall."
upper_Str = Str.upper()
print (upper_Str)
# 18. Current Temperature
temperature = 31 
print ("The current temperature is" ,temperature, "degree celcius.")
# 19. Printing Poem
poem = """
In ancient lands, beneath the sun,
Where battles are lost and victories won,
A simple stone, so meek and small,
Becomes a symbol for all.
It speaks of struggles, of dreams so vast,
Of a future built, from the shadowed past,
Against the mighty, it takes its stand,
A symbol of resistance, in a striving land.
Though time may pass, its tale remains,
A testament to courage, amidst the pains,
For in each stone, a story is cast,
Of a resilient spirit, steadfast.
"""
print(poem)
