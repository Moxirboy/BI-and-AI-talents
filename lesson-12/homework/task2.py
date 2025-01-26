import requests
import random

API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your TMDB API key

def get_genre_id(genre_name):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching genres. Please check your API key and internet connection.")
        return None
    try:
        genres = response.json()['genres']
    except KeyError:
        print("Unexpected response format from API.")
        return None
    for genre in genres:
        if genre['name'].lower() == genre_name.lower():
            return genre['id']
    return None

def get_random_movie(genre_id):
    # First, find out the total number of pages
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching movies. Please try again later.")
        return None
    try:
        data = response.json()
        total_pages = data['total_pages']
        if total_pages == 0:
            print("No movies found in this genre.")
            return None
    except KeyError:
        print("Unexpected response format from API.")
        return None
    
    # Select a random page
    random_page = random.randint(1, total_pages)
    url = f'{url}&page={random_page}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching movies. Please try again later.")
        return None
    try:
        movies = response.json()['results']
        if not movies:
            print("No movies found on the selected page.")
            return None
    except KeyError:
        print("Unexpected response format from API.")
        return None
    
    return random.choice(movies)

def main():
    genre = input("Enter a movie genre: ").strip()
    if not genre:
        print("No genre entered. Exiting.")
        return
    
    genre_id = get_genre_id(genre)
    if genre_id is None:
        print(f"Genre '{genre}' not found.")
        return
    
    movie = get_random_movie(genre_id)
    if not movie:
        return
    
    print("\nRecommended Movie:")
    print(f"Title: {movie.get('title', 'N/A')}")
    print(f"Overview: {movie.get('overview', 'No overview available.')}")
    print(f"Release Date: {movie.get('release_date', 'N/A')}")
    print(f"Rating: {movie.get('vote_average', 'N/A')}/10")

if __name__ == "__main__":
    main()
