from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# 1. shortest_names


def shortest_names(countries):
    for country in countries:
        if len(country) == len(min(countries, key=len)):
            print(country)

# 2. most_vowels, top three


vowels = ['a', 'e', 'i', 'o', 'u']
count_list = []


def most_vowels(countries):
    # loop through each country
    for country in countries:
        country = country.lower()
        count = 0
        # loop through each letter in country
        for letter in country:
            # check if the letter is a vowel
            if letter in vowels:
                count += 1

        count_list.append(count)

    print(count_list)

    # find highest value in count_list
    highest_count = int(max(count_list))

    indices_highest_count = [index for index, value in enumerate(count_list) if value == highest_count]

    for i in indices_highest_count:
        print(countries[i])


    # create new list without the highest value
    new_count_list = count_list
    new_count_list.remove(highest_count)
    print(new_count_list)

    # find second largest
    second_count = int(max(new_count_list))
    indices_second_count = [index for index, value in enumerate(new_count_list) if value == second_count]

    for j in indices_second_count:
        print(countries[j])

    # create new list without second largest value
    third_count_list = new_count_list
    third_count_list.remove(second_count)
    print(third_count_list)
    # find third largest value
    third_count = int(max(third_count_list))
    indices_third_count = [index for index, value in enumerate(third_count_list) if value == third_count]

    for y in indices_third_count:
        print(countries[y])


""" Poging 
    # loop trough countries
    for country in countries:
        country_vowels = 0
        # loop through country
        for letter in country:
            # check amount of vowels and save in variable
            if letter in vowels:
                country_vowels += 1
        
        # save to amount of vowels to vowel_list
        vowel_list.append(country_vowels)

    # order list and find first three values
    top_1 = max(vowel_list)
    index_top_1 = [index for index, value in enumerate(vowel_list) if value == top_1]
    
    for index in index_top_1:
        print(f'The first place most goes to: {countries[index]}')
        
    
    top_2 = max(vowel_list)
    index_top_2 = [index for index, value in enumerate(vowel_list) if value == top_2]

    print('The second place goes to: ')
    for index in index_top_2:
        print(countries[index])"""


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

#shortest_names(countries)

most_vowels(countries)
