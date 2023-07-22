# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains
# 2 Dictionaries.
#
# Write a function that will work with the following line of code to add the entry for Russia to the
# travel_log.
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#
#     You've visited Russia 2 times.
#
#     You've been to Moscow and Saint Petersburg.

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_country(country_visited, times_visited, cities_visited):
    new_dict = {'country' : country_visited, 'visits' : times_visited, 'cities' : cities_visited}
    travel_log.append(new_dict)


add_country('Russia', 55, ['Moscow', 'Saint Petersburg'])
print(travel_log)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order['main'][2][0])

