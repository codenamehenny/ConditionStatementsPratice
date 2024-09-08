def mood_response(mood):
    mood = mood.lower()
    if mood == "happy":
        return "It's always a good day to be happy"
    elif mood == "sad" or "depressed":
        return "Oh no, try to find something to lift your spirits!"
    elif mood == "excited":
        return "THAT'S AWESOME!"
    elif mood == "angry" or "mad":
        return "Take a breather and revisit the situation"