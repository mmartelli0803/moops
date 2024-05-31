import csv

# Aggregated list of top drama movies from various sources
movies = [
    ("The Godfather", "A crime family's rise and near fall as told through the eyes of its patriarch and son.", 1972),
    ("Schindler's List", "The true story of a man who saved thousands of Jews during World War II.", 1993),
    ("The Shawshank Redemption", "Two imprisoned men bond over several years, finding solace and eventual redemption through acts of common decency.", 1994),
    ("The Dark Knight", "Batman faces the Joker, a criminal mastermind who wants to plunge Gotham City into anarchy.", 2008),
    ("Pulp Fiction", "The lives of two mob hitmen, a boxer, and a pair of diner bandits intertwine in four tales of violence and redemption.", 1994),
    ("Fight Club", "An insomniac office worker and a devil-may-care soap maker form an underground fight club.", 1999),
    ("Forrest Gump", "The presidencies of Kennedy and Johnson, Vietnam, and more through the perspective of an Alabama man with a low IQ.", 1994),
    ("Inception", "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into a CEO's mind.", 2010),
    ("The Lord of the Rings: The Return of the King", "The final confrontation between the forces of good and evil fighting for control of the future of Middle-earth.", 2003),
    ("The Good, the Bad and the Ugly", "A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold.", 1966),
    # ... more movies to complete the list up to 100
]

# Path to the CSV file
csv_file_path = "top_100_drama_movies.csv"

# Writing to CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(["Movie", "Summary", "Year"])
    # Writing the movie data
    writer.writerows(movies)

print(f"CSV file '{csv_file_path}' has been created successfully.")
