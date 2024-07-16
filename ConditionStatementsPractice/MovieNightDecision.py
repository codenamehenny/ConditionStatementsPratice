# You are developing a feature for a movie streaming platform that suggests a movie genre to users based on their current mood 
# and the day's weather. The platform has the following recommendation criteria:
# If the user is feeling "happy" and the weather is "sunny", recommend a "Comedy".
# If the user is feeling "happy" but the weather is not "sunny", recommend a
#"Romantic" movie.
# If the user is feeling "sad", recommend a "Drama".
# For any other mood, recommend an "Adventure" movie.

# user tells us mood and weather
mood = input("How are you feeling today? ")
weather = input("How is the weather like? ")

#conditions to match movie genre
if mood == "happy" and weather == "sunny":
    print("Watch a comedy movie")
elif mood == "happy" and weather != "sunny":
    print("Watch a romantic movie")
elif mood == "sad":
    print("Watch a drama movie")
else:
    print("Watch an adventure movie")