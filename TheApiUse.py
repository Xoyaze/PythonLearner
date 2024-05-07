import requests
import sys

api_key  = 'd741e715fe272578d562d25d122e2e08'

def getMovies(url):
    fullURL = url + '&api_key=' + api_key

    response = requests.get(fullURL)
    if response.status_code == 200:
        data = response.json()
        return (data.get('results'))
    
    else: 
        print("Failed to get the data.")
        return []



def main():
    print("1- To view popular movie titles")
    print("2- To view top rated movie titles")
    print("3- To view upcoming movie titles")

    userInput = int(input("Enter your choice: "))
    choice = ''

    if userInput == 1:
        url = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1'
        choice = 'Popular'

    elif userInput == 2:
        url = 'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1'
        choice = 'Top Rated'


    elif userInput == 3:
        url = 'https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1'
        choice = 'Upcoming'

    
    else:
        sys.exit("You need to enter a valid choice.")


    def printOverview(movieTitle, movies):
        print()
        print("**********")
        print(f"Movie title: {movieTitle}")
        print()
        print("Movie Overview: ")
        print()
        for movie in movies:
            if movieTitle == movie['title']:
                print(movie['overview'])

        print("**********")
        print()
        print()


    movies = getMovies(url)


    movieTitles = []

    for movie in movies:
        movieTitles.append(movie['title'])

    print()
    print()

    print(f"***** The {choice} Movie Titles *****")
    print()
    i = 1
    for titles in movieTitles:
        print(f"{i}. {titles}")
        i += 1


    print()
    print()
    print("********************")

    print()

    while True:
        print("If you want an overview for anyone of the movies above, type their number")
        overview = int(input("Enter the number here (0 for exiting the program): "))

        if overview == 0:
            sys.exit("You have chose to exit the program")
        
        elif overview > len(movieTitles):
            print("The number cannot be greater than the number of movies")
        
        else:
            printOverview(movieTitles[overview - 1], movies)



        




main()
    
    