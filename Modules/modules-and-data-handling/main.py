#Task 1: Your Mood Today - Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today and responds with a custom message based on the mood entered.

import mood_responses
mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))