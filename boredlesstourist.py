# The Boredless Tourist
# Sample implementation for tracking destinations and matching traveler interests

# List of destinations
destinations = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt"
]

# Sample traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# Function to get destination index
def get_destination_index(destination):
    return destinations.index(destination)

# Function to get traveler location index
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# Initialize attractions for each destination
attractions = [[] for destination in destinations]

# Function to add an attraction
def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return

# Adding some sample attractions
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Function to find attractions in a destination that match traveler interests
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []

    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
                break  # Avoid duplicates if multiple interests match

    return attractions_with_interest

# Function to generate a personalized message for the traveler
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    interests_string += ", ".join(traveler_attractions) + "."
    return interests_string

# Testing the system
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)  # ['LACMA']

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)  # "Hi Dereck Smill, we think you'll like these places around Paris, France: Arc de Triomphe"
