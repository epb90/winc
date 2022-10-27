# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
# Variable for every player that scored

scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

# Integer must be converted to string



scorers = scorer_0 + ' ' + str(goal_0) + ", " + scorer_1 + ' ' + str(goal_1)

print(scorers)
report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"
print(report)

# Part 2
player = 'Ruud Gullit'

first_name = player[:player.find(' ')]
print(first_name)


last_name = player.split()[1]
print(last_name)

last_name_len = len(last_name)
print(last_name_len)

name_short = f"{player[0]}. {last_name}"
print(name_short)

chant = (len(first_name) - 1) * f"{first_name}! " + f"{first_name}!"
print(chant)

good_chant = chant[-1] != " "
print(good_chant)
