from random import randint, choice

from names import get_first_name, get_last_name


def generate_gender():
    return choice(('m', 'f'))


def generate_first_name(gender):
    gender = 'male' if gender == 'm' else 'female'
    return get_first_name(gender)


def generate_last_name():
    return get_last_name()


def generate_attitude():
    return randint(0, 100)


def generate_levels(n, bonuses=()):
    levels = []
    bonuses = bonuses + (0,) * (n - len(bonuses))
    for i in range(n):
        level = max(1, min(randint(1, 5) + bonuses[i], 5))
        levels.append(level)
    return levels
