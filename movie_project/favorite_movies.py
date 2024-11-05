# Movie Management Program

# empty dictionary to store movie information
movies = {}

# Add a movie to the dictionary
def add_movie(title, genre, rating):
    movies[title] = {'genre': genre, 'rating': rating}
    print(f'Movie "{title}" added successfully.')

# checking if a movie exists in the list and deleting it
def remove_movie(title):
    if title in movies:
        del movies[title]
        print(f'Movie "{title}" removed successfully.')
    else:
        print(f'Movie "{title}" not found in the list.')

# checking if there are items in movie lists and displaying the movies and their details
def display_movies():
    if not movies:
        print("No movies in the list.")
        return
    print("Movies in your list:")
    for title, details in movies.items():
        print(f'Title: {title}, Genre: {details["genre"]}, Rating: {details["rating"]}')
        
# Main function to run the movie management program, handling user inputs and calling functions for each option
def main():
    while True:
        print("\nWelcome to the Movie Favorites Manager!")
        print("1. Add a movie\n2. Remove a movie\n3. View movies\n4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            title = input("Enter the movie title: ")
            genre = input("Enter the movie genre: ")
            rating = input("Enter the movie rating: ")
            add_movie(title, genre, rating)
        elif choice == '2':
            title = input("Enter the movie title to remove: ")
            remove_movie(title)
        elif choice == '3':
            display_movies()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main function to start the program
if __name__ == "__main__":
    main()