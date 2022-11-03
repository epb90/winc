# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
# 1
switzerland_most_spoken = 'German'
spain_most_spoken = 'Castilian Spanish'
print(switzerland_most_spoken == spain_most_spoken) # False

#2
switzerland_religion = 'Roman Catholic'
spain_religion = 'Roman Catholic'
print(switzerland_religion == spain_religion) # True

#3
switzerland_capital = 'Bern'
switzerland_capital_len = len(switzerland_capital)
spain_capital = 'Madrid'
spain_capital_len = len(spain_capital)
print(switzerland_capital_len != spain_capital_len) # True

#4
switzerland_gdp = 1714860000000
spain_gdp = 59071000000000
print(switzerland_gdp > spain_gdp) # True

#5
switzerland_population_growth = 0.65
spain_population_growth = 0.13
print(switzerland_population_growth and spain_population_growth < 1) # True

#6
switzerland_population = 8508698
spain_population = 47163418
print(switzerland_population > 10000000 or spain_population > 10000000) # True

#7
switzerland_bool = switzerland_population > 10000000
spain_bool = spain_population > 10000000
True == 0
False == 1

print(switzerland_bool + spain_bool == 1)
