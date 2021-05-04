import sys

def state():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if len(sys.argv) == 2:
        city = sys.argv[1]
        if city in capital_cities.values():
            for key1 in capital_cities:
                if city == capital_cities[key1]:
                    acronym = key1
            for key2 in states:
                if acronym == states[key2]:
                    print(key2)
        else:
            print("Unknown capital city")

if __name__ == '__main__':
    state()