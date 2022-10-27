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

def farm_action(weather, time_of_day, need_milking, location, season, tank_full, grass_long):
    if location == 'pasture' and weather == 'rainy' or location == 'pasture' and time_of_day == 'night':
        return "take cows to cowshed"
    
    if location == 'cowshed' and need_milking == True:
        return "milk cows"

    if weather != 'sunny' and weather != 'windy' and tank_full == True and location == 'cowshed':
        return "fertilize pasture"

    if location == 'cowshed' and grass_long == True and season == 'spring' and weather == 'sunny':
        return "mow grass"

