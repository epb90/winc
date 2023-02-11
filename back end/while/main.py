from helpers import random_koala_fact
import json
import re

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# 1. X number of unique koala facts
def unique_koala_facts(amount):
    unique_list = []
    i = 0

    while amount > len(unique_list):
        i += 1
        fact = random_koala_fact()

        if fact not in unique_list:
            unique_list.append(fact)

        if i >= 1000:
            break

    return unique_list

# 2. number of unique joey facts in database

def num_joey_facts():

    dict_count_facts = {}
    max_value = 0
    
    while max_value < 10:
        fact = random_koala_fact()
        if fact in dict_count_facts:
            dict_count_facts[fact] += 1
        else:
            dict_count_facts[fact] = 1
        max_value = dict_count_facts[max(dict_count_facts, key = dict_count_facts.get)]

    count_joey_facts = 0
    for i in dict_count_facts:
        if 'joey' in i.lower():
            count_joey_facts += 1

    return count_joey_facts

# 3. koala weight
def koala_weight():

    with open('facts.json') as file:
        koala_facts = json.load(file)

    for string in koala_facts:
        if 'kg' in string:
            kg_string = string

    kg_string_to_list = kg_string.split()
    for part in kg_string_to_list:
        if 'kg' in part:
            kilogram_koala = int(''.join(filter(str.isdigit, part)))

    return kilogram_koala

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    
    print(unique_koala_facts(10))
    print(num_joey_facts())
    print(koala_weight())
