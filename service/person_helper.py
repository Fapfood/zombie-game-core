from random import randint, choice

from names import get_first_name, get_last_name


def generate_gender():
    return choice(('m', 'f'))


def generate_first_name(gender):
    gender = 'female' if gender == 'f' else 'male'
    return get_first_name(gender)


def generate_last_name():
    return get_last_name()


def generate_attitude():
    return randint(51, 100)


def generate_age():
    return randint(15, 65)


def generate_icon(gender, age):
    if age <= 18:
        males = ['👦']
        females = ['👧']
    elif age > 50:
        males = ['👴', '👨‍🦳']
        females = ['👵', '👩‍🦳']
    else:
        males = ['👨', '🧔', '👨‍🦰', '👨‍🦱', '👨‍🦲', '👱‍♂️']
        females = ['👩', '👩‍🦰', '👩‍🦱', '👩‍🦲', '👱‍♀️']

    if gender == 'f':
        return choice(females)
    else:
        return choice(males)


def generate_levels(n, bonuses=()):
    levels = []
    bonuses = bonuses + (0,) * (n - len(bonuses))
    for i in range(n):
        level = max(1, min(randint(1, 5) + bonuses[i], 5))
        levels.append(level)
    return levels
