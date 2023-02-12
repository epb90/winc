# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Part 1: Greet Template

def greet(name='', template='Hello, <name>!'):
    return template.replace('<name>', name)

# Part 2: Force

def force(mass = float, body = 'earth'):

    bodies = {
        'sun': 274,
        'jupiter': 24.92,
        'neptune': 11.15,
        'saturn': 10.44,
        'earth': 9.798,
        'uranus': 8.87,
        'venus': 8.87,
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62,
        'pluto': 0.58
    }

    return round(mass * bodies[body], 1)

# Part 3: Gravity

def pull(m1, m2, d):
    G = 6.674 * (10 ** -11) # gravity constant
    return G * ((m1 * m2) / (d ** 2))

