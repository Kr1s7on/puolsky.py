import csv

# Global variables to store the last search query and its results
last_query = None
last_results = None

def load_films(file_path):
    films = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            films.append(row)
    return films

def search_film(films, query):
    global last_query, last_results

    # If the query is "last", display the last search query and its results
    if query.lower() == "last":
        print(f"Last query: {last_query}")
        print(f"Found {len(last_results)} results.")
        for film in last_results:
            print(f"\nTitle: {film['title']}\nDirector: {film['director']}\nYear: {film['year']}\nGenre: {film['genre']}\n{'-'*40}")
        return

    # Split the query into multiple terms
    terms = query.split()

    # Search for each term separately and combine the results
    results = [film for film in films for term in terms if term.lower() in film['title'].lower() or term.lower() in film['director'].lower() or term.lower() in str(film['year']).lower() or term.lower() in film['genre'].lower()]

    print(f"Found {len(results)} results.")
    for film in results:
        print(f"\nTitle: {film['title']}\nDirector: {film['director']}\nYear: {film['year']}\nGenre: {film['genre']}\n{'-'*40}")

    # Store the query and its results in the global variables
    last_query = query
    last_results = results

films = load_films("movies.csv")

search_term = input("Enter a search term: ")

search_film(films, search_term)