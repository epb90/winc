# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

"""Factors:
            Weather:    Time of Day:    Cow Milk Status (Boolean):      Location of cows:   Season:     Slurry tank:        Grass status:
            - rainy     day             Need milking: True              pasture             winter      Full: True          Long: True
            - sunny     night           Don't need milking: False       cowshed             spring      Not Full: False     Short: False
            - windy                                                                         summer
            - neutral                                                                       fall                                                            
            
    --> Actions:
    
        take cows to cowshed --> when : - PASTURE at NIGHT
                                        - PASTURE with RAIN
        
        milk cows            --> when : - Need MILKING TRUE  when
                                            - Cows in COWSHED
                                        
        fertilize pasture    --> when : - Slurry FULL TRUE   when 
                                            - cows in COWSHED
                                            = weather != sunny or windy 
                                            
        mow grass            --> when : - grass Long TRUE
                                        - SPRING
                                        - SUNNY
                                        but only when:
                                        cows in COWSHED
                                        
        wait    --> when no other actions"""

# functie
from turtle import back


def farm_action(weather, time_of_day, need_milking, location, season, tank_full, grass_long):
    check_1 = False
    check_2 = False
    check_3 = False
    check_4 = False
    check_5 = False

# in geval van pasture en 1 can be milked
    if location == 'pasture' and need_milking == True:
        take_cows_to_cowshed = "take cows to cowshed"
        milk_cows = "milk cows"
        back_to_pasture = "take cows back to pasture"
        return f"{take_cows_to_cowshed}\n{milk_cows}\n{back_to_pasture}"

# in geval van pasture en fertilize 
    if weather != 'sunny' and weather != 'windy' and tank_full == True and location != 'cowshed':
        take_cows_to_cowshed = "take cows to cowshed"
        fertilize_pasture = "fertilize pasture"
        back_to_pasture = "take cows back to pasture"
        return f"{take_cows_to_cowshed}\n{fertilize_pasture}\n{back_to_pasture}"

# in geval van pasture en mow grass
    if grass_long == True and season == 'spring' and weather == 'sunny' and location != 'cowshed':
        take_cows_to_cowshed = "take cows to cowshed"
        mow_grass = "mow grass"
        back_to_pasture = "take cows back to pasture"
        return f"{take_cows_to_cowshed}\n{mow_grass}\n{back_to_pasture}"
        
# eerste actie: take cows to cowshed
    if location == 'pasture' and weather == 'rainy' or location == 'pasture' and time_of_day == 'night':
        check_1 = True
        take_cows_to_cowshed = "take cows to cowshed"
        return take_cows_to_cowshed

# tweede actie: milk cows
    elif location == 'cowshed' and need_milking == True:
        check_2 = True
        milk_cows = "milk cows"
        return milk_cows

# derde actie: fertilize pasture
    elif weather != 'sunny' and weather != 'windy' and tank_full == True and location == 'cowshed':
        check_3 = True
        fertilize_pasture = "fertilize pasture"
        return fertilize_pasture

# vier actie: mow grass
    elif location == 'cowshed' and grass_long == True and season == 'spring' and weather == 'sunny':
        check_4 = True
        mow_grass = "mow grass"
        return mow_grass

# wait - bij geen enkele actie
    else:
        return "wait"



result_1= farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)

print(result_1)

result_2 = farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)

print(result_2)

result_3 = farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)

print(result_3)

result_4 = farm_action('sunny', 'day', False, 'pasture', 'spring', False, True)

print(result_4)
