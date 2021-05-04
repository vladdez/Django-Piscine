import sys

def my_search(word):
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
    if word in states:
        print(capital_cities[states[word]], 'is the capital of', word)
    elif word in capital_cities.values():
        for key1 in capital_cities:
            if word == capital_cities[key1]:
                acronym = key1
        for key2 in states:
            if acronym == states[key2]:
                print(capital_cities[acronym], 'is the capital of', key2)
    else:
        return 0


def get_data():
    if len(sys.argv) == 2:
        words = sys.argv[1].split(',')
        words = list(map(str.strip, words))
        initial = words.copy()
        words = list(map(str.casefold, words))
        words = list(map(str.title, words))
        for i in range(len(words)):
            if words[i] != '':
                if (my_search(words[i]) == 0):
                    print(initial[i], "is neither a capital city nor a state")


if __name__ == '__main__':
    get_data()