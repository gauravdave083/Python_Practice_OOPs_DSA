#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# Create an empty list to store the favorite movies
favorite_movies = []

# Prompt the user to enter the names of their favorite movies
for i in range(3):
    movie_name = input(f"Enter the name of your favorite movie #{i+1}: ")
    favorite_movies.append(movie_name)

# Print the list of favorite movies
print("Your favorite movies are:")

print(favorite_movies)